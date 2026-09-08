"""Tela Principal - Dashboard + CRUD + Features."""
import os

os.environ.setdefault("QT_API", "pyside6")

from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PySide6 import QtGui
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QFileDialog,
    QFrame,
    QGridLayout,
    QHBoxLayout,
    QInputDialog,
    QLabel,
    QLineEdit,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QStackedWidget,
    QTableWidget,
    QTableWidgetItem,
    QTabWidget,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)

from PySide6.QtCore import QTimer

from src.auth.license import validate_license
from src.auth.session import session
from src.config import Config
from src.features.books import BooksCRUD
from src.features.collaborators import CollaboratorsCRUD
from src.features.import_data import export_template, import_books, import_readers
from src.features.loans import LoansCRUD
from src.features.notifications import NotificationsCRUD
from src.features.premium_promo import promo_manager
from src.features.readers import ReadersCRUD
from src.features.reports import (
    generate_books_report,
    generate_loans_report,
    generate_readers_report,
)
from src.ui.i18n.translator import t
from src.ui.screens.import_paste import ImportPasteScreen
from src.ui.themes.theme_manager import cycle_theme
from src.ui.widgets.premium_badge import PremiumBadge
from src.ui.widgets.premium_promo import PremiumPromoToast
from src.ui.widgets.toast import ToastNotification
from src.utils.constants import (
    APP_AUTHOR, APP_CNPJ, APP_ORG,
    FREE_MAX_BOOKS, FREE_MAX_COLLABS, FREE_MAX_READERS,
)
from src.utils.excel_export import export_books_to_excel, export_readers_to_excel
from src.utils.isbn_api import set_isbn
from src.utils.validators import validate_book, validate_reader


class HomeScreen(QMainWindow):
    def __init__(self, login_screen=None):
        super().__init__()
        self.login_screen = login_screen
        self.setWindowTitle(t("home.title"))
        self.setMinimumSize(1100, 650)
        self.setWindowIcon(QtGui.QIcon(Config.resource_path("img/logoicone.png")))
        self.current_nav = 0
        self.autenticado_colab = False
        self._build_ui()
        self._connect_signals()
        self._update_premium_badge()
        self._navigate(0)
        # Premium promo system
        self._promo_toast = PremiumPromoToast(self)
        self._promo_timer = QTimer(self)
        self._promo_timer.timeout.connect(self._check_promos)
        self._promo_timer.start(30000)  # Verifica a cada 30s
        promo_manager.reset_session()

    def _build_ui(self):
        central = QWidget()
        self.setCentralWidget(central)
        main_layout = QHBoxLayout(central)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # Sidebar
        self.sidebar = QFrame()
        self.sidebar.setObjectName("sidebar")
        self.sidebar.setFixedWidth(220)
        self.sidebar_layout = QVBoxLayout(self.sidebar)
        self.sidebar_layout.setContentsMargins(0, 0, 0, 0)
        self.sidebar_layout.setSpacing(0)

        # Logo area
        logo_frame = QFrame()
        logo_layout = QHBoxLayout(logo_frame)
        logo_layout.setContentsMargins(16, 14, 16, 14)
        logo_layout.setSpacing(10)
        logo_icon = QLabel()
        logo_pixmap = QtGui.QPixmap(Config.resource_path("img/logoicone.png"))
        if not logo_pixmap.isNull():
            logo_pixmap = logo_pixmap.scaledToHeight(30, Qt.TransformationMode.SmoothTransformation)
            logo_icon.setPixmap(logo_pixmap)
        logo_layout.addWidget(logo_icon)
        logo_text = QLabel("LIBRYNO")
        logo_text.setStyleSheet(
            "font-size: 17px; font-weight: bold; color: #5CE1E6; background: transparent;"
        )
        logo_layout.addWidget(logo_text)
        logo_layout.addStretch()
        self.sidebar_layout.addWidget(logo_frame)

        self.sidebar_layout.addSpacing(10)

        # Nav buttons
        self.nav_buttons = []
        nav_items = [
            (t("home.dashboard"), 0),
            (t("home.books"), 1),
            (t("home.readers"), 2),
            (t("home.loans"), 3),
            (t("home.collaborators"), 4),
            (t("home.reports"), 5),
            (t("home.about"), 6),
        ]
        for text, idx in nav_items:
            btn = QPushButton(text)
            btn.setCheckable(True)
            btn.clicked.connect(lambda checked, i=idx: self._navigate(i))
            self.sidebar_layout.addWidget(btn)
            self.nav_buttons.append(btn)

        self.sidebar_layout.addStretch()

        # Theme toggle
        btn_theme = QPushButton("🎨 Tema")
        btn_theme.setCheckable(False)
        btn_theme.clicked.connect(self._toggle_theme)
        self.sidebar_layout.addWidget(btn_theme)

        # Premium badge
        self.badge = PremiumBadge(session.is_premium)
        self.sidebar_layout.addWidget(self.badge)

        # Logout
        btn_logout = QPushButton(t("home.logout"))
        btn_logout.setCheckable(False)
        btn_logout.clicked.connect(self._do_logout)
        self.sidebar_layout.addWidget(btn_logout)

        main_layout.addWidget(self.sidebar)

        # Content area
        content_layout = QVBoxLayout()
        content_layout.setContentsMargins(0, 0, 0, 0)

        # Top bar
        topbar = QFrame()
        topbar.setFixedHeight(50)
        topbar_layout = QHBoxLayout(topbar)
        topbar_layout.setContentsMargins(20, 0, 20, 0)

        self.input_search = QLineEdit()
        self.input_search.setPlaceholderText(t("home.search"))
        self.input_search.setFixedWidth(300)
        self.input_search.returnPressed.connect(self._do_search)
        topbar_layout.addWidget(self.input_search)

        topbar_layout.addStretch()

        btn_notif = QPushButton(f"🔔 {NotificationsCRUD.unread_count()}")
        btn_notif.clicked.connect(self._show_notifications)
        topbar_layout.addWidget(btn_notif)

        content_layout.addWidget(topbar)

        # Stacked pages
        self.stack = QStackedWidget()
        self._build_pages()
        content_layout.addWidget(self.stack)

        main_layout.addLayout(content_layout, 1)

        # Toast
        self.toast = ToastNotification(central)

    def _build_pages(self):
        self.stack.addWidget(self._page_dashboard())
        self.stack.addWidget(self._page_books())
        self.stack.addWidget(self._page_readers())
        self.stack.addWidget(self._page_loans())
        self.stack.addWidget(self._page_collaborators())
        self.stack.addWidget(self._page_reports())
        self.stack.addWidget(self._page_about())

    # ---- Dashboard ----
    def _page_dashboard(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.setContentsMargins(20, 20, 20, 20)

        title = QLabel(t("home.dashboard"))
        title.setObjectName("title")
        layout.addWidget(title)

        # Stats cards
        stats_layout = QHBoxLayout()
        for label_text, getter in [
            ("📚 Livros", lambda: BooksCRUD.count()),
            ("👥 Leitores", lambda: ReadersCRUD.count()),
            ("📖 Empréstimos", lambda: LoansCRUD.count()),
            ("👤 Colaboradores", lambda: CollaboratorsCRUD.count()),
        ]:
            card = QFrame()
            card.setProperty("class", "card")
            card.setFixedHeight(100)
            card_layout = QVBoxLayout(card)
            num = QLabel(str(getter()))
            num.setStyleSheet("font-size: 28px; font-weight: bold; color: #5CE1E6;")
            num.setAlignment(Qt.AlignCenter)
            card_layout.addWidget(num)
            lbl = QLabel(label_text)
            lbl.setAlignment(Qt.AlignCenter)
            lbl.setStyleSheet("color: #a0a0a0;")
            card_layout.addWidget(lbl)
            stats_layout.addWidget(card)

        layout.addLayout(stats_layout)

        # Charts
        charts = QHBoxLayout()

        self.frame_pie = QFrame()
        self.frame_pie.setFixedHeight(280)
        charts.addWidget(self.frame_pie)

        self.frame_bar = QFrame()
        self.frame_bar.setFixedHeight(280)
        charts.addWidget(self.frame_bar)

        layout.addLayout(charts)
        layout.addStretch()
        return page

    def _update_dashboard_charts(self):
        for frame in [self.frame_pie, self.frame_bar]:
            if frame.layout():
                while frame.layout().count():
                    w = frame.layout().takeAt(0).widget()
                    if w:
                        w.deleteLater()

        # Pie chart
        fig1 = Figure(figsize=(4, 4), facecolor="#1a1a2e")
        canvas1 = FigureCanvas(fig1)
        ax1 = fig1.add_subplot(111)
        ax1.set_facecolor("#1a1a2e")
        data = [BooksCRUD.count(), CollaboratorsCRUD.count(), ReadersCRUD.count()]
        labels = ["Livros", "Colab", "Leitores"]
        if sum(data) > 0:
            ax1.pie(data, labels=labels, autopct="%1.1f%%",
                    startangle=90, wedgeprops={"edgecolor": "#1a1a2e"},
                    colors=["#5CE1E6", "#FFD700", "#FF6B6B"])
        ax1.set_aspect("equal")
        fig1.tight_layout()
        if not self.frame_pie.layout():
            self.frame_pie.setLayout(QVBoxLayout())
        self.frame_pie.layout().addWidget(canvas1)

        # Bar chart
        fig2 = Figure(figsize=(6, 4), facecolor="#1a1a2e")
        canvas2 = FigureCanvas(fig2)
        ax2 = fig2.add_subplot(111)
        ax2.set_facecolor("#1a1a2e")
        ax2.tick_params(colors="#a0a0a0")
        for spine in ax2.spines.values():
            spine.set_color("#0f3460")
        loans_stats = LoansCRUD.get_stats()
        ax2.bar(
            ["Ativos", "Devolvidos", "Atrasados"],
            [loans_stats["active"], loans_stats["returned"], loans_stats["overdue"]],
            color=["#5CE1E6", "#2ecc71", "#e74c3c"],
        )
        ax2.set_title("Empréstimos", color="#e0e0e0", fontsize=12)
        fig2.tight_layout()
        if not self.frame_bar.layout():
            self.frame_bar.setLayout(QVBoxLayout())
        self.frame_bar.layout().addWidget(canvas2)

    # ---- Books ----
    def _page_books(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.setContentsMargins(20, 20, 20, 20)

        header = QHBoxLayout()
        title = QLabel(t("books.title"))
        title.setObjectName("title")
        header.addWidget(title)
        header.addStretch()

        btn_export = QPushButton(f"📊 {t('books.export_excel')}")
        btn_export.clicked.connect(lambda: self._export_excel("books"))
        header.addWidget(btn_export)

        btn_import = QPushButton("📥 Importar Planilha")
        btn_import.setProperty("class", "premium")
        btn_import.clicked.connect(lambda: self._import_data("books"))
        header.addWidget(btn_import)

        btn_template = QPushButton("📋 Template")
        btn_template.clicked.connect(lambda: self._export_template("books"))
        header.addWidget(btn_template)

        btn_refresh = QPushButton("🔄 Atualizar")
        btn_refresh.clicked.connect(self._refresh_books_table)
        header.addWidget(btn_refresh)
        layout.addLayout(header)

        # Tab widget
        tabs = QTabWidget()

        # Tab: List
        list_tab = QWidget()
        list_layout = QVBoxLayout(list_tab)
        self.table_books = QTableWidget()
        self.table_books.setAlternatingRowColors(True)
        self.table_books.setSelectionBehavior(QTableWidget.SelectRows)
        list_layout.addWidget(self.table_books)

        btn_row = QHBoxLayout()
        btn_update = QPushButton(t("books.update"))
        btn_update.clicked.connect(self._update_book)
        btn_row.addWidget(btn_update)

        btn_delete = QPushButton(f"🗑 {t('books.delete')}")
        btn_delete.setProperty("class", "danger")
        btn_delete.clicked.connect(self._delete_book)
        btn_row.addWidget(btn_delete)
        btn_row.addStretch()
        list_layout.addLayout(btn_row)

        tabs.addTab(list_tab, t("books.list"))

        # Tab: Register
        reg_tab = QWidget()
        reg_layout = QVBoxLayout(reg_tab)
        form_grid = QGridLayout()
        form_grid.setSpacing(12)

        self.book_inputs = {}
        fields = [
            ("n_tombo", t("books.n_tombo")), ("isbn", t("books.isbn")),
            ("editora", t("books.publisher")), ("ano_edicao", t("books.edition_year")),
            ("classificacao", t("books.classification")), ("n_folhas", t("books.n_sheets")),
            ("titulo", t("books.title")), ("autor", t("books.author")),
            ("volume", t("books.volume")), ("data_cadastro", t("books.date")),
        ]
        for i, (key, label) in enumerate(fields):
            row, col = divmod(i, 2)
            lbl = QLabel(label)
            inp = QLineEdit()
            inp.setFixedHeight(36)
            form_grid.addWidget(lbl, row * 2, col)
            form_grid.addWidget(inp, row * 2 + 1, col)
            self.book_inputs[key] = inp

        # ISBN search
        btn_isbn = QPushButton(t("books.search_isbn"))
        btn_isbn.clicked.connect(self._search_isbn)
        form_grid.addWidget(btn_isbn, len(fields) * 2, 0, 1, 2)

        # Subject (text edit)
        lbl_subject = QLabel(t("books.subject"))
        self.book_subject = QTextEdit()
        self.book_subject.setMaximumHeight(80)
        form_grid.addWidget(lbl_subject, len(fields) * 2 + 1, 0)
        form_grid.addWidget(self.book_subject, len(fields) * 2 + 2, 0, 1, 2)

        reg_layout.addLayout(form_grid)

        btn_save_book = QPushButton(t("books.save"))
        btn_save_book.setFixedWidth(200)
        btn_save_book.clicked.connect(self._save_book)
        reg_layout.addWidget(btn_save_book)
        reg_layout.addStretch()

        tabs.addTab(reg_tab, t("books.register"))
        layout.addWidget(tabs)
        return page

    def _save_book(self):
        data = {k: inp.text().strip() for k, inp in self.book_inputs.items()}
        data["assunto"] = self.book_subject.toPlainText().strip()
        ok, msg = validate_book(data)
        if not ok:
            QMessageBox.warning(self, t("messages.warning"), msg)
            return
        result = BooksCRUD.create(**data)
        if result:
            self.toast.show_toast(t("messages.data_saved"))
            self._refresh_books_table()
            for inp in self.book_inputs.values():
                inp.clear()
            self.book_subject.clear()
        else:
            QMessageBox.critical(self, t("messages.error"), "Erro ao salvar livro.")

    def _refresh_books_table(self):
        data = BooksCRUD.read_all()
        headers = ["ID", "Tombo", "ISBN", "Editora", "Ano", "Classif.", "Folhas",
                    "Título", "Autor", "Vol.", "Cadastro", "Assunto"]
        self.table_books.setColumnCount(len(headers))
        self.table_books.setHorizontalHeaderLabels(headers)
        self.table_books.setRowCount(len(data))
        for row, book in enumerate(data):
            for col, key in enumerate(["id", "n_tombo", "isbn", "editora", "ano_edicao",
                                        "classificacao", "n_folhas", "titulo", "autor",
                                        "volume", "data_cadastro", "assunto"]):
                item = QTableWidgetItem(str(book.get(key, "")))
                self.table_books.setItem(row, col, item)
        self.table_books.resizeColumnsToContents()

    def _update_book(self):
        row = self.table_books.currentRow()
        if row < 0:
            QMessageBox.warning(self, t("messages.warning"), "Selecione um livro.")
            return
        book_id = int(self.table_books.item(row, 0).text())
        data = {k: inp.text().strip() for k, inp in self.book_inputs.items()}
        data["assunto"] = self.book_subject.toPlainText().strip()
        if BooksCRUD.update(book_id, **data):
            self.toast.show_toast(t("messages.data_updated"))
            self._refresh_books_table()

    def _delete_book(self):
        row = self.table_books.currentRow()
        if row < 0:
            return
        reply = QMessageBox.question(
            self, t("messages.confirm_action"), t("messages.confirm_delete"),
            QMessageBox.Yes | QMessageBox.No,
        )
        if reply == QMessageBox.Yes:
            book_id = int(self.table_books.item(row, 0).text())
            if BooksCRUD.delete(book_id):
                self.toast.show_toast(t("messages.data_deleted"))
                self._refresh_books_table()

    def _search_isbn(self):
        isbn = self.book_inputs["isbn"].text().strip()
        if not isbn:
            return
        data = set_isbn(isbn)
        if data:
            if data.get("subtitle"):
                self.book_inputs["titulo"].setText(f"{data['title']} - {data['subtitle']}")
            else:
                self.book_inputs["titulo"].setText(data.get("title", ""))
            authors = data.get("authors", [])
            self.book_inputs["autor"].setText(", ".join(authors) if isinstance(authors, list) else str(authors))
            self.book_inputs["editora"].setText(data.get("publisher", ""))
            self.book_subject.setText(data.get("synopsis", ""))
            self.book_inputs["n_folhas"].setText(str(data.get("page_count", "")))
            self.toast.show_toast("ISBN encontrado! Campos preenchidos.")

    # ---- Readers ----
    def _page_readers(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.setContentsMargins(20, 20, 20, 20)

        header = QHBoxLayout()
        title = QLabel(t("readers.title"))
        title.setObjectName("title")
        header.addWidget(title)
        header.addStretch()

        btn_export = QPushButton(f"📊 {t('readers.export_excel')}")
        btn_export.clicked.connect(lambda: self._export_excel("readers"))
        header.addWidget(btn_export)

        btn_import = QPushButton("📥 Importar Planilha")
        btn_import.setProperty("class", "premium")
        btn_import.clicked.connect(lambda: self._import_data("readers"))
        header.addWidget(btn_import)

        btn_template = QPushButton("📋 Template")
        btn_template.clicked.connect(lambda: self._export_template("readers"))
        header.addWidget(btn_template)

        btn_refresh = QPushButton("🔄 Atualizar")
        btn_refresh.clicked.connect(self._refresh_readers_table)
        header.addWidget(btn_refresh)
        layout.addLayout(header)

        tabs = QTabWidget()

        # Tab: List
        list_tab = QWidget()
        list_layout = QVBoxLayout(list_tab)
        self.table_readers = QTableWidget()
        self.table_readers.setAlternatingRowColors(True)
        self.table_readers.setSelectionBehavior(QTableWidget.SelectRows)
        list_layout.addWidget(self.table_readers)

        btn_row = QHBoxLayout()
        btn_update = QPushButton(t("readers.update"))
        btn_update.clicked.connect(self._update_reader)
        btn_row.addWidget(btn_update)
        btn_delete = QPushButton(f"🗑 {t('readers.delete')}")
        btn_delete.setProperty("class", "danger")
        btn_delete.clicked.connect(self._delete_reader)
        btn_row.addWidget(btn_delete)
        btn_row.addStretch()
        list_layout.addLayout(btn_row)
        tabs.addTab(list_tab, t("readers.list"))

        # Tab: Register
        reg_tab = QWidget()
        reg_layout = QVBoxLayout(reg_tab)
        form_grid = QGridLayout()
        form_grid.setSpacing(12)

        self.reader_inputs = {}
        fields = [
            ("nome", t("readers.name")), ("telefone", t("readers.phone")),
            ("email", t("readers.email")), ("cpf", t("readers.cpf")),
            ("identidade", t("readers.identity")), ("cep", t("readers.cep")),
            ("escolaridade", t("readers.schooling")), ("data_nascimento", t("readers.birth_date")),
            ("endereco", t("readers.address")), ("data_cadastro", t("readers.date")),
        ]
        for i, (key, label) in enumerate(fields):
            row, col = divmod(i, 2)
            lbl = QLabel(label)
            inp = QLineEdit()
            inp.setFixedHeight(36)
            if key == "telefone":
                inp.setInputMask("(99) 99999-9999")
            elif key == "cpf":
                inp.setInputMask("000.000.000-00")
            elif key == "cep":
                inp.setInputMask("00000-000")
            form_grid.addWidget(lbl, row * 2, col)
            form_grid.addWidget(inp, row * 2 + 1, col)
            self.reader_inputs[key] = inp

        reg_layout.addLayout(form_grid)
        btn_save = QPushButton(t("readers.save"))
        btn_save.setFixedWidth(200)
        btn_save.clicked.connect(self._save_reader)
        reg_layout.addWidget(btn_save)
        reg_layout.addStretch()
        tabs.addTab(reg_tab, t("readers.register"))

        layout.addWidget(tabs)
        return page

    def _save_reader(self):
        data = {k: inp.text().strip() for k, inp in self.reader_inputs.items()}
        ok, msg = validate_reader(data)
        if not ok:
            QMessageBox.warning(self, t("messages.warning"), msg)
            return
        result = ReadersCRUD.create(**data)
        if result:
            self.toast.show_toast(t("messages.data_saved"))
            self._refresh_readers_table()
            for inp in self.reader_inputs.values():
                inp.clear()
        else:
            QMessageBox.critical(self, t("messages.error"), "Erro ao salvar leitor.")

    def _refresh_readers_table(self):
        data = ReadersCRUD.read_all()
        headers = ["ID", "Nome", "Telefone", "Email", "CPF", "Identidade",
                    "CEP", "Escolaridade", "Nasc.", "Endereço", "Cadastro"]
        self.table_readers.setColumnCount(len(headers))
        self.table_readers.setHorizontalHeaderLabels(headers)
        self.table_readers.setRowCount(len(data))
        for row, reader in enumerate(data):
            for col, key in enumerate(["id", "nome", "telefone", "email", "cpf",
                                        "identidade", "cep", "escolaridade",
                                        "data_nascimento", "endereco", "data_cadastro"]):
                item = QTableWidgetItem(str(reader.get(key, "")))
                self.table_readers.setItem(row, col, item)
        self.table_readers.resizeColumnsToContents()

    def _update_reader(self):
        row = self.table_readers.currentRow()
        if row < 0:
            QMessageBox.warning(self, t("messages.warning"), "Selecione um leitor.")
            return
        reader_id = int(self.table_readers.item(row, 0).text())
        data = {k: inp.text().strip() for k, inp in self.reader_inputs.items()}
        if ReadersCRUD.update(reader_id, **data):
            self.toast.show_toast(t("messages.data_updated"))
            self._refresh_readers_table()

    def _delete_reader(self):
        row = self.table_readers.currentRow()
        if row < 0:
            return
        reply = QMessageBox.question(
            self, t("messages.confirm_action"), t("messages.confirm_delete"),
            QMessageBox.Yes | QMessageBox.No,
        )
        if reply == QMessageBox.Yes:
            reader_id = int(self.table_readers.item(row, 0).text())
            if ReadersCRUD.delete(reader_id):
                self.toast.show_toast(t("messages.data_deleted"))
                self._refresh_readers_table()

    # ---- Loans ----
    def _page_loans(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.setContentsMargins(20, 20, 20, 20)

        header = QHBoxLayout()
        title = QLabel(t("loans.title"))
        title.setObjectName("title")
        header.addWidget(title)
        header.addStretch()

        btn_refresh = QPushButton("🔄 Atualizar")
        btn_refresh.clicked.connect(self._refresh_loans_table)
        header.addWidget(btn_refresh)
        layout.addLayout(header)

        self.table_loans = QTableWidget()
        self.table_loans.setAlternatingRowColors(True)
        self.table_loans.setSelectionBehavior(QTableWidget.SelectRows)
        layout.addWidget(self.table_loans)

        btn_row = QHBoxLayout()
        btn_new = QPushButton(f"➕ {t('loans.register')}")
        btn_new.clicked.connect(self._new_loan)
        btn_row.addWidget(btn_new)

        btn_return = QPushButton(f"📥 {t('loans.return_book')}")
        btn_return.clicked.connect(self._return_loan)
        btn_row.addWidget(btn_return)

        btn_row.addStretch()
        layout.addLayout(btn_row)
        return page

    def _new_loan(self):
        if not session.is_premium:
            self._promo_toast.show_feature_gate("Empréstimos de Livros")
            return

        books = BooksCRUD.read_all()
        readers = ReadersCRUD.read_all()
        if not books or not readers:
            QMessageBox.warning(self, t("messages.warning"), "Cadastre livros e leitores primeiro.")
            return

        book_items = [f"{b['n_tombo']} - {b['titulo']}" for b in books]
        reader_items = [f"{r['cpf']} - {r['nome']}" for r in readers]

        book_idx, ok1 = QInputDialog.getItem(self, t("loans.register"), t("loans.book"), book_items, 0, False)
        if not ok1:
            return
        reader_idx, ok2 = QInputDialog.getItem(self, t("loans.register"), t("loans.reader"), reader_items, 0, False)
        if not ok2:
            return

        book_id = books[book_idx]["id"]
        reader_id = readers[reader_idx]["id"]

        result = LoansCRUD.create(book_id, reader_id)
        if result:
            self.toast.show_toast(t("messages.data_saved"))
            self._refresh_loans_table()
        else:
            QMessageBox.critical(self, t("messages.error"), "Erro ao criar empréstimo. Livro pode já estar emprestado.")

    def _return_loan(self):
        if not session.is_premium:
            self._promo_toast.show_feature_gate("Devolução de Livros")
            return

        row = self.table_loans.currentRow()
        if row < 0:
            QMessageBox.warning(self, t("messages.warning"), "Selecione um empréstimo.")
            return
        loan_id = int(self.table_loans.item(row, 0).text())
        ok, fine = LoansCRUD.return_book(loan_id)
        if ok:
            msg = t("messages.data_saved")
            if fine > 0:
                msg += f"\n\nMulta: R$ {fine:.2f}"
            self.toast.show_toast(msg)
            self._refresh_loans_table()

    def _refresh_loans_table(self):
        data = LoansCRUD.read_all()
        headers = ["ID", "Livro", "Leitor", "Saída", "Prevista", "Devolução", "Status", "Multa"]
        self.table_loans.setColumnCount(len(headers))
        self.table_loans.setHorizontalHeaderLabels(headers)
        self.table_loans.setRowCount(len(data))
        for row, loan in enumerate(data):
            for col, key in enumerate(["id", "livro", "leitor", "data_emprestimo",
                                        "data_devolucao_prevista", "data_devolucao_real",
                                        "status", "multa"]):
                val = loan.get(key, "")
                if key == "multa":
                    val = f"R$ {val:.2f}" if val else "R$ 0.00"
                item = QTableWidgetItem(str(val))
                self.table_loans.setItem(row, col, item)
        self.table_loans.resizeColumnsToContents()

    # ---- Collaborators ----
    def _page_collaborators(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.setContentsMargins(20, 20, 20, 20)

        header = QHBoxLayout()
        title = QLabel(t("collaborators.title"))
        title.setObjectName("title")
        header.addWidget(title)
        header.addStretch()

        btn_refresh = QPushButton("🔄 Atualizar")
        btn_refresh.clicked.connect(self._refresh_collabs_table)
        header.addWidget(btn_refresh)
        layout.addLayout(header)

        self.table_collabs = QTableWidget()
        self.table_collabs.setAlternatingRowColors(True)
        self.table_collabs.setSelectionBehavior(QTableWidget.SelectRows)
        layout.addWidget(self.table_collabs)

        btn_row = QHBoxLayout()
        btn_delete = QPushButton(f"🗑 {t('collaborators.delete')}")
        btn_delete.setProperty("class", "danger")
        btn_delete.clicked.connect(self._delete_collab)
        btn_row.addWidget(btn_delete)
        btn_row.addStretch()
        layout.addLayout(btn_row)
        return page

    def _refresh_collabs_table(self):
        data = CollaboratorsCRUD.read_all(safe=True)
        headers = ["ID", "Nome", "Usuário", "Senha", "Função"]
        self.table_collabs.setColumnCount(len(headers))
        self.table_collabs.setHorizontalHeaderLabels(headers)
        self.table_collabs.setRowCount(len(data))
        for row, collab in enumerate(data):
            for col, key in enumerate(["id", "nome", "nome_usuario", "senha", "role"]):
                item = QTableWidgetItem(str(collab.get(key, "")))
                self.table_collabs.setItem(row, col, item)
        self.table_collabs.resizeColumnsToContents()

    def _delete_collab(self):
        row = self.table_collabs.currentRow()
        if row < 0:
            return
        reply = QMessageBox.question(
            self, t("messages.confirm_action"), t("messages.confirm_delete"),
            QMessageBox.Yes | QMessageBox.No,
        )
        if reply == QMessageBox.Yes:
            collab_id = int(self.table_collabs.item(row, 0).text())
            if CollaboratorsCRUD.delete(collab_id):
                self.toast.show_toast(t("messages.data_deleted"))
                self._refresh_collabs_table()

    # ---- Reports ----
    def _page_reports(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.setContentsMargins(20, 20, 20, 20)

        title = QLabel(t("reports.title"))
        title.setObjectName("title")
        layout.addWidget(title)

        if not session.is_premium:
            lbl = QLabel(t("reports.premium_required"))
            lbl.setStyleSheet("font-size: 16px; color: #FFD700; margin-top: 40px;")
            lbl.setAlignment(Qt.AlignCenter)
            layout.addWidget(lbl)

            btn_activate = QPushButton("🔑 Ativar Premium")
            btn_activate.setFixedWidth(250)
            btn_activate.setStyleSheet("""
                QPushButton {
                    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                        stop:0 #FFD700, stop:1 #FFA500);
                    color: #1a1a2e;
                }
            """)
            btn_activate.clicked.connect(self._activate_license)
            layout.addWidget(btn_activate, alignment=Qt.AlignCenter)
            layout.addStretch()
            return page

        btn_row = QHBoxLayout()
        for text, func in [
            (t("reports.books_report"), "books"),
            (t("reports.readers_report"), "readers"),
            (t("reports.loans_report"), "loans"),
        ]:
            btn = QPushButton(f"📄 {text}")
            btn.setFixedHeight(80)
            btn.clicked.connect(lambda checked, f=func: self._generate_report(f))
            btn_row.addWidget(btn)
        layout.addLayout(btn_row)
        layout.addStretch()
        return page

    def _generate_report(self, report_type):
        filepath, _ = QFileDialog.getSaveFileName(
            self, t("reports.save_pdf"), "", "PDF (*.pdf)"
        )
        if not filepath:
            return
        funcs = {
            "books": generate_books_report,
            "readers": generate_readers_report,
            "loans": generate_loans_report,
        }
        if funcs[report_type](filepath):
            self.toast.show_toast(f"Relatório salvo: {filepath}")
        else:
            QMessageBox.critical(self, t("messages.error"), "Erro ao gerar relatório.")

    # ---- About ----
    def _page_about(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.setContentsMargins(40, 40, 40, 40)
        layout.setAlignment(Qt.AlignCenter)

        logo = QLabel("📚")
        logo.setAlignment(Qt.AlignCenter)
        logo.setStyleSheet("font-size: 72px; background: transparent;")
        layout.addWidget(logo)

        name = QLabel("LIBRYNO")
        name.setAlignment(Qt.AlignCenter)
        name.setStyleSheet("font-size: 36px; font-weight: bold; color: #5CE1E6; background: transparent;")
        layout.addWidget(name)

        info_lines = [
            f"{t('about.version')}: {Config.APP_VERSION}",
            f"{t('about.developer')}: {APP_AUTHOR}",
            f"{t('about.library')}: {APP_ORG}",
            f"{t('about.license')}: Apache License 2.0",
        ]
        if APP_CNPJ:
            info_lines.insert(3, f"{t('about.cnpj')}: {APP_CNPJ}")
        for line in info_lines:
            lbl = QLabel(line)
            lbl.setAlignment(Qt.AlignCenter)
            lbl.setStyleSheet("font-size: 14px; color: #a0a0a0; background: transparent;")
            layout.addWidget(lbl)

        layout.addSpacing(20)

        if session.is_authenticated:
            user_lbl = QLabel(f"Logado como: {session.user_name} ({session.user_email})")
            user_lbl.setAlignment(Qt.AlignCenter)
            user_lbl.setStyleSheet("color: #5CE1E6; background: transparent;")
            layout.addWidget(user_lbl)

        layout.addStretch()
        return page

    # ---- Navigation ----
    def _navigate(self, index):
        self.current_nav = index
        self.stack.setCurrentIndex(index)
        for i, btn in enumerate(self.nav_buttons):
            btn.setChecked(i == index)

        if index == 0:
            self._update_dashboard_charts()
        elif index == 1:
            self._refresh_books_table()
        elif index == 2:
            self._refresh_readers_table()
        elif index == 3:
            self._refresh_loans_table()
        elif index == 4:
            self._refresh_collabs_table()

    # ---- Actions ----
    def _connect_signals(self):
        pass

    # ---- Premium Promo System ----

    def _check_promos(self):
        """Verifica se deve mostrar promoção."""
        if session.is_premium:
            self._promo_timer.stop()
            return

        if promo_manager.should_show_initial_promo():
            self._promo_toast.show_welcome_tip()
        elif promo_manager.should_show_usage_promo():
            usage = promo_manager.get_usage_percentage()
            for entity, pct in usage.items():
                if pct >= 80:
                    limit_map = {
                        "livros": FREE_MAX_BOOKS,
                        "leitores": FREE_MAX_READERS,
                        "colaboradores": FREE_MAX_COLLABS,
                    }
                    count_map = {
                        "livros": lambda: BooksCRUD.count(),
                        "leitores": lambda: ReadersCRUD.count(),
                        "colaboradores": lambda: CollaboratorsCRUD.count(),
                    }
                    self._promo_toast.show_limit_reached(
                        entity,
                        count_map[entity](),
                        limit_map[entity],
                    )
                    break

    def _do_search(self):
        term = self.input_search.text().strip()
        if not term:
            return
        books = BooksCRUD.search(term)
        if books:
            self._navigate(1)
            self.toast.show_toast(f"Encontrado(s) {len(books)} livro(s)")
            return
        readers = ReadersCRUD.search(term)
        if readers:
            self._navigate(2)
            self.toast.show_toast(f"Encontrado(s) {len(readers)} leitor(es)")
            return
        self.toast.show_toast("Nenhum resultado encontrado.")

    def _export_excel(self, table_type):
        filepath, _ = QFileDialog.getSaveFileName(
            self, "Salvar Excel", "", "Excel (*.xlsx)"
        )
        if not filepath:
            return
        if table_type == "books":
            ok = export_books_to_excel(filepath)
        else:
            ok = export_readers_to_excel(filepath)
        if ok:
            self.toast.show_toast(f"Exportado: {filepath}")
        else:
            QMessageBox.warning(self, t("messages.warning"), "Nenhum dado para exportar.")

    def _import_data(self, entity_type):
        if not session.is_premium:
            # Mostrar opção de import por cola (FREE com limite)
            reply = QMessageBox.question(
                self,
                t("home.premium"),
                "📥 Importação de arquivo Excel/CSV é Premium.\n\n"
                "Mas você pode importar copiando e colando dados!\n"
                "(Plano FREE: até 20 linhas)\n\n"
                "Deseja usar a importação por cola?",
                QMessageBox.Yes | QMessageBox.No,
            )
            if reply == QMessageBox.Yes:
                self._import_paste(entity_type)
            else:
                self._promo_toast.show_feature_gate("Importação de Planilhas")
            return

        filepath, _ = QFileDialog.getOpenFileName(
            self,
            f"Importar {t(entity_type + '.title') if entity_type == 'books' else t(entity_type + '.title')}",
            "",
            "Planilhas (*.xlsx *.xls *.csv);;Todos os arquivos (*)"
        )
        if not filepath:
            return

        reply = QMessageBox.question(
            self,
            "Confirmar Importação",
            f"Importar dados de:\n{filepath}\n\nDeseja continuar?",
            QMessageBox.Yes | QMessageBox.No,
        )
        if reply != QMessageBox.Yes:
            return

        if entity_type == "books":
            result = import_books(filepath)
        else:
            result = import_readers(filepath)

        if result.success:
            self.toast.show_toast(
                f"Importados: {result.imported} registros"
            )
            QMessageBox.information(
                self,
                "Importação Concluída",
                f"✅ Importados: {result.imported}\n"
                f"⏭ Ignorados: {result.skipped}\n"
                f"📊 Total: {result.total}"
            )
            if entity_type == "books":
                self._refresh_books_table()
            else:
                self._refresh_readers_table()
        else:
            QMessageBox.warning(
                self,
                "Importação",
                f"Importados: {result.imported}\n"
                f"Ignorados: {result.skipped}\n"
                f"Erros: {len(result.errors)}\n\n"
                + "\n".join(result.errors[:5])
            )

    def _import_paste(self, entity_type):
        """Abre tela de importação por cola."""
        self._import_screen = ImportPasteScreen(
            entity_type=entity_type,
            on_complete=lambda: self._on_import_complete(entity_type),
        )
        self._import_screen.setWindowTitle(f"Importar {entity_type}")
        self._import_screen.resize(700, 500)
        self._import_screen.show()

    def _on_import_complete(self, entity_type):
        """Callback após importação bem-sucedida."""
        if entity_type == "books":
            self._refresh_books_table()
        else:
            self._refresh_readers_table()
        # Mostrar teaser Premium após importação
        if not session.is_premium:
            QTimer.singleShot(2000, self._promo_toast.show_import_teaser)

    def _export_template(self, entity_type):
        filepath, _ = QFileDialog.getSaveFileName(
            self,
            f"Salvar Template {entity_type}",
            f"template_{entity_type}.xlsx",
            "Excel (*.xlsx)"
        )
        if not filepath:
            return
        if export_template(entity_type, filepath):
            self.toast.show_toast(f"Template salvo: {filepath}")
            QMessageBox.information(
                self,
                "Template Exportado",
                f"Template salvo em:\n{filepath}\n\n"
                "Preencha os dados e importe novamente."
            )
        else:
            QMessageBox.critical(self, t("messages.error"), "Erro ao exportar template.")

    def _show_notifications(self):
        if not session.is_premium:
            self._promo_toast.show_feature_gate("Notificações")
            return
        notifs = NotificationsCRUD.read_all()
        if not notifs:
            self.toast.show_toast(t("notifications.no_notifications"))
            return
        msg = "\n\n".join(
            f"• [{n['tipo']}] {n['titulo']}: {n['mensagem'][:60]}"
            for n in notifs[:10]
        )
        QMessageBox.information(self, t("notifications.title"), msg)

    def _toggle_theme(self):
        from PySide6.QtWidgets import QApplication
        app = QApplication.instance()
        if app:
            cycle_theme(app)

    def _update_premium_badge(self):
        self.badge.set_premium(session.is_premium)

    def _activate_license(self):
        key, ok = QInputDialog.getText(
            self, "Chave de Licença",
            "Insira sua chave OrdoB Premium:",
            QLineEdit.Normal,
        )
        if ok and key.strip():
            valid, msg = validate_license(key.strip())
            if valid:
                self.toast.show_toast(msg)
                self._update_premium_badge()
                self._navigate(0)
            else:
                QMessageBox.warning(self, t("messages.error"), msg)

    def _do_logout(self):
        reply = QMessageBox.question(
            self, t("home.logout"), "Deseja sair da conta?",
            QMessageBox.Yes | QMessageBox.No,
        )
        if reply == QMessageBox.Yes:
            session.logout()
            self.close()
            from src.ui.screens.login import LoginScreen
            self.login_window = LoginScreen(on_success=self._reopen_home)
            self.login_window.show()

    def _reopen_home(self):
        new_home = HomeScreen(login_screen=self.login_screen)
        new_home.show()
        self.deleteLater()

    def closeEvent(self, event):
        if self.login_screen:
            self.login_screen.close()
        event.accept()

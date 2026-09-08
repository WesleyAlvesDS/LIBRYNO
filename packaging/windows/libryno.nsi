; Libryno NSIS Installer Script
; Gera: Libryno-Setup.exe
; Compilar com: makensis libryno.nsi

!include "LogicLib.nsh"
!include "x64.nsh"
!include "FileFunc.nsh"
!include "MUI2.nsh"

; =============================================================================
# Configurações Básicas
; =============================================================================
!define APP_NAME "Libryno"
!define APP_VERSION "2.0.0"
!define APP_PUBLISHER "OrdoB"
!define APP_URL "https://ordob.com/libryno"
!define APP_EXE "Libryno.exe"

; Nome do instalador gerado
OutFile "..\..\dist\Libryno-Setup.exe"
InstallDir "$LOCALAPPDATA\Programs\Libryno"
InstallDirRegKey HKCU "Software\Libryno" "Install_Dir"

; Instalação por usuário (sem necessidade de admin)
RequestExecutionLevel user

; =============================================================================
# Interface
; =============================================================================
!define MUI_ICON "..\..\img\icon.ico"
!define MUI_UNICON "..\..\img\icon.ico"
!define MUI_WELCOMEFINISHPAGE_BITMAP "banner.bmp"
!define MUI_HEADERIMAGE
!define MUI_HEADERIMAGE_BITMAP "header.bmp"
!define MUI_HEADERIMAGE_UNBITMAP "header.bmp"

; Welcome page
!insertmacro MUI_PAGE_WELCOME
; License page
!insertmacro MUI_PAGE_LICENSE "LICENSE.txt"
; Directory page
!insertmacro MUI_PAGE_DIRECTORY
; Install page
!insertmacro MUI_PAGE_INSTFILES
; Finish page
!define MUI_FINISHPAGE_RUN "$INSTDIR\${APP_EXE}"
!define MUI_FINISHPAGE_RUN_NOTCHECKED
!insertmacro MUI_PAGE_FINISH

; Uninstall pages
!insertmacro MUI_UNPAGE_WELCOME
!insertmacro MUI_UNPAGE_CONFIRM
!insertmacro MUI_UNPAGE_INSTFILES
!insertmacro MUI_UNPAGE_FINISH

!insertmacro MUI_LANGUAGE "PortugueseBR"

; =============================================================================
# Variáveis
; =============================================================================
Var PreviousVersion

; =============================================================================
# Funções
; =============================================================================
Function .onInit
    ; Em modo silencioso (/S, auto-update) não pergunta nada
    ${IfNot} ${Silent}
        ; Verifica se já existe versão instalada
        ReadRegStr $PreviousVersion HKCU "Software\Libryno" "Version"
        ${If} $PreviousVersion != ""
            MessageBox MB_YESNO|MB_ICONQUESTION \
                "Já existe uma versão do Libryno instalada (v$PreviousVersion).$\n$\n\
                Deseja atualizar para a versão ${APP_VERSION}?$\n$\n\
                (Seus dados locais serão preservados)" \
                IDYES +2
            Abort
        ${EndIf}
    ${EndIf}
FunctionEnd

Function .onInstSuccess
    ; Registra versão instalada
    WriteRegStr HKCU "Software\Libryno" "Version" "${APP_VERSION}"
    WriteRegStr HKCU "Software\Libryno" "Install_Dir" "$INSTDIR"

    ; Adiciona ao Painel de Controle (Add/Remove Programs)
    WriteRegStr HKCU "Software\Microsoft\Windows\CurrentVersion\Uninstall\Libryno" \
        "DisplayName" "Libryno"
    WriteRegStr HKCU "Software\Microsoft\Windows\CurrentVersion\Uninstall\Libryno" \
        "DisplayVersion" "${APP_VERSION}"
    WriteRegStr HKCU "Software\Microsoft\Windows\CurrentVersion\Uninstall\Libryno" \
        "Publisher" "${APP_PUBLISHER}"
    WriteRegStr HKCU "Software\Microsoft\Windows\CurrentVersion\Uninstall\Libryno" \
        "URLInfoAbout" "${APP_URL}"
    WriteRegStr HKCU "Software\Microsoft\Windows\CurrentVersion\Uninstall\Libryno" \
        "InstallLocation" "$INSTDIR"
    WriteRegStr HKCU "Software\Microsoft\Windows\CurrentVersion\Uninstall\Libryno" \
        "UninstallString" "$INSTDIR\uninstall.exe"
    WriteRegStr HKCU "Software\Microsoft\Windows\CurrentVersion\Uninstall\Libryno" \
        "DisplayIcon" "$INSTDIR\${APP_EXE}"
    WriteRegDWORD HKCU "Software\Microsoft\Windows\CurrentVersion\Uninstall\Libryno" \
        "NoModify" 1
    WriteRegDWORD HKCU "Software\Microsoft\Windows\CurrentVersion\Uninstall\Libryno" \
        "NoRepair" 1
FunctionEnd

Function un.onInit
    MessageBox MB_ICONQUESTION|MB_YESNO \
        "Tem certeza que deseja desinstalar o Libryno?$\n$\n\
        Seus dados locais (livros, leitores, empréstimos) NÃO serão removidos. $\n$\n\
        Apenas o programa será desinstalado." \
        IDYES +2
    Abort
FunctionEnd

Function un.onUninstSuccess
    ; Remove entradas do registro
    DeleteRegKey HKCU "Software\Microsoft\Windows\CurrentVersion\Uninstall\Libryno"
    DeleteRegKey HKCU "Software\Libryno"

    ; Remove atalhos
    Delete "$SMPROGRAMS\Libryno\Libryno.lnk"
    Delete "$SMPROGRAMS\Libryno\Desinstalar Libryno.lnk"
    Delete "$DESKTOP\Libryno.lnk"

    ; Remove pasta do menu iniciar se vazia
    RMDir "$SMPROGRAMS\Libryno"
FunctionEnd

; =============================================================================
# Seção Principal
; =============================================================================
Section "Main" SEC_MAIN
    SetOutPath $INSTDIR

    ; Binário principal (PyInstaller onefile)
    File /oname=${APP_EXE} "..\..\dist\libryno.exe"

    ; Cria desinstalador
    WriteUninstaller "$INSTDIR\uninstall.exe"

    ; Atalhos
    CreateDirectory "$SMPROGRAMS\Libryno"
    CreateShortcut "$SMPROGRAMS\Libryno\Libryno.lnk" "$INSTDIR\${APP_EXE}" "" "$INSTDIR\${APP_EXE}"
    CreateShortcut "$SMPROGRAMS\Libryno\Desinstalar Libryno.lnk" "$INSTDIR\uninstall.exe"
    CreateShortcut "$DESKTOP\Libryno.lnk" "$INSTDIR\${APP_EXE}" "" "$INSTDIR\${APP_EXE}"
SectionEnd

; =============================================================================
# Desinstalador
; =============================================================================
Section "Uninstall"
    ; Remove arquivos
    Delete "$INSTDIR\${APP_EXE}"
    Delete "$INSTDIR\uninstall.exe"

    ; Remove atalhos
    Delete "$SMPROGRAMS\Libryno\Libryno.lnk"
    Delete "$SMPROGRAMS\Libryno\Desinstalar Libryno.lnk"
    Delete "$DESKTOP\Libryno.lnk"
    RMDir "$SMPROGRAMS\Libryno"

    ; Remove auto-start
    DeleteRegKey HKCU "Software\Microsoft\Windows\CurrentVersion\Run" "Libryno"

    ; Remove registro
    DeleteRegKey HKCU "Software\Libryno"
    DeleteRegKey HKCU "Software\Microsoft\Windows\CurrentVersion\Uninstall\Libryno"

    ; Tenta remover diretório de instalação
    RMDir $INSTDIR
SectionEnd

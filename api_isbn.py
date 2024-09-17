import requests
import json

def set_isbn(isbn):
    url = f"https://brasilapi.com.br/api/isbn/v1/{isbn}"
    
    try:
        response = requests.get(url)
        print(response)
        if response.status_code == 200:
            resp = json.loads(response.text)
            return (
                resp.get('title', 'Título não encontrado'),
                resp.get('subtitle','Subtítulo não encontrado'),
                resp.get('authors', 'Autor(es) não encontrado(s)'),
                resp.get('publisher', 'Editora não encontrada'),
                resp.get('synopsis', 'Sinopse não encontrada'),
                resp.get('page_count', 'Contagem de páginas não encontrada')
            )
        else:
            return f"Erro na API: {response.status_code}"

    except requests.exceptions.RequestException as e:
        return f"Erro na requisição: {e}"

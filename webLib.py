import locale
import requests
import os

from bs4 import BeautifulSoup

# pd.set_option('display.max_rows', 100)

# Configura o locale para o formato de número brasileiro
locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')

def textFromURL(url):
    try:
        # Fazer a solicitação HTTP para a URL
        response = requests.get(url)

        # Verificar se a solicitação foi bem-sucedida
        response.raise_for_status()  

        # Criar um objeto BeautifulSoup para analisar o conteúdo HTML
        soup = BeautifulSoup(response.content, 'html.parser', from_encoding="utf-8")

        # Extrair o texto visível da página (excluindo o HTML)
        texto_visivel = soup.get_text()

        # separa as linhas, e limpa os espaços iniciais, e tabulações
        linhas = [linha.replace("\t"," ").strip() for linha in texto_visivel.split("\n")]

        # junta o texto
        return "\n".join(linhas)
    except requests.exceptions.RequestException as e:
        print(f"Erro ao obter a página: {e}")
        return None
    
def textFromURLorFile(url, fileTXT):
    if os.path.exists(fileTXT):
        with open(fileTXT, "r", encoding="utf-8") as file:
            texto = file.readlines()
            file.close()
        texto = "".join(texto)
    else:
        texto = textFromURL(url)
        with open(fileTXT, "w+", encoding="utf-8") as file:
            file.write(texto)
            file.close()

    return texto

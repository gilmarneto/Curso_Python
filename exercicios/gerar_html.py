# data: 03/06/2022

# Neste exercício vamos criar um arquivo (.html)

# Declarando variável
caminho = "arquivos/"

# Função responsável por gerar arquivo (.html)
def arquivo_html(nome_arquivo) :
    arquivo = open(f"{caminho}{nome_arquivo}", "w")
    arquivo.write('''<!doctype html>\n
        <html>\n
            <head>\n
                <title>Arquivo HTML feito em Python</title>\n
            </head>\n
            <body>\n
                <h1>Olá, HTML!!!</html>\n
            </body>\n
        </html>''')
    # aqui vamos fechar o arquivo
    arquivo.close

# vamos chamar a função 
arquivo_html("index.html")
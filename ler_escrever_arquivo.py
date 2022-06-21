# data: 03/06/2022

# declarar variável
caminho_do_arquivo = "arquivos/"

# ler e escrever arquivo 

# função para leitura de arquivo (.txt)
def ler_arquivo_txt(nome_arquivo_txt) :
    # leitura-read(r)
    arquivo = open(f"{caminho_do_arquivo}{nome_arquivo_txt}", 'r') # o arquivo (txt) deve estar no mesmo diretório do arquivo Python
    for linha in arquivo :
        # vamos passar pelos valores do arquivo (txt)
        print(linha)
        # O Python usa o espaço como delimitador
    # abaixo vamos fechar o arquivo    
    arquivo.close

ler_arquivo_txt("pessoas.txt") # chamar função (ler_arquivo_txt), passando como parâmetro o nome do arquivo

# função para leitura de arquivo (.csv)
def ler_arquivo_csv(nome_arquivo_csv) :
    arquivo = open(f"{caminho_do_arquivo}{nome_arquivo_csv}", "r")
    for linha in arquivo :
        print(linha)
    # abaixo vamos fechar o arquivo    
    arquivo.close

ler_arquivo_csv("pedidos.csv")

# função para escrita de arquivo (.txt)
def escrever_txt(arquivo_txt) :
    arquivo = open(f"{caminho_do_arquivo}{arquivo_txt}","w")
    arquivo.write("Olá Mundo!!!")

escrever_txt("primeiro_arquivo.txt")
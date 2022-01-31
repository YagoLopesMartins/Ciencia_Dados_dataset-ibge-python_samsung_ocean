
'''
 2. Qual o valor médio do Produto Interno Bruto da cidade de Manaus no periodo que abrange o dataset?
 (O Produto Interno Bruto consiste na soma dos valores da Agropecuária, 
 Indústria, Serviços, Administracao e Impostos)
'''

# funcao que recebe o nome da cidade como parametro
def valor_medio_pib_cidade (cidade):
    #leitura do dataset, r=read (encoding)
    arquivo = open('../dataset/pib_municipio_2010_a_2018.txt', 'r')
    
    lista = arquivo.readlines() #ler o arquivo como um todo
    #variaveis
    pib_per_capita_cidade = 0.0
    media = 0.0

# estrutura de repeticao que vai ler linha por linha do arquivo
    for linha in lista:
        # ao final de cada linha possui o caractere especial \n, quando inserido em um array este é inserido
        # também, por isso importante removê-lo com a funcao strip
        linha_auxiliar = linha.strip('\n')
        # cada linha do arquivo é separado por ";", por isso funcao split "quebra" separa por bloco o que tem 
        # entre a pontuacao
        linha_do_arquivo = linha_auxiliar.split(';')
         
            # Cada linha segue o padrão de exemplo abaixo, portanto apos ser quabrada/separada, cada parte
            # é representada por um numero, como temos 10 partes de informacoes, no python um array começa com ZERO,
            #  no caso, vamos do 0 ao 9
            # Ex.: 2010;RO;Rond�nia;Alta Floresta D'Oeste;69260;16119;62496;93245;20957;10731.18
            # 0; 1; 2; 3; 4; 5; 6; 7; 8; 9;

        # SE posicao 3 do array (cidade) for igual a cidade enviada (Manaus)
        if(linha_do_arquivo[3] == cidade):
            # como estamos utilizando lista, é preciso converter a informacao que é STRING para real/FLOAT
            valor_per_capita_auxiliar = float(linha_do_arquivo[9])
            # tendo convertido STRING (caracteres) para FLOAT (real) pode-se agora 
            # podemos somar os valores toda vez que identificar a cidade enviada
            # nao era necessario criar dessa forma, porem fica generico, o que facilita posteriormente
            # querer a media de outra cidade por exemplo
            pib_per_capita_cidade = pib_per_capita_cidade + valor_per_capita_auxiliar

    # tendo somado todos os pib da cidade, agora dividir por 9 que é a quantidade do intervalo (2010 a 2018)
    media = pib_per_capita_cidade / 9
               
    arquivo.close()# fecha arquivo
    return round(media,2) # retorna a media com arrendodamento para duas casas decimais padrão: valor.xx, onde os x's é a quantidade do arrendodamento

# abrir arquivo e escreve no mesmo, encoding w=write/escrita
arquivo_saida = open("saida_q2.txt", "w")
cidade = 'Manaus' # se quiser outras medias de outras cidades, basta trocar pelo nome das mesmas e tudo funcionará normalmente

#chama a funcao passando o nome da cidade e guarda na variavel media
media = valor_medio_pib_cidade(cidade)
print(media) # mostra na tela a media
#escreve no arquivo a mensagem com conversao agora de FLOAT para STRING
arquivo_saida.write(str(media) + ' do PIB da cidade de Manaus em todo o dataset (2010 - 2018)')

arquivo_saida.close()#fecha o arquivo
    
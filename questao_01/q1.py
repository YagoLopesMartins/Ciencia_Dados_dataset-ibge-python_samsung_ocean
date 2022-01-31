'''
 1. Qual a cidade de cada estado que possui o maior PIB per capita, no ano de 2018?
 SAIDA: informar: CIDADE, ESTADO e PIB
'''
# funcao criada para nao ficar repetindo varias vezes o codigo, deixando mais organizado e estruturado
def funcao_maior_pib_per_capita_por_estado_2018 (sigla_estado):
    # abertura do arquivo txt dataset, segundo parametro (encoding) siginifica r=read
    arquivo_dataset = open('../dataset/pib_municipio_2010_a_2018.txt', 'r')

    #variaveis utilizadas
    lista = arquivo_dataset.readlines() #ler o arquivo como um todo
    cidade_com_maior_pib_per_capita_por_estado = 0.0 #variavel do tipo float (tipos reais)
    linha_final = [] # array
    final = [] # array

    # estrutura de repeticao que vai ler linha por linha do arquivo
    for linha in lista:

        # ao final de cada linha possui o caractere especial \n, quando inserido em um array este é inserido
        # também, por isso importante removê-lo com a funcao strip
        linha_auxiliar = linha.strip('\n')
        # cada linha do arquivo é separado por ";", por isso funcao split "quebra" separa por bloco o que tem 
        # entre a pontuacao
        linha_do_arquivo = linha_auxiliar.split(';')
        '''
        Cada linha segue o padrão de exemplo abaixo, portanto apos ser quabrada/separada, cada parte
        é representada por um numero, como temos 10 partes de informacoes, no python um array começa com ZERO,
        no caso, vamos do 0 ao 9
         Ex.: 2010;RO;Rond�nia;Alta Floresta D'Oeste;69260;16119;62496;93245;20957;10731.18
         0; 1; 2; 3; 4; 5; 6; 7; 8; 9;
        '''
        # se sabemos que na posicao 0 contem a informacao de ano, precisamos filtrar pelo mesmo, ou seja 2018
        # e o filtro é feito pelo IF (SE) onde perguntamos se é igual a 2018
        if(linha_do_arquivo[0] == '2018'):
            # se for iagual 2018, entao precisamos filtrar por cada espaço de acordo com a pergunta do problema
            # 1 significa a SIGLA do estado
            if(linha_do_arquivo[1] == sigla_estado):
                # como estamos utilizando lista, é preciso converter a informacao que é STRING para real/FLOAT
                valor_per_capita_auxiliar = float(linha_do_arquivo[9])
                # tendo convertido STRING (caracteres) para FLOAT (real) pode-se agora comparar quem é o maior
                # tendo em vista que a variavel cidade_com_maior_pib_per_capita_por_estado ira
                #guardar o valor da comparacao
                if(valor_per_capita_auxiliar > cidade_com_maior_pib_per_capita_por_estado):
                    # sempre que for maior é preciso atualizar a variavel, nesse caso fazendo a troca
                    cidade_com_maior_pib_per_capita_por_estado = valor_per_capita_auxiliar

                    #nesse caso como é pedido como saida( 3 é igual a cidade; 2 é o estado e 9 é o PIB)
                    linha_final = 'Cidade: '+linha_do_arquivo[3] + ' - Estado: ' + linha_do_arquivo[2] + ' - PIB: ' + linha_do_arquivo[9]
                    
    arquivo_dataset.close() # fecha o arquivo 
    return linha_final # retorna a linha contendo a cidade de maior PIB no qual a sigla foi informada

'''
    PROGRAMA COMEÇA AQUI
'''
# definindo escrita em arquivo, segundo parametro (encoding) siginifica w= write
arquivo_saida = open("saida_q1.txt", "w")

# estrutura de dados criada para armazenar as siglas e assim facilitar quando lidas e enviadas para a funcao
# com isso foi economizado varios if's no qual inicialmente foi utilizado, porém modificado posteriormente
siglas_dos_estados = ['AM', 'PA', 'RO', 'AC', 'TO', 'RR', 'AP',
                    'MT','GO','MS','DF',
                    'MA','PI','CE','RN','PB','PE','AL','SE','BA',
                    'SP','MG','ES','RJ',
                    'PR','SC','RS'
                 ]

# se queremos a cidade de maior PIB por estado, entao teremos que enviar a sigla do estado para a funcao
# dessa forma, cada vez que uma silga é enviada (por exemplo AM), a funcao precisa devolver os dados da linha
# que contem a cidade de maior PIB por estado
for sigla_estado in siglas_dos_estados:
    # chama a funcao passando a SIGLA do estado da estrutura de dados e recebe na variavel(do tipo lista) o resultado
    resultado = funcao_maior_pib_per_capita_por_estado_2018(sigla_estado)
    
    print(resultado) # mostra no terminal
    arquivo_saida.write(resultado + "\n") # escreve no arquivo e dessa vez acrescenta o \n que significa QUEBRA DE LINHA

arquivo_saida.close() #fechamento do arquivo
    
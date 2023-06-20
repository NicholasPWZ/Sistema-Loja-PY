import Cliente, Item, Produto, Pedido, Vendedor, Service

def criar_produto():
    codigo_barras = input('Insira o código do produto')
    retorno = Service.consulta_produto(codigo_barras)
    if retorno == None:
        nome_produto = input('Insira o nome do produto')
        #Conferir se o nome ja está inserido no banco

        preco = input('Insira o preço do produto')
        #Conferir se são apenas números

        estoque = input('Informe a quantidade em estoque do produto')
        #Conferir se é um inteiro

        flag = input('C - Para adicionar cor ao produto\nP - Para pular')
        if flag == 'C':
            ...
        flag = input('T - Para adicionar tamanho ao produto\nP - Para pular')
        if flag == 'T':
            ...
    else:
        ...

    produto = Produto()
    #Adicionar produto ao banco de dados

def cadastrar_funcionario():
    cpf = input('Insira o CPF do funcionário: ')
    #Conferir se já está inserido na tabela de funcionários, Conferir se tem o tamanho de CPF e se
    #possui somente números

    nome = input('Insira o nome do funcionário: ')
    #Verificar se são somente letras

    salario = input('Insira o salário do funcionário: ')
    #Verificar se são somente números

    taxa = input('Insira a taxa de comissão por vende do funcionário: ')
    #Verificar se são somente números e se é abaixo ou igual a 15%

    comissão = 0
    #A cada venda do funcionário deve se adicionar o total de comissão do mes nessa variável

def cadastrar_cliente():
    cpf = input('Insira o CPF do cliente: ')
    #Verificar se são somente numeros, Confere se já está cadastrado, e se estiver 
    # traz as informações do cliente
    retorno = Service.consulta_cliente(cpf)
    if retorno == None:
    
        nome = input('Insira o nome do cliente: ')
        #Verificar se são somente letras

        nascimento = input('Insira a data de nascimento do cliente: ')
        #Verifica se está no modelo correto

        rua = input('Insira a rua: ')
        

        numero = input('Insira o número: ')
        #Verificar se são somente números

        complemento = ('Insira o complemento(se houver): ')
    else:
        nome, nascimento, rua, numero, complemento = retorno[1], retorno[2], retorno[3], retorno[4], retorno[5]
        print(f"Cliente já cadastrado! {nome} - {nascimento} - {rua} - {numero} - {complemento}")
    
def criar_pedido():
    cliente = input('Insira o CPF do cliente')
    #Puxa no banco as informações do cliente, se não houver, chama a função de cadastrar cliente

    vendedor = input('Informe o CPF do vendedor')
    #Consulta se é um cpf cadastrado no banco, se não for, é invalido. Funcionário deve ser cadastrado ANTES

    cod_prod = input('Insira o código do produto')
    #Validar se já está cadastrado 
    
    qtd_prod = input('Insira a quantidade desse produto')
    #Validar se são somente numeros inteiros e se o produto tem estoque disponível




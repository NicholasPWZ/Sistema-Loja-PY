from Classes import Cliente, Pedido, Produto, Vendedor, Item
import Service, validations
from faker import Faker
fake = Faker('pt_BR')

def criar_produto():
    codigo_barras = input('Insira o código do produto')
    retorno = Service.consulta_produto(codigo_barras)
    if retorno == None:
        nome_produto = input('Insira o nome do produto')
        #Conferir se o nome ja está inserido no banco

        preco = input('Insira o preço do produto')
        validations.valida_numero(preco)

        estoque = input('Informe a quantidade em estoque do produto')
        validations.valida_inteiro(estoque)

        flag = input('C - Para adicionar cor ao produto\nP - Para pular')
        if flag == 'C':
            ...
        flag = input('T - Para adicionar tamanho ao produto\nP - Para pular')
        if flag == 'T':
            ...
    else:
        ...

    
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
    validations.valida_cpf(cpf)
    retorno = Service.consulta_cliente(cpf)
    if retorno == None:
        cpf = validations.formata_cpf(cpf)

        nome = input('Insira o nome do cliente: ')
        validations.valida_nome(nome)

        nascimento = input('Insira a data de nascimento do cliente: ')
        validations.valida_data(nascimento)

        rua = input('Insira a rua: ')
        validations.valida_nome(rua)

        numero =input('Insira o número: ')
        validations.valida_inteiro(numero)

        complemento = input('Insira o complemento(se houver): ')

        cliente = Cliente(nome,cpf,nascimento,rua,numero,complemento)
        Service.cadastra_cliente(cliente)
    else:
        nome, nascimento, rua, numero, complemento = retorno[1], retorno[2], retorno[3], retorno[4], retorno[5]
        print(f"Cliente já cadastrado! {nome} - {nascimento} - {rua} - {numero} - {complemento}")
    
def criar_pedido():
    cliente = input('Insira o CPF do cliente')
    validations.valida_cpf(cliente)
    #Puxa no banco as informações do cliente, se não houver, chama a função de cadastrar cliente

    vendedor = input('Informe o CPF do vendedor')
    validations.valida_cpf(vendedor)
    #Consulta se é um cpf cadastrado no banco, se não for, é invalido. Funcionário deve ser cadastrado ANTES

    cod_prod = input('Insira o código do produto')
    #Validar se já está cadastrado 
    
    qtd_prod = input('Insira a quantidade desse produto')
    validations.valida_inteiro(qtd_prod)
    #Validar se o produto tem estoque disponível


while True:
    decisao = input('1 - Cadastrar Cliente\n9 - Sair do programa:')
    if decisao == '9':
        break
    elif decisao == '1':
        cadastrar_cliente()

  
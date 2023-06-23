from Classes import Cliente, Pedido, Produto, Vendedor, Item
import Service, validations
from faker import Faker
fake = Faker('pt_BR')

def criar_produto():
    codigo_barras = input('Insira o código do produto')
    retorno = Service.consulta_produto(codigo_barras)
    if retorno is None:
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
    if validations.valida_cpf(cpf) is False:
        print(f'CPF: {cpf} É INVÁLIDO')
        return False
    
    retorno = Service.consulta_funcionario(cpf)
    if retorno is None:
    
        nome = input('Insira o nome do funcionário: ')
        if validations.valida_nome(nome) is False:
            print(f'NOME: {nome} INVÁLIDO')
            return False
        
        salario = input('Insira o salário do funcionário: ')
        
        if validations.valida_numero(salario) is False:
            print(f'SALÁRIO: {salario} INVÁLIDO')
            return False
        
        taxa = input('Insira a taxa de comissão por venda do funcionário(em %): ')
        if validations.valida_numero(taxa) is False:
            print(f'TAXA: {taxa} INVÁLIDA')
            return False
        
        vendedor = Vendedor(cpf, nome, salario, taxa)
        Service.cadastra_funcionario(vendedor)
        print(f'Funcionário {vendedor.nome} com CPF: {vendedor.cpf} FOI CADASTRADO COM SUCESSO!')
    else:
        nome, taxa, salario = retorno[1], retorno[2], retorno[3]
        print(f"Funcionário já cadastrado! {nome} - {taxa} - {salario}")

def cadastrar_cliente():
    cpf = input('Insira o CPF do cliente: ')
    cpf = validations.formata_cpf(cpf)
    if validations.valida_cpf(cpf) is False:
        print(f'CPF : {cpf} INVÁLIDO')
        return
    
    retorno = Service.consulta_cliente(cpf)
    if retorno is None:
        

        nome = input('Insira o nome do cliente: ')
        if validations.valida_nome(nome) is False:
            print(f'NOME : {nome} INVÁLIDO')
            return
        
        nascimento = input('Insira a data de nascimento do cliente: ')
        if validations.valida_data(nascimento) is False:
            print(f'DATA DE NASCIMENTO : {nascimento} INVÁLIDO')
            return
        
        rua = input('Insira a rua: ')
        if validations.valida_nome(rua) is False:
            print(f'RUA : {rua} INVÁLIDO')
            return
        
        numero =input('Insira o número: ')
        if  validations.valida_inteiro(numero) is False:
            print(f'NÚMERO : {numero} INVÁLIDO')
            return
        
        complemento = input('Insira o complemento(se houver): ')

        cliente = Cliente(nome,cpf,nascimento,rua,numero,complemento)
        Service.cadastra_cliente(cliente)
        print(f'Cliente {cliente.nome} com CPF: {cliente.cpf} FOI CADASTRADO COM SUCESSO!')
    else:
        nome, nascimento, rua, numero, complemento = retorno[1], retorno[2], retorno[3], retorno[4], retorno[5]
        print(f"Cliente já cadastrado! {nome} - {nascimento} - {rua} - {numero} - {complemento}")
    
def criar_pedido():
    cliente = input('Insira o CPF do cliente -|>')
    cliente = validations.formata_cpf(cliente)
    if validations.valida_cpf(cliente) is False:
        print(f'CPF {cliente} É INVÁLIDO')
        return
    print(Service.consulta_cliente(cliente))
    #Puxa no banco as informações do cliente, se não houver, chama a função de cadastrar cliente

    vendedor = input('Informe o CPF do vendedor -|>')
    vendedor = validations.formata_cpf(vendedor)
    if validations.valida_cpf(vendedor) is False:
        print(f'CPF {vendedor} É INVÁLIDO')
        return
    print(Service.consulta_funcionario(vendedor))
    #Consulta se é um cpf cadastrado no banco, se não for, é invalido. Funcionário deve ser cadastrado ANTES

    cod_prod = input('Insira o código do produto -|>')
    #Validar se já está cadastrado 
    
    qtd_prod = input('Insira a quantidade desse produto -|>')
    validations.valida_inteiro(qtd_prod)
    #Validar se o produto tem estoque disponível


while True:
    decisao = input('1 - Cadastrar Cliente\n2 - Cadastrar Funcionário\n9 - Sair do programa\n-|>')
    if decisao == '9':
        break
    
    elif decisao == '1': 
        validacao = cadastrar_cliente()
        if validacao is False:
            print('ERRO NO CADASTRO')
    
    elif decisao == '2':
        validacao = cadastrar_funcionario()
        if validacao is False:
            print('ERRO NO CADASTRO')
    
    elif decisao == '3':
        validacao = criar_pedido()
        if validacao is False:
            print('ERRO NA CRIAÇÃO DO PEDIDO')
    elif decisao == '8':
        ...
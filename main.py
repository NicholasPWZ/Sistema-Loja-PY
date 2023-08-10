from Classes import Cliente, Pedido, Produto, Vendedor, Item
import repository, validations
from faker import Faker
fake = Faker('pt_BR')

def criar_produto():
    codigo_barras = input('Insira o código do produto: ')
    
    retorno = repository.consulta_produto(codigo_barras)
    
    if retorno is None:
        nome_produto = input('Insira o nome do produto: ')
        

        preco = input('Insira o preço do produto: ')
        if validations.valida_numero(preco) is False:
            print(f'Preço: {preco} inválido')
            return

        estoque = input('Informe a quantidade em estoque do produto: ')
        if validations.valida_inteiro(estoque) is False:
            print(f'Quantidade {estoque} em estoque inválida')
            return

        flag = input('C - Para adicionar cor ao produto\nP - Para pular: ').upper()
        if flag == 'C':
            cor = input('Informe a cor: ')
        else:
            cor = None

        flag = input('T - Para adicionar tamanho ao produto\nP - Para pular: ').upper()
        if flag == 'T':
            tamanho = input('Informe o tamanho: ')
        else:
            tamanho = None
        produto = Produto(codigo_barras, nome_produto, preco, estoque, cor, tamanho)
        repository.cadastra_produto(produto)
    else:
        print(f'Produto já cadastrado: {retorno[1]} {retorno[-1]} {retorno[-2]} - Preço: {retorno[2]} - Itens no estoque: {retorno[3]}')

    
    #Adicionar produto ao banco de dados

def cadastrar_funcionario():
    cpf = input('Insira o CPF do funcionário: ')
    if validations.valida_cpf(cpf) is False:
        print(f'CPF: {cpf} É INVÁLIDO')
        return False
    
    retorno = repository.consulta_funcionario(cpf)
   
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
        repository.cadastra_funcionario(vendedor)
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
    
    retorno = repository.consulta_cliente(cpf)
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
        repository.cadastra_cliente(cliente)
        print(f'Cliente {cliente.nome} com CPF: {cliente.cpf} FOI CADASTRADO COM SUCESSO!')
    else:
        nome, nascimento, rua, numero, complemento = retorno[1], retorno[2], retorno[3], retorno[4], retorno[5]
        print(f"Cliente já cadastrado! {nome} - {nascimento} - {rua} - {numero} - {complemento}")
    
def criar_pedido():
    cliente = input('Insira o CPF do cliente -|> ' )
    cliente = validations.formata_cpf(cliente)
    if validations.valida_cpf(cliente) is False:
        print(f'CPF {cliente} É INVÁLIDO')
        return
    retorno_cliente = repository.consulta_cliente(cliente)
    while retorno_cliente is None:
        print('Cliente deve ser cadastrado: ')
        cadastrar_cliente()
        cliente = input('Insira o CPF do cliente -|> ' )
        cliente = validations.formata_cpf(cliente)
        if validations.valida_cpf(cliente) is False:
            print(f'CPF {cliente} É INVÁLIDO')
            return
        retorno_cliente = repository.consulta_cliente(cliente)
    print(retorno_cliente)

    vendedor = input('Informe o CPF do vendedor -|> ')
    vendedor = validations.formata_cpf(vendedor)
    if validations.valida_cpf(vendedor) is False:
        print(f'CPF {vendedor} É INVÁLIDO')
        return
    if repository.consulta_funcionario(vendedor) is None:
        print('Funcionário não cadastrado!')
        return
    retorno_vendedor = repository.consulta_funcionario(vendedor)
    nota_final = { }   
    print("Adicione os produtos, para finalizar digite 'sair' ao invés do código produto")
    while True:    
        cod_prod = input('Insira o código do produto  -|> ') 
        if cod_prod == 'sair':
            break
        retorno_produto = repository.consulta_produto(cod_prod)
        if retorno_produto is None:
            print('Produto não cadastrado no sistema')
            return
        print(f'{retorno_produto[1]} {retorno_produto[4]} Preço: {retorno_produto[2]}')
        nome_produto, preco_produto = retorno_produto[1] +' '+ retorno_produto[4], float(retorno_produto[2])
        nota_final['vendedor'] = retorno_vendedor[4]
        nota_final['cliente'] = retorno_cliente[1]
        nota_final['produtos'] = {}
        nota_final['produtos'][cod_prod] = {}
        dicio_prods = nota_final['produtos'][cod_prod]
        dicio_prods['nome'] = nome_produto
        dicio_prods['precoUnitário'] = preco_produto
        qtd_prod = input('Insira a quantidade desse produto -|> ')
        if validations.valida_inteiro(qtd_prod) is None:
            print('Informe um número válido')
            return
        if int(qtd_prod) > int(retorno_produto[3]):
            print('Quantidade indisponível no estoque')
            return
        dicio_prods['quantidade'] = qtd_prod

        
        repository.atualiza_produto((int(retorno_produto[3]) - int(qtd_prod)),cod_prod)


    print (nota_final)



while True:
    decisao = input('1 - Cadastrar Cliente\n2 - Cadastrar Funcionário\n3 - Cadastrar Pedido\n4 - Cadastrar Produto\n9 - Sair do programa\n-|> ')
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
    elif decisao == '4':
        validacao = criar_produto()
        if validacao is False:
            print('ERRO NA CRIAÇÃO DO PRODUTO')
    elif decisao == '8':
        ...
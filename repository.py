import sqlite3

def consulta_cliente(cpf):
    conn = sqlite3.connect('../BancoLoja.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM clientes where cpf ='{cpf}'")
    dados = cursor.fetchone()
    return dados

def cadastra_cliente(cliente):
    conn = sqlite3.connect('../BancoLoja.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM clientes where cpf ='{cliente.cpf}'")
    conf_exist = cursor.fetchone()
    if conf_exist:
        pass
    else:
        cursor.execute(f"INSERT INTO clientes (cpf,name,nascimento,rua,numero,complemento) VALUES (?,?,?,?,?,?)"
                       ,(f'{cliente.cpf}', f'{cliente.nome}',f'{cliente.nascimento}', f'{cliente.rua}',f'{cliente.numero}', f'{cliente.complemento}'))
    conn.commit()
    conn.close()

def visualizar_todos_clientes():
    conn = sqlite3.connect('../BancoLoja.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM clientes")
    data_return = cursor.fetchall()
    return data_return
#-------------#

def cadastra_produto(produto):
    conn = sqlite3.connect('../BancoLoja.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM produtos where codigo ={produto.codigo}")
    conf_exist = cursor.fetchone()
    if conf_exist:
        pass
    else:
        cursor.execute(f"INSERT INTO produtos (codigo,nome,preco,estoque,cor,tamanho) VALUES (?,?,?,?,?,?)"
                       ,(f'{produto.codigo}', f'{produto.nome}',f'{produto.preco}', f'{produto.estoque}',f'{produto.cor}', f'{produto.tamanho}'))
    conn.commit()
    conn.close()
        
def consulta_produto(cod):
    conn = sqlite3.connect('../BancoLoja.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM produtos where codigo ={cod}")
    dados = cursor.fetchone()
    return dados

#-------------#

def consulta_funcionario(cpf):
    conn = sqlite3.connect('../BancoLoja.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM funcionarios where cpf ={cpf}")
    dados = cursor.fetchone()
    return dados

def cadastra_funcionario(vendedor):
    conn = sqlite3.connect('../BancoLoja.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM funcionarios where cpf ='{vendedor.cpf}'")
    conf_exist = cursor.fetchone()
    if conf_exist:
        pass
    else:
        cursor.execute(f"INSERT INTO funcionarios (cpf,name,salario,taxa,comissao) VALUES (?,?,?,?,?)"
                       ,(f'{vendedor.cpf}', f'{vendedor.nome}',f'{vendedor.salario}', f'{vendedor.taxa}',f'{vendedor.comissao}'))
    conn.commit()
    conn.close()

#-------------#

def consulta_pedido(num):
    conn = sqlite3.connect('../BancoLoja.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT * from produtos where id ='{num}'")
    dados = cursor.fetchone()
    return dados

#def cadastra_pedido(pedido):



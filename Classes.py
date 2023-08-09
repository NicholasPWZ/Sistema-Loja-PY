class Cliente:
    def __init__(self, nome, cpf, nascimento, rua, numero, complemento):
        self.nome = nome
        self.cpf = cpf
        self.nascimento = nascimento
        self.rua = rua
        self.numero = numero
        self.complemento = complemento

class Item:
    def __init__(self, produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade
        

class Pedido:
    def __init_(self, cliente, item, vendedor):
        self.cliente = cliente
        self.item = item
        self.vendedor = vendedor
        
           

class Produto:
    def __init__(self, codigo, nome, preco, estoque, cor = None, tamanho = None):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
        self.cor = cor
        self.tamanho = tamanho

class Vendedor:
    def __init__(self,cpf, nome, salario, taxa):
        self.nome = nome
        self.cpf = cpf
        self.taxa = float(taxa) / 100
        self.salario = salario
        self.comissao = 0
    
    def calcular_comissao(self,venda):
        valor_final = venda * self.taxa
        self.comissao += valor_final

        
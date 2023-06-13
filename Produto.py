class Produto:
    def __init__(self, codigo, nome, preco, estoque, cor = None, tamanho = None):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
        self.cor = cor
        self.tamanho = tamanho
        
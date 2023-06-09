import Produto
class Item:
    def __init__(self, produto, quantidade):
        if isinstance(produto, Produto):
            self.produto = produto
        else:
            raise TypeError('Produto fornecido não é válido')
        self.quantidade = quantidade

        self.__dict__[produto] = quantidade
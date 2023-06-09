import Cliente, Item, Vendedor
class Pedido:
    def __init_(self, cliente, item, vendedor):
        if isinstance(cliente, Cliente):
            self.cliente = cliente
        else:
            raise TypeError('Cliente fornecido não é válido')
        if isinstance(item, Item):
            self.item = item
        else:
            raise TypeError('Item fornecido não é válido')
        if isinstance(vendedor, Vendedor):
            self.vendedor = vendedor
        else:
            raise TypeError('Vendedor fornecido não é válido')
        
        
        
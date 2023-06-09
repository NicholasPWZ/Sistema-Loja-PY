class Vendedor:
    def __init__(self, nome, cpf, taxa, salario, comissao):
        self.nome = nome
        self.cpf = cpf
        self.taxa = float(taxa)
        self.salario = salario
        self.comissao = comissao
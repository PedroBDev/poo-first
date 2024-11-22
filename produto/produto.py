class Loja:
    taxa=0.3
    def __init__(self, valor_produto_bruto:float):
        self.valor_produto_bruto = valor_produto_bruto

    def consultar_valor_do_produto(self):
        return self.valor_produto_bruto + (self.valor_produto_bruto * self.taxa)

    @classmethod
    def editar_taxa_do_produto(cls, valor:float):
        cls.taxa=valor


produto_1=Loja(10)
print(produto_1.consultar_valor_do_produto())
produto_1.editar_taxa_do_produto(0.5)
print(produto_1.consultar_valor_do_produto())

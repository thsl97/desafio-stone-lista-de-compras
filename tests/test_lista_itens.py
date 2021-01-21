import unittest

from item import Item
from lista_compras import somar_itens


class TestListaItens(unittest.TestCase):

    def test_lista_itens_retorna_preco_de_todos_os_itens(self):
        lista_itens = [Item(valor=100), Item(valor=100)]
        self.assertEquals(somar_itens(lista_itens), 200)

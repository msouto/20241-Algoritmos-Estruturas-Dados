import unittest

from Atividade_07 import produto_escalar
from Atividade_07 import soma_diagonal

class TestProdutoEscalar(unittest.TestCase):
    def test_produto_escalar(self):
        self.assertEqual(produto_escalar([1, 2, 3], [4, 5, 6]), 32)
        self.assertEqual(produto_escalar([0, 0, 0], [1, 2, 3]), 0)
        self.assertEqual(produto_escalar([1, 1, 1], [1, 1, 1]), 3)
        self.assertEqual(produto_escalar([2, 4, 6], [3, 6, 9]), 84)


class TestSomaDiagonal(unittest.TestCase):
    def test_soma_diagonal(self):
        self.assertEqual(soma_diagonal([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 15)
        self.assertEqual(soma_diagonal([[5, 2], [3, 6]]), 11)
        self.assertEqual(soma_diagonal([[1]]), 1)
        self.assertEqual(soma_diagonal([[0, 1], [1, 0]]), 0)


if __name__ == '__main__':
    unittest.main()

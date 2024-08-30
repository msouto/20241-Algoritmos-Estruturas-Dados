import unittest
import eq_linear

class TestFuncaoLinear(unittest.TestCase):
    def test_valor_postivo(self):
        #Teste para um valor positivo
        #de X
        resultado = eq_linear.funcao_linear(2)
        self.assertEqual(resultado, 4)

    def test_valor_negativo(self):
        #Teste para um valor negativo
        #de X
        resultado = eq_linear.funcao_linear(-2)
        self.assertEqual(resultado, -4)


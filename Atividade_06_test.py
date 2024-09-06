#Atividade 06 - Exercicíos II - TDD

#Questão 1 - Função: Cálculo do Fatorial
#Descrição: Crie uma função fatorial(n) que receba um número inteiro n e retorne o
#fatorial desse número. O fatorial de n é o produto de todos os números inteiros de 1 até
#n.

import unittest
from unittest.mock import patch

from Atividade_06 import fatorial
from Atividade_06 import soma_pares
from Atividade_06 import conversor_temperatura
from Atividade_06 import soma_matrizes

class TestFatorial(unittest.TestCase):
    def test_fatorial(self):
        self.assertEqual(fatorial(5), 120)
        self.assertEqual(fatorial(0), 1)
        self.assertEqual(fatorial(1), 1)
        self.assertEqual(fatorial(6), 720)

if __name__ == '__main__':
    unittest.main()

#Questão 2 - Vetor: Soma de Elementos Pares
#Descrição: Crie uma função soma_pares(vetor) que receba um vetor de inteiros e
#retorne a soma de todos os elementos pares do vetor.
class TestSomaPares(unittest.TestCase):
    def test_soma_pares(self):
        self.assertEqual(soma_pares([1, 2, 3, 4, 5, 6]), 12)
        self.assertEqual(soma_pares([10, 21, 32, 43, 54]), 96)
        self.assertEqual(soma_pares([0, -2, -4, 3]), -6)
        self.assertEqual(soma_pares([1, 3, 5]), 0)

if __name__ == '__main__':
    unittest.main()


#Questão 3 - Input/Output: Conversor de Temperatura
#Descrição: Crie uma função conversor_temperatura() que leia uma temperatura em
#graus Celsius fornecida pelo usuário, converta para Fahrenheit e imprima o resultado. A
#fórmula de conversão é: F = C * 9/5 + 32.

class TestConversorTemperatura(unittest.TestCase):
    @patch('builtins.input', return_value='0')
    @patch('builtins.print')
    def test_conversor_temperatura(self, mock_print, mock_input):
        conversor_temperatura()
        mock_print.assert_called_with(32.0)

    @patch('builtins.input', return_value='100')
    @patch('builtins.print')
    def test_conversor_temperatura_100(self, mock_print, mock_input):
        conversor_temperatura()
        mock_print.assert_called_with(212.0)

if __name__ == '__main__':
    unittest.main()


#Questão 4 - Matriz Bidimensional: Soma de Matrizes
#Descrição: Crie uma função soma_matrizes(m1, m2) que receba duas matrizes 2x2 e
#retorne uma nova matriz, que seja a soma das duas matrizes recebidas.
class TestSomaMatrizes(unittest.TestCase):
    def test_soma_matrizes(self):
        m1 = [[1, 2], [3, 4]]
        m2 = [[5, 6], [7, 8]]
        resultado = soma_matrizes(m1, m2)
        self.assertEqual(resultado, [[6, 8], [10, 12]])

        m1 = [[0, 0], [0, 0]]
        m2 = [[1, 2], [3, 4]]
        resultado = soma_matrizes(m1, m2)
        self.assertEqual(resultado, [[1, 2], [3, 4]])

        m1 = [[-1, -2], [-3, -4]]
        m2 = [[1, 2], [3, 4]]
        resultado = soma_matrizes(m1, m2)
        self.assertEqual(resultado, [[0, 0], [0, 0]])

if __name__ == '__main__':
    unittest.main()

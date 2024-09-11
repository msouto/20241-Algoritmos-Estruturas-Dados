#Atividade 06 - Exercicíos II

#Questão 1 - Função: Cálculo do Fatorial
#Descrição: Crie uma função fatorial(n) que receba um número inteiro n e retorne o
#fatorial desse número. O fatorial de n é o produto de todos os números inteiros de 1 até
#n.
def fatorial(n):
  if n == 0 or n ==1:
    return 1
  resultado = 1
  for i in range(2, n+1):
    resultado *= i
  return resultado
  #pass

#Questão 2 - Vetor: Soma de Elementos Pares
#Descrição: Crie uma função soma_pares(vetor) que receba um vetor de inteiros e
#retorne a soma de todos os elementos pares do vetor.
def soma_pares(vetor):
  soma = 0
  for numero in vetor:
    if numero % 2 == 0:
      soma+=numero
  return soma
  #pass

#Questão 3 - Input/Output: Conversor de Temperatura
#Descrição: Crie uma função conversor_temperatura() que leia uma temperatura em
#graus Celsius fornecida pelo usuário, converta para Fahrenheit e imprima o resultado. A
#fórmula de conversão é: F = C * 9/5 + 32.
def conversor_temperatura():
  celsius = float(input("Digite a temp. em graus Celsius: "))
  fahrenheit = celsius * 9/5 + 32
  print(fahrenheit)
  #pass

#Questão 4 - Matriz Bidimensional: Soma de Matrizes
#Descrição: Crie uma função soma_matrizes(m1, m2) que receba duas matrizes 2x2 e
#retorne uma nova matriz, que seja a soma das duas matrizes recebidas.
def soma_matrizes(m1,m2):
  matriz_soma = [[0,0],[0,0]]
  for i in range(2):
    for j in range(2):
      matriz_soma[i][j] = m1[i][j] + m2[i][j]
  return matriz_soma
  #pass

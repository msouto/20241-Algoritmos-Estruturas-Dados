# Atividade 7 - Lista 3

#Questão 1
#Produto Escalar de Dois Vetores:
#Descrição: Multiplica os elementos correspondentes #de dois vetores e soma os resultados.
#Função: produto_escalar(vetor1, vetor2)
#TDD: Verifica vetores comuns, vetores com zeros e vetores com valores idênticos.

def produto_escalar(vetor1,vetor2):
    produto = 0
    for i in range(len(vetor1)):
        produto += vetor1[i] * vetor2[i] 
    return produto

#Questão 2
#Soma dos Elementos na Diagonal Principal de uma Matriz:
#Descrição: Soma os elementos localizados na diagonal principal de uma matriz quadrada.
#Função: soma_diagonal(matriz)
#TDD: Testa matrizes de diferentes tamanhos, incluindo casos simples e com valores zero.
def soma_diagonal(matriz):
    soma = 0
    #Como implementar ?
    return soma

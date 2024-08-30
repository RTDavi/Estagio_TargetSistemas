"""
Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores 
(exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, 
informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se 
o número informado pertence ou não a sequência.
"""


def e_sequencia_fibonacci(numero: int):

    sequencia = [0, 1]
    while sequencia[-1] < numero:
        sequencia.append(sequencia[-1] + sequencia[-2])

    if numero in sequencia:
        return True

    return False


print("------BEM VINDO AO PROGRAMA TESTE DA SEQUENCIA DE FIBONNACTI------")
numero = int(input("DIGITE UM NÚMERO: "))

if e_sequencia_fibonacci(numero):
    print(f"O NÚMERO {numero} PERTENCE A SEQUÊNCIA DE FIBONACCI!")

else:
    print(f"O NÚMERO {numero} NÃO PERTENCE A SEQUÊNCIA DE FIBONACCI.")

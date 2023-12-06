""""
2- Faça um programa que preencha por leitura um vetor de 10 posições, 
e conta quantos valores diferentes existem no vetor.
"""

def contar_valores_diferentes(vetor):
    conjunto_valores = set(vetor)
    return len(conjunto_valores)

vetor = []

for i in range(10):
    valor = int(input(f"Digite o valor para a posição {i + 1}: "))
    vetor.append(valor)

quantidade_diferentes = contar_valores_diferentes(vetor)

print(f"Quantidade de valores diferentes no vetor: {quantidade_diferentes}")
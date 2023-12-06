"""
01 - Dada a lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52] faça um programa que:

a) imprima o maior elemento
b) imprima o menor elemento
c) imprima os números pares
d) imprima o número de ocorrências do primeiro elemento da lista
e) imprima a média dos elementos
f) imprima a soma dos elementos de valor negativo

"""
lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52]


maior_elemento = max(lista)
print(f"Maior elemento: {maior_elemento}")


menor_elemento = min(lista)
print(f"Menor elemento: {menor_elemento}")


numeros_pares = [num for num in lista if num % 2 == 0]
print(f"Números pares: {numeros_pares}")


primeiro_elemento = lista[0]
num_ocorrencias_primeiro = lista.count(primeiro_elemento)
print(f"Número de ocorrências do primeiro elemento: {num_ocorrencias_primeiro}")


soma_elementos = sum(lista)
media_elementos = soma_elementos / len(lista)
print(f"Média dos elementos: {media_elementos}")


soma_negativos = sum(num for num in lista if num < 0)
print(f"Soma dos elementos negativos: {soma_negativos}")







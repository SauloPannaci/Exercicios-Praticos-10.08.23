""""
3- Faça um programa que preencha por leitura um vetor de 5 posições,
e informe a posição em que um valor x (lido do teclado) aparece pela primeira
vez no vetor. Caso o valor x não seja encontrado, o programa deve imprimir o valor -1

"""

def main():
    tamanho_vetor = 5
    vetor = []

    
    for i in range(tamanho_vetor):
        valor = int(input(f"Digite o valor para a posição {i+1}: "))
        vetor.append(valor)

    
    valor_procurado = int(input("Digite o valor a ser procurado: "))
    
    
    posicao_encontrada = -1
    for i in range(len(vetor)):
        if vetor[i] == valor_procurado:
            posicao_encontrada = i
            break
    

    if posicao_encontrada != -1:
        print(f"O valor {valor_procurado} foi encontrado na posição {posicao_encontrada + 1}.")
    else:
        print("-1: Valor não encontrado no vetor.")

if __name__ == "__main__":
    main()

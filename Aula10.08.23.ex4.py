"""4- Um dado é lançado 50 vezes, e o valor correspondente é armazenado em um vetor
. Faça um programa que simule o lançamento do dado e determine o percentual de ocorrências 
de face 6 do dado dentre esses 50 lançamentos.
"""




import random

def main():
    num_lancamentos = 50
    num_ocorrencias_face6 = 0
    
    for _ in range(num_lancamentos):
        resultado_lancamento = random.randint(1, 6)  
        if resultado_lancamento == 6:
            num_ocorrencias_face6 += 1
    
    percentual_face6 = (num_ocorrencias_face6 / num_lancamentos) * 100
    
    print(f"Percentual de ocorrências da face 6: {percentual_face6:.2f}%")

if __name__ == "__main__":
    main()






from random import randint

def maiorNumero(maior, matriz):
    maior = matriz[0][0];
    for l in range(len(matriz)):
        for c in range(len(matriz)):
            if(matriz[l][c] > maior):
                maior = matriz[l][c];

    return maior;

def menorNumero(menor, matriz):
    menor = matriz[0][0];
    for l in range(len(matriz)):
        for c in range(len(matriz)):
            if(matriz[l][c] < menor):
                menor = matriz[l][c];

    return menor;

matriz = [];maior = 0;menor = 0;

for l in range(0, 4):
    colunas = [];
    for c in range(0, 4):
        numeros = int(randint(0, 500));
        colunas.append(numeros);
    
    matriz.append(colunas);

for l in range(0, 4):
    for c in range(0, 4):
        print(matriz[l][c], "", end="");

print("\nO maior número é: {}".format(maiorNumero(maior, matriz)));
print("O menor número é: {}".format(menorNumero(menor, matriz)));
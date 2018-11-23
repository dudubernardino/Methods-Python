from random import randint

def maiorNumero(maior, array):
    maior = array[0];
    for i in range(len(array)):
        if(array[i] > maior):
            maior = array[i];

    return maior;

def menorNumero(menor, array):
    menor = array[0];
    for i in range(len(array)):
        if(array[i] < menor):
            menor = array[i];

    return menor;
    
vetor = [];maior = 0;menor = 0;

for i in range(0, 10):
    vetor.append(int(randint(0, 500)));

for i in range(0, 10):
    print(vetor[i], "", end="");

print("\nO maior número é: {}".format(maiorNumero(maior, vetor)));
print("O menor número é: {}".format(menorNumero(menor, vetor)));

from random import randint

def tacaOPau():
    numero = float(randint(0, 9));
    return numero

matriz = [];

for l in range(4):
    colunas = [];
    for c in range(4):
        numeros = tacaOPau();
        colunas.append(numeros);
    
    matriz.append(colunas);

for l in range(4):
    for c in range(4):
        print("matriz[{:d}] [{:d}]: {:.2f}".format(l, c, matriz[l][c]));
        
    print("\n");
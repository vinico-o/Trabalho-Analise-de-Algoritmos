import numpy as np

def heap_regra_max(lista, n, i):
   
    maior = i  
    
    filho_da_esquerda = 2 * i + 1
    
    filho_da_direita = 2 * i + 2

    if filho_da_esquerda < n and lista[maior] < lista[filho_da_esquerda]:
        maior = filho_da_esquerda

    
    if filho_da_direita < n and lista[maior] < lista[filho_da_direita]:
        maior = filho_da_direita

   
    if maior != i:
        lista[i], lista[maior] = lista[maior], lista[i] 
        
        heap_regra_max(lista, n, maior)

def HeapSort(lista):

    n = len(lista)

    for i in range(n // 2 - 1, -1, -1):
        
        heap_regra_max(lista, n, i)

    
    for i in range(n - 1, 0, -1):

        lista[i], lista[0] = lista[0], lista[i] 
        
        heap_regra_max(lista, i, 0)


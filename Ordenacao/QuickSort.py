def particao_primeiro(vetor, inicio, fim):
    
    pivo = vetor[inicio]  
    i = inicio            
    
    for j in range(inicio + 1, fim + 1):

        if vetor[j] < pivo:

            i += 1
            temp = vetor[i]
            vetor[i] = vetor[j]
            vetor[j] = temp
    
    
    vetor[i], vetor[inicio] = vetor[inicio], vetor[i]

    return i 

def quickSort_primeiro(lista, inicio, fim):
    
    if inicio < fim:

        p = particao_primeiro(lista, inicio, fim)

        quickSort_primeiro(lista, inicio, p - 1)  
        quickSort_primeiro(lista, p + 1, fim)    

def QuickSortPrimeiro(lista):
    inicio = 0
    fim = len(lista) - 1
    quickSort_primeiro(lista, inicio, fim);

def particao_central(lista, inicio, fim):

    meio = (inicio + fim) // 2
    pivo = lista[meio]
    
    lista[meio], lista[inicio] = lista[inicio], lista[meio]
    i = inicio

    for j in range(inicio + 1, fim + 1):

        if lista[j] < pivo:

            i += 1
            lista[i], lista[j] = lista[j], lista[i]
    


    lista[i], lista[inicio] = lista[inicio], lista[i]
    return i

def quickSort_central(lista, inicio, fim):
    
    if inicio < fim:

        p = particao_central(lista, inicio, fim)

        quickSort_central(lista, inicio, p - 1) 
        quickSort_central(lista, p + 1, fim)    

def QuickSortCentral(lista):
    inicio = 0
    fim = len(lista) - 1
    quickSort_central(lista, inicio, fim);

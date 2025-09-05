def ordenarVetor_merge(lista, inicio, fim):
    if inicio < fim:
        meio = (inicio + fim) // 2

        ordenarVetor_merge(lista, inicio, meio)
        ordenarVetor_merge(lista, meio + 1, fim)

        intercalarVetor_merge(lista, inicio, meio, fim)



def intercalarVetor_merge(lista, inicio, meio, fim):
    
    tamanho1 = meio - inicio + 1
    tamanho2 = fim - meio

    vetor1 = []
    vetor2 = []

    for i in range (tamanho1):
        vetor1.append(lista[inicio + i])

    for j in range (tamanho2):
        vetor2.append(lista[meio + j + 1])

    i = 0
    j = 0
    k = inicio

    while i < tamanho1 and j < tamanho2:
        if vetor1[i] <= vetor2[j]:
            lista[k] = vetor1[i]

            i += 1
            k += 1
        
        else:
            lista[k] = vetor2[j]

            j += 1
            k += 1

    
    while i < tamanho1:
        lista[k] = vetor1[i]

        i += 1
        k += 1

    while j < tamanho2:
        lista[k] = vetor2[j]

        j += 1
        k += 1

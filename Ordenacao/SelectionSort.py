def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        
        menor = i
        
        for j in range(i + 1, n):
            if (lista[j] < lista[menor]):
                menor = j

        temp = lista[i]

        lista[i] = lista[menor]

        lista[menor] = temp


    return lista

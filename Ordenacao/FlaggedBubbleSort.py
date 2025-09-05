def FlaggedBubbleSort(lista):
    n = len(lista)
    
    for i in range(n):
        troca = False
        for j in range(0, n - i - 1):
            
            if lista[j] > lista[j + 1]:
                troca = True
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
            
        if not troca:
            break
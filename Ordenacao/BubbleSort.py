def bubble_sort(lista):
    n = len(lista)
    # Percorre todos os elementos da lista
    for i in range(n):
        # Últimos i elementos já estão no lugar
        for j in range(0, n - i - 1):
            # Troca se o elemento encontrado é maior que o próximo
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
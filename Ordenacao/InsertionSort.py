def EncontrarPosicao(lista, numero, fim):
    i = 0
    while i <= fim and lista[i] <= numero:
        i += 1
    return i

def DeslocarLista(lista, posicao, fim):
    i = fim
    while i >= posicao:
        lista[i + 1] = lista[i]
        i -= 1

def InsertionSort(lista):
    n = len(lista)

    for i in range(1, n):  # começa em 1
        elemento = lista[i]
        pos = EncontrarPosicao(lista, elemento, i - 1)
        DeslocarLista(lista, pos, i - 1)
        lista[pos] = elemento
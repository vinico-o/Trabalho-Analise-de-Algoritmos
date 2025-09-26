def shell_sort(lista, n, lista_incrementos, n_incremento):
    for incr_index in range(n_incremento):
        span = lista_incrementos[incr_index]
        
        for j in range(span, n):
            y = lista[j]
            k = j - span
            
            while k >= 0 and lista[k] > y:
                lista[k + span] = lista[k]
                k -= span
            lista[k + span] = y

def ShellSort(lista):
    if not lista:
        return []

    n = len(lista)
    
    lista_incrementos = []
    h = 1
    while h < n / 3:
        lista_incrementos.append(h)
        h = 3 * h + 1
    
    lista_incrementos.reverse()
    
    if not lista_incrementos:
        lista_incrementos.append(1)

    n_incremento = len(lista_incrementos)
    
    shell_sort(lista, n, lista_incrementos, n_incremento)
    
    return lista
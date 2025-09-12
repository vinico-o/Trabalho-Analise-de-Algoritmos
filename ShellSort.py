def ShellSort(lista, n, lista_incrementos, n_incremento):
    for incr in range (0, n_incremento):
        span = lista_incrementos[incr]
        
        j = span
        for j in range (n):
            y = lista[j]

            k = j - span
            
            while (k >= 0 and lista[k] > y):
                lista[k + span] = lista[k]

                k -= span
            lista[k + span] = y

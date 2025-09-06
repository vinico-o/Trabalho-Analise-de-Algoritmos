#Bibliotecas utilizadas
import random
import time

#Módulo dos Algoritmos
import Ordenacao.BubbleSort as bs
import Ordenacao.FlaggedBubbleSort as fbs
import Ordenacao.InsertionSort as ins
import Ordenacao.MergeSort as ms
import Ordenacao.SelectionSort as ss

lista = random.sample(range(1, 10001), 10000)
print(lista)

inicio = time.time()
ms.MergeSort(lista)
fim = time.time()
print(f"{fim - inicio}")

print(lista)
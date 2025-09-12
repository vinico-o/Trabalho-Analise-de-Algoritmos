#Bibliotecas utilizadas
import random
import time
import csv

#Módulo dos Algoritmos
import Ordenacao.BubbleSort as bs
import Ordenacao.FlaggedBubbleSort as fbs
import Ordenacao.InsertionSort as ins
import Ordenacao.MergeSort as ms
import Ordenacao.SelectionSort as ss

arquivo = "Algorithms.csv"

def adicionarInformacoes(nome, tamanho, tempo):
    with open(arquivo, "a", newline="") as arq:
        escritor = csv.writer(arq)
        escritor.writerow([nome, tamanho, tempo])

with open(arquivo, "w", newline="") as arq:
    escritor = csv.writer(arq)
    escritor.writerow(["Algoritmo", "Tamanho", "Tempo"])

lista = random.sample(range(1, 10001), 10000)

inicio = time.time()
ms.MergeSort(lista)
fim = time.time()
tempo = fim - inicio
adicionarInformacoes("MergeSort", 10000, f"{tempo:.2f}")

inicio = time.time()
bs.BubbleSort(lista)
fim = time.time()
tempo = fim - inicio
adicionarInformacoes("BubbleSort", 10000, f"{tempo:.2f}")

print(lista)
#Bibliotecas utilizadas
import random
import time
import csv
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#Módulo dos Algoritmos
import Ordenacao.BubbleSort as bs
import Ordenacao.FlaggedBubbleSort as fbs
import Ordenacao.InsertionSort as ins
import Ordenacao.MergeSort as ms
import Ordenacao.SelectionSort as ss

def adicionarInformacoes(nome, tamanho, tempo):
    with open(arquivo, "a", newline="") as arq:
        escritor = csv.writer(arq)
        escritor.writerow([nome, tamanho, tempo])

arquivo = "Algorithms.csv"
tamanhos = [100, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
funcoes = {
    "BubbleSort": bs.BubbleSort,
    "FlaggedBubbleSort": fbs.FlaggedBubbleSort,
    "InsertionSort": ins.InsertionSort,
    "MergeSort": ms.MergeSort,
    "SelectionSort": ss.selection_sort
}

with open(arquivo, "w", newline="") as arq:
    escritor = csv.writer(arq)
    #Algoritmo = nome do algoritmo de ordenacao
    #Tamanho = tamanho do vetor utilizado na ordenacao
    #Tempo = Tempo de execução do Algoritmo
    #Tipo = Tipo do vetor: Crescente, Aleatorio, Decrescente
    escritor.writerow(["Algoritmo", "Tamanho", "Tempo"]) #TODO: adicionar Tipo

for nome, funcao in funcoes.items():
    for tamanho in tamanhos:
        lista = random.sample(range(1, tamanho + 1), tamanho)
        inicio = time.time()
        funcao(lista)
        fim = time.time()
        tempo = fim - inicio
        adicionarInformacoes(nome, tamanho, f"{tempo:.2f}")

print("Arquivo Finalizado!")

df = pd.read_csv("Algorithms.csv")

df_bubble = df[df["Algoritmo"] == "BubbleSort"]
df_InsertionSort = df[df["Algoritmo"] == "InsertionSort"]
df_mergeSort = df[df["Algoritmo"] == "MergeSort"]


plt.figure(figsize= (4, 5))
plt.plot(df_bubble["Tamanho"], df_bubble["Tempo"], color = "blue" , label="Bubble")
#plt.plot(df_InsertionSort["Tamanho"], df_InsertionSort["Tempo"], color= "red", label="Insertion")
#plt.plot(df_mergeSort["Tamanho"], df_mergeSort["Tempo"], color= "green", label="Merge")
plt.xlabel("Tamanho")
plt.ylabel("Tempo")
plt.legend()
plt.show()

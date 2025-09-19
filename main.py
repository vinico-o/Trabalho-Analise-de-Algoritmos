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

def adicionarInformacoes(nome, tamanho, tempo, tipo):
    with open(arquivo, "a", newline="") as arq:
        escritor = csv.writer(arq)
        escritor.writerow([nome, tamanho, tempo, tipo])

arquivo = "Algorithms.csv"
tamanhos = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 20000, 30000, 40000, 50000]
tipos = ["Crescente", "Aleatorio", "Decrescente"]
funcoes = {
    "BubbleSort": bs.BubbleSort,
    #"FlaggedBubbleSort": fbs.FlaggedBubbleSort,
    # "InsertionSort": ins.InsertionSort,
    # "MergeSort": ms.MergeSort,
    # "SelectionSort": ss.selection_sort
}

with open(arquivo, "w", newline="") as arq:
    escritor = csv.writer(arq)
    #Algoritmo = nome do algoritmo de ordenacao
    #Tamanho = tamanho do vetor utilizado na ordenacao
    #Tempo = Tempo de execução do Algoritmo
    #Tipo = Tipo do vetor: Crescente, Aleatorio, Decrescente
    escritor.writerow(["Algoritmo", "Tamanho", "Tempo", "Tipo"]) #TODO: adicionar Tipo

for nome, funcao in funcoes.items():
    for tamanho in tamanhos:
        for tipo in tipos:
            if tipo == "Crescente":
                lista = list(range(1, tamanho + 1))
            elif tipo == "Decrescente":
                lista = list(range(tamanho + 1, 1, -1))
            else:
                lista = random.sample(range(1, tamanho + 1), tamanho)
            inicio = time.time()
            funcao(lista)
            fim = time.time()
            tempo = fim - inicio
            adicionarInformacoes(nome, tamanho, f"{tempo:.2f}", tipo)
print("Arquivo Finalizado!")

df = pd.read_csv("Algorithms.csv")

df_bubble1 = df[(df["Algoritmo"] == "BubbleSort") & (df["Tipo"] == "Aleatorio")]
df_bubble2 = df[(df["Algoritmo"] == "BubbleSort") & (df["Tipo"] == "Crescente")]
df_bubble3 = df[(df["Algoritmo"] == "BubbleSort") & (df["Tipo"] == "Decrescente")]
""" df_flaggaedbubble1 = df[(df["Algoritmo"] == "FlaggedBubbleSort") & (df["Tipo"] == "Aleatorio")]
df_flaggaedbubble2 = df[(df["Algoritmo"] == "FlaggedBubbleSort") & (df["Tipo"] == "Crescente")]
df_flaggaedbubble3 = df[(df["Algoritmo"] == "FlaggedBubbleSort") & (df["Tipo"] == "Decrescente")] """


plt.figure(figsize= (4, 5))
plt.plot(df_bubble1["Tamanho"], df_bubble1["Tempo"], color = "red" , label="Bubble Aleatorio")
plt.plot(df_bubble2["Tamanho"], df_bubble2["Tempo"], color = "green" , label="Bubble Crescente")
plt.plot(df_bubble3["Tamanho"], df_bubble3["Tempo"], color = "blue" , label="Bubble Decrescente")
#plt.plot(df_InsertionSort["Tamanho"], df_InsertionSort["Tempo"], color= "red", label="Insertion")
#plt.plot(df_mergeSort["Tamanho"], df_mergeSort["Tempo"], color= "green", label="Merge")
#plt.plot(df_selectionSort["Tamanho"], df_selectionSort["Tempo"], color= "yellow", label="Selection")
plt.xlabel("Tamanho")
plt.ylabel("Tempo")
plt.legend()
plt.show()

import csv
import numpy as np

arquivo = "Algorithms.csv"

def adicionarInformacoes(nome, tamanho, tempo, tipo):
    with open(arquivo, "a", newline="") as arq:
        escritor = csv.writer(arq)
        escritor.writerow([nome, tamanho, tempo, tipo])

def criarArquivo():
    with open(arquivo, "w", newline="") as arq:
        escritor = csv.writer(arq)
        #Algoritmo = nome do algoritmo de ordenacao
        #Tamanho = tamanho do vetor utilizado na ordenacao
        #Tempo = Tempo de execução do Algoritmo
        #Tipo = Tipo do vetor: Crescente, Aleatorio, Decrescente
        escritor.writerow(["Algoritmo", "Tamanho", "Tempo", "Tipo"])
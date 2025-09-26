import Ordenacao.BubbleSort as bs
import Ordenacao.FlaggedBubbleSort as fbs
import Ordenacao.HeapSort as hps
import Ordenacao.InsertionSort as ins
import Ordenacao.MergeSort  as ms
import Ordenacao.QuickSort as qs
import Ordenacao.SelectionSort as ses
import Ordenacao.ShellSort as shs
import Utils.registro as reg
import time
import random

tamanhos = [100, 163, 268, 439, 719, 1178, 1930, 3162, 5179, 8483, 13894, 22758, 37275, 61054, 100000]
tipos = ["Crescente", "Decrescente", "Aleatorio"]
funcoes = {
    "BubbleSort": bs.BubbleSort,
    "FlaggedBubbleSort": fbs.FlaggedBubbleSort,
    "HeapSort": hps.HeapSort,
    "InsertionSort": ins.InsertionSort,
    "MergeSort": ms.MergeSort,
    "QuickSortCentral": qs.QuickSortCentral,
    "QuickSortPrimeiro": qs.QuickSortPrimeiro,
    "SelectionSort": ses.selection_sort,
    "ShellSort": shs.ShellSort
}

def ordenacao():
    for nome, funcao in funcoes.items():
        for tamanho in tamanhos:
            for tipo in tipos:
                if tipo == "Crescente":
                    lista = list(range(1, tamanho + 1))
                elif tipo == "Decrescente":
                    lista = list(range(tamanho + 1, 1, -1))
                else:
                    lista = random.sample(range(1, tamanho + 1), tamanho)
                escreverArquivo(nome, funcao, tamanho, tipo, lista)
                
def escreverArquivo(nome, funcao, tamanho, tipo, lista):
    inicio = time.time()
    funcao(lista)
    fim = time.time()
    tempo = fim - inicio
    reg.adicionarInformacoes(nome, tamanho, f"{tempo:.2f}", tipo)

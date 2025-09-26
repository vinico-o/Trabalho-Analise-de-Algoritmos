import pandas as pd
import matplotlib.pyplot as plt

def lerArquivo():
    return pd.read_csv("Algorithms.csv")

def gerarDataFrame_tipoEspecifico(tipo):
    df = lerArquivo()
    
    return {
        "BubbleSort": df[(df["Algoritmo"] == "BubbleSort") & (df["Tipo"] == tipo)],
        "FlaggedBubbleSort": df[(df["Algoritmo"] == "FlaggedBubbleSort") & (df["Tipo"] == tipo)],
        "HeapSort": df[(df["Algoritmo"] == "HeapSort") & (df["Tipo"] == tipo)],
        "InsertionSort": df[(df["Algoritmo"] == "InsertionSort") & (df["Tipo"] == tipo)],
        "MergeSort": df[(df["Algoritmo"] == "MergeSort") & (df["Tipo"] == tipo)],
        "QuickSortCentral": df[(df["Algoritmo"] == "QuickSortCentral") & (df["Tipo"] == tipo)],
        "QuickSortPrimeiro": df[(df["Algoritmo"] == "QuickSortPrimeiro") & (df["Tipo"] == tipo)],
        "SelectionSort": df[(df["Algoritmo"] == "SelectionSort") & (df["Tipo"] == tipo)],
        "ShellSort": df[(df["Algoritmo"] == "ShellSort") & (df["Tipo"] == tipo)],
    }

def gerarDataframe_algoritmoEspecico(algoritmo):
    df = lerArquivo()
    
    return {
        "Aleatorio": df[(df["Algoritmo"] == algoritmo) & (df["Tipo"] == "Aleatorio")],
        "Crescente": df[(df["Algoritmo"] == algoritmo) & (df["Tipo"] == "Crescente")],
        "Decrescente": df[(df["Algoritmo"] == algoritmo) & (df["Tipo"] == "Decrescente")]
    }

def plotarGrafico_algoritmoEspecifico(algoritmo, titulo):

    dados = gerarDataframe_algoritmoEspecico(algoritmo)

    cores = {"Aleatorio": "red", "Crescente": "green", "Decrescente": "blue"}
    
    plt.figure(figsize=(5, 4))
    for tipo, df_tipo in dados.items():
        plt.plot(df_tipo["Tamanho"], df_tipo["Tempo"], color=cores[tipo], label=f"{algoritmo} {tipo}")
    
    plt.xlabel("Tamanho")
    plt.ylabel("Tempo (s)")
    plt.title(titulo)
    plt.legend()
    plt.grid(True)
    plt.show()

def plotarGrafico_tipoEspecifico(tipo, titulo):

    dados = gerarDataFrame_tipoEspecifico(tipo)

    cores_algoritmos = {
        "BubbleSort": "red",
        "FlaggedBubbleSort": "orange",
        "HeapSort": "gold",
        "InsertionSort": "green",
        "MergeSort": "cyan",
        "QuickSortCentral": "blue",
        "QuickSortPrimeiro": "purple",
        "SelectionSort": "magenta",
        "ShellSort": "black"
    }
    
    plt.figure(figsize=(5, 4))
    for algoritmo, df_algoritmo in dados.items():
        plt.plot(df_algoritmo["Tamanho"], df_algoritmo["Tempo"], color=cores_algoritmos[algoritmo], label=f"{algoritmo} {tipo}")
    
    plt.xlabel("Tamanho")
    plt.ylabel("Tempo (s)")
    plt.title(titulo)
    plt.legend()
    plt.grid(True)
    plt.show()
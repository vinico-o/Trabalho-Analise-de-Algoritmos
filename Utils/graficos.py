import pandas as pd
import matplotlib.pyplot as plt

def lerArquivo():
    return pd.read_csv("Algorithms.csv")

def gerarDataframe(df, algoritmo):
    return {
        "Aleatorio": df[(df["Algoritmo"] == algoritmo) & (df["Tipo"] == "Aleatorio")],
        "Crescente": df[(df["Algoritmo"] == algoritmo) & (df["Tipo"] == "Crescente")],
        "Decrescente": df[(df["Algoritmo"] == algoritmo) & (df["Tipo"] == "Decrescente")]
    }

def plotarGrafico(algoritmo, titulo):
    dados = lerArquivo();
    dados = gerarDataframe(dados, algoritmo)
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
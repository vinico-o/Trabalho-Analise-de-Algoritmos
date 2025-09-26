import sys
import Utils.execucao as execucao
import Utils.registro as registro
import Utils.graficos as grafico

# aumenta o numero de chamadas recursivas para 3000
sys.setrecursionlimit(200000)



""" graficos.plotarGrafico("BubbleSort", "BubbleSort")
graficos.plotarGrafico("FlaggedBubbleSort", "FlaggedBubbleSort")
graficos.plotarGrafico("HeapSort", "HeapSort")
graficos.plotarGrafico("InsertionSort", "InsertionSort")
graficos.plotarGrafico("MergeSort", "MergeSort")
graficos.plotarGrafico("QuickSortCentral", "QuickSortCentral")
graficos.plotarGrafico("QuickSortPrimeiro", "QuickSortPrimeiro")
graficos.plotarGrafico("SelectionSort", "SelectionSort")
graficos.plotarGrafico("ShellSort", "ShellSort");  """



def lerArquivo_ou_ordenar():
    i = int(input("\nDeseja ler o arquivo Algorithms.csv ou fazer a ordenação (0 - LER || 1 - ORDENAR): "))
    return i

def leitura_ordenacao(i):
    if i == 1:
        registro.criarArquivo()
        execucao.ordenacao()
        print ("\nOrdenação feita!")
    menu()

def todos_algoritmos(i):
    if i == 1:
        grafico.plotarGrafico_tipoEspecifico("Crescente", "Crescente")
    elif i == 2:
        grafico.plotarGrafico_tipoEspecifico("Decrescente", "Decrescente")
    else:
        grafico.plotarGrafico_tipoEspecifico("Aleatorio", "Aleatorio")

def algoritmo_especifico(i):
    if i == 4:
        grafico.plotarGrafico_algoritmoEspecifico("BubbleSort", "BubbleSort")
    elif i == 5:
        grafico.plotarGrafico_algoritmoEspecifico("FlaggedBubbleSort", "FlaggedBubbleSort")
    elif i == 6:
        grafico.plotarGrafico_algoritmoEspecifico("HeapSort", "HeapSort")
    elif i == 7:
        grafico.plotarGrafico_algoritmoEspecifico("QuickSortCentral", "QuickSortCentral")
    elif i == 8:
        grafico.plotarGrafico_algoritmoEspecifico("QuickSortPrimeiro", "QuickSortPrimeiro")
    elif i == 9:
        grafico.plotarGrafico_algoritmoEspecifico("SelectionSort", "SelectionSort")
    elif i == 10:
        grafico.plotarGrafico_algoritmoEspecifico("ShellSort", "ShellSort")

def menu():
    print ("Informe a opção de gráfico dos tipos de ordenação")
    print ("1-  Todos algoritmos com entrada crescente")
    print ("2-  Todos algoritmos com entrada decrescente")
    print ("3-  Todos algoritmos com entrada aleatória")
    print ("4-  BubbleSort com as três entradas")
    print ("5-  FlaggedBubbleSort com as três entradas")
    print ("6-  HeapSort com as três entradas")
    print ("7-  QuickSortCentral com as três entradas")
    print ("8-  QuickSortPrimeiro com as três entradas")
    print ("9-  SelectionSort com as três entradas")
    print ("10- ShellSort com as três entradas")
    print ("11- SAIR")

    i = int(input())

    if i >= 1 and i <= 3:
        todos_algoritmos(i)
        menu()

    elif i >= 4 and i <= 10:
        algoritmo_especifico(i)
        menu()
    
    else:
        print ("Índice inválido ou fim da execução(10)")



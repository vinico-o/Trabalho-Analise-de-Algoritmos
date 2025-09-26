import Utils.execucao as execucao
import Utils.graficos as graficos
import Utils.registro as registro
import Utils.sistema as sistema
import sys
# aumenta o numero de chamadas recursivas para 3000
sys.setrecursionlimit(200000)



""" graficos.plotarGrafico("BubbleSort", "BubbleSort");
graficos.plotarGrafico("FlaggedBubbleSort", "FlaggedBubbleSort");
graficos.plotarGrafico("HeapSort", "HeapSort");
graficos.plotarGrafico("InsertionSort", "InsertionSort");
graficos.plotarGrafico("MergeSort", "MergeSort");
graficos.plotarGrafico("QuickSortCentral", "QuickSortCentral");
graficos.plotarGrafico("QuickSortPrimeiro", "QuickSortPrimeiro");
graficos.plotarGrafico("SelectionSort", "SelectionSort");
graficos.plotarGrafico("ShellSort", "ShellSort"); """

i = sistema.lerArquivo_ou_ordenar()
sistema.leitura_ordenacao(i)
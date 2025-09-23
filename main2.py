import Utils.execucao as execucao
import Utils.graficos as graficos
import Utils.registro as registro

# Cria o arquivo Algorithms.csv com o header
registro.criarArquivo();

# Gera a lista e Escreve as informacoes no CSV
execucao.ordenacao();

graficos.plotarGrafico("QuickSortCentral", "QuickSortCentral");
import Utils.execucao as execucao
import Utils.graficos as graficos
import Utils.registro as registro
import Utils.sistema as sistema
import sys
# aumenta o numero de chamadas recursivas para 200000
sys.setrecursionlimit(200000)

i = sistema.lerArquivo_ou_ordenar()
sistema.leitura_ordenacao(i)
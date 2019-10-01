# coding: utf-8
# Aluno: Paulo Henrique Rodrigues de Matos
# Matricula: 2012070552

#================== Include da função kmedias_nebuloso ========================#
import kmedias_nebuloso as tp1

#====================== Validação do algoritimo ===============================#

# Função para carregar arquivo .mat gerado no Matlab
from scipy.io import loadmat
# Biblioteca para gerar graficos
import matplotlib
matplotlib.use("TkAgg") # Para exibir o grafico em uma janela
import matplotlib.pyplot as plt

dados = loadmat("./Arquivos TP1/fcm_dataset.mat")
pontos = dados['x']

(cents, perts) = tp1.kmedias_nebuloso(pontos = pontos, k = 4,  t = 100)

plt.plot(pontos[:,0], pontos[:,1], 'ro')
plt.show()
plt.plot(pontos[:,0], pontos[:,1], 'ro')
plt.plot(cents[:,0], cents[:,1],'bo')
plt.show()

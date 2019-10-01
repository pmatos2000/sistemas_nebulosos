# coding: utf-8
# Aluno: Paulo Henrique Rodrigues de Matos
# Matricula: 2012070552

#================== Include da função kmedias_nebuloso ========================#
import kmedias_nebuloso as tp1

#=================== Aplicação do algoritimo em imagens =======================#

# Biblioteca para trabalhar com matriz
import numpy as np

# Biblioteca para carregar imagens
from PIL import Image

# Função para carregar imagens
def carrega_image(nome_arquivo) :
    img = Image.open(nome_arquivo)
    img.load()

    #Dimensão da imagem
    l, a = img.size
    data = np.asarray(img, dtype="float").reshape(l*a,3)/255
    return data, l, a

# Função para salvar a imagem
def salva_imagem(nome_arquivo, img):
    img = np.asarray(np.clip(img,0,255), dtype="uint8")
    img = Image.fromarray(img)
    img.save(nome_arquivo)

# Nome da imaagem
nome = "photo011"
# Quantidade de agrupamentos
k = 4

# Executa o algoritimo
pontos, l, a = carrega_image("./Arquivos TP1/ImagensTeste/" + nome + ".png")
(cents, perts) = tp1.kmedias_nebuloso(pontos = pontos, k = k)

# Gera a imagem de sáida
index = perts.argmax(axis=1)
cents = np.round(cents*255)
for i in range(pontos.shape[0]):
    pontos[i] = cents[index[i]]
img = pontos.reshape(a,l,3)

# Salva a imagem
salva_imagem("saida_" + nome + "_k_" + str(k) + "_.png", img)

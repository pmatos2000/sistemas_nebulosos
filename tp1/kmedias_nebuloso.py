# coding: utf-8
# Aluno: Paulo Henrique Rodrigues de Matos
# Matricula: 2012070552

# Biblioteca para calculos matemáticos
import math as mat

#Biblioteca para trabalhar com matriz
import numpy as np

def kmedias_nebuloso(k, pontos, m, t):
    '''
        Descrição:
            Função usado para agrupamentos de pontos usando logica fuzzy

        Utilização:
            kmedias_nebuloso(k, pontos, t)

        Parâmetros:
            k -> Número de agrupamentos
            pontos -> vetor de pontos
            t -> Número de interações
    '''

    # Quantidades de pontos
    m = pontos.shape[0]

    # Dimensão do vetor
    n = pontos.shape[1]

    # Inicia os centroides
    # Seleciona k pontos da lista aleatoriamente
    id = np.random.randint(m, size = k)
    centroides = np.zeros((k,n))
    pertinencia = np.zeros((k,m))

    for i in range(k):
        centroides[i,:] = pontos[id[i], :]


    for i in range(t):
        for j in range(k):

            # Calcula a norma total
            _norma = lambda p : np.linalg.norm(p - centroides[j])

            norma_total = 0;
            for p in pontos:
                norma_total += _norma(p)

            # Função de pertinencia
            def _fp(p):
                norma = _norma(p)
                potencia = mat.floor(2 / (m - 1))
                if(norma == 0):
                    return 1
                return 1/(norma/norma_total) ** potencia



            # Calcula a função de pertinencia
            pertinencia[j,:] = map(_fp, pontos)

            # Atualiza o centroides
            soma_pertiencia = np.sum(pertinencia[j,:] ** m)

            centroides[j,:] = np.zeros(n)
            for l in range(m):
                centroides[j] += pontos[l,:] * pertinencia[j,l] ** m
            centroides[j] /= soma_pertiencia


        print(pertinencia)



    return (centroides, pertinencia)

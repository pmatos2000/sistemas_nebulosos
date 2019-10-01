# coding: utf-8
# Aluno: Paulo Henrique Rodrigues de Matos
# Matricula: 2012070552

# Biblioteca para trabalhar com matriz
import numpy as np

# FUnção para realizar copia de objetos no python
from copy import copy


def kmedias_nebuloso(pontos, k = 2, m = 2, t = 100, e = 1e-4):
    '''
        Descrição:
            Função usado para agrupamentos de pontos usando logica fuzzy

        Utilização:
            kmedias_nebuloso(k, pontos, t)

        Parâmetros:
            k -> Número de agrupamentos
            pontos -> vetor de pontos
            m -> Sensibilidade do fuzzy
            t -> Número de interações
            e -> Criteiro de parada
    '''

    # Quantidades de pontos
    n = pontos.shape[0]

    # Inicia os centroides
    # Seleciona k pontos da lista aleatoriamente
    id = np.random.choice(a = n, size = k, replace=False)
    cents = pontos[id,:]
    ncents = copy(cents)

    # Inicia a matriz de pertinencia
    perts = np.random.rand(n, k)
    perts = perts/perts.sum(axis=1)[:,None]

    for l in range(t):
        for j in range(k):
            # Atualiza centroides
            ncents[j,:] = perts[:,j].dot(pontos)/np.sum(perts[:,j])

        # Condição de saida
        if (np.linalg.norm(ncents - cents) <  e):
            break
        cents = ncents
        ncents = copy(cents)

        # Atualiza matriz de pertinencia
        for j in range(k):
            for i in range(n):
                num = np.sum(np.square(pontos[i,:] - cents[j,:]))
                den = np.sum(np.square(pontos[i,:] - cents))
                perts[i,j] = 1/np.power(num/den, 2/(m-1))
        perts = perts/perts.sum(axis=1)[:,None]


    return ncents, perts

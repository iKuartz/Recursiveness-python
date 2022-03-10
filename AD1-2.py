from itertools import permutations

def cria_listas(limite):
    if limite == 0:
        return []
    elif limite == 1:
        return [1]
    else:
        base = list(range(1,limite+1))*2
        tuples = list(permutations(base))
        listas = list(map(list, tuples))
        return listas

def verifica_condicoes(listas):
    for i in listas:
        for j in len(i):

entrada = int(input("Por favor digite o inteiro a ser verificado"))

todas_listas = cria_listas(entrada)




# # for x in sequencia

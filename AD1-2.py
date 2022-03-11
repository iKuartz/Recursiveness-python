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
    resultados = []
    temporarios = []
    for i in listas:
        for j in range(len(i)):
            if i[j] == i[j+i[j]+1] or i[j] == i[j-i[j]-1]:
                temporarios.append(i[j])
                if j == len(i) and len(temporarios) == len(i):
                    resultados.append(temporarios)
                    temporarios = []
                else:
                    temporarios = []
            else:
                continue

entrada = int(input("Por favor digite o inteiro a ser verificado"))

todas_listas = cria_listas(entrada)




# # for x in sequencia

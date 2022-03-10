from itertools import permutations


entrada = int(input("Por favor digite o inteiro a ser verificado"))

def criaListas(limite):
    tuples = list(permutations(range(1, limite+1)))
    lists = list(map(list, tuples))
    print(lists)
    return lists

criaListas(entrada)


# for x in sequencia

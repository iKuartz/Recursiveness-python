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
            if j+i[j]+1 < len(i) and i[j] == i[j+i[j]+1] or j-i[j]-1 < len(i) and i[j] == i[j-i[j]-1]:
                # A linha acima precisa de algum meio pra verificar que o mesmo número não vá ser colocado duas vezes
                # Ou será necessário verificar dentre os resultados se há listas repetidas e eliminá-las. O segundo parece mais simples.
                temporarios.append(i[j])
                if j == len(i)-1 and len(temporarios) == len(i):
                    resultados.append(temporarios)
                    temporarios = []
                else:
                    pass
            else:
                temporarios = []
                continue
    return resultados

entrada = int(input("Por favor digite o inteiro a ser verificado"))

todas_listas = cria_listas(entrada)

listas_obedecendo_requisitos = verifica_condicoes(todas_listas)

print(listas_obedecendo_requisitos)




# # for x in sequencia

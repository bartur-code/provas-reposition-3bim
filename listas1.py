a = [1, 2, 3, 4, 5, 6]
# len é a funcção que determina a quantidade de elementos que deve ser calculado da lista.
print(len(a))
# ao colocar a lista e o número 0 nos colchetes, está sendo selecionado o primeiro item da lista.
print(a[0])
print(a[4])
# Caso a lista seja enorme (incontável) chama-se a lista com o número -1 nos colchetes, pois sempre será o último termo.
print(a[-1])
s = input()
a.append(s)
print(a)
# Declaração
minha_lista = [1, 2, 3, 4, 5, "rocketseat", True, False]
lista = [10, 90, 6, 56, 38]

# Exibindo a lista
print("Minhas lista de de exemplo", minha_lista)

# Exibindo os elementos
minha_lista[0] = "python"
print("Minhas lista de de exemplo", minha_lista)

print("minha_lista[0]:",minha_lista[0])
print("minha_lista[5]:",minha_lista[5])
print("minha_lista[1:7]:", minha_lista[1:7])
print("minha_lista[:5]:", minha_lista[:6])
print("minha_lista[2:]:", minha_lista[2:])

# Metodos de lista

# Metodo append(): Adiciona uma elemento no final da lista
minha_lista.append(6)
print("Após append(6):", minha_lista)

# Metodo index: retorna o indice do primeiro elemento indicado
indice = minha_lista.index(6);
print("Indice do elemento 6:", indice)

# Metodo insert: inseri um elemnto em um indice especifico
minha_lista.insert(2, 10)
print("Após o insert(2, 10):", minha_lista)

# Metodo pop: remove e retorna o elemento de indice especifico
elemento_removido = minha_lista.pop(3)
print("Elemento removido:", elemento_removido)
print("Após o pop(3):", minha_lista)

# Metodo remove: remove oo primeiro elemento com o valor especificado
minha_lista.remove(True)
print("Após remove(True):", minha_lista)

# Metodo sort: organiza os elemento em ordem crescente, todos os elemento precisa ser números
lista. sort()
print("Após sort():", lista)
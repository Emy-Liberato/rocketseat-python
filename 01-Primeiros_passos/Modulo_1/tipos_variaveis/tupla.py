# é uma coleção ordenada e imutavel de elemento

# Criando uma tupla de exemplo
minha_tupla = (1, 2, 2, 3, 4)

print("Minha tupla:", minha_tupla)

print('minha_tupla[0]',minha_tupla[0])
print('minha_tupla[2]',minha_tupla[2])
print('minha_tupla[-1]',minha_tupla[-1]) #mostra o ultimo elemento

#Metodo count
contagem = minha_tupla.count(2)
print("Quantidade de vezes que o elemento 2 aparece:", contagem)

indice = minha_tupla.index(3)
print("Indice da primeira ocorência do elemento 3:", indice)
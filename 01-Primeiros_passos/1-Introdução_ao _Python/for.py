#Lop - continuar fazendo a ação até que ela serja verdadeira

print("For utilizando lista")
lista = [1, 2, 3, 4, 5]
for elemento in lista:
  print(elemento)

print("For utilizando tupla")
tupla = (1, 2, 3, 4, 5)
for elemento in tupla:
  print(elemento)

pessoa = {"nome": "João", "Idade": 30, "cidade":"São Paulo"}
print("For utilizando dicionário - chaves")
for chave in pessoa.keys():
  print(chave)

print("\n For utilizando dicionário - valores")
for valor in pessoa.values():
  print(valor)

print("\n For utilizando dicionário - chave-valor")
for chave, valor in pessoa.items():
  print(f"{chave}: {valor}")

# range(): intervalo númerico em formato de lista
print("\n Utilizando a função range()")
for numero in range(5):
  print("Número:", numero)

print("\n Utilizando a função range() com len()")
print(lista)
for indice in range(0, len(lista)):
  print("Indice:", indice)
  print("Elemento:", lista[indice])
  if indice == 3:
    lista[indice] = 5
  else:
    lista[indice] = 0
print(lista)

# enumerate()
lista_enumerate = ["a", "b", "c"]
for indice, valor in enumerate(lista_enumerate):
  print(f"{indice}:{valor}")
  if indice == 1:
   print("indice = 1")
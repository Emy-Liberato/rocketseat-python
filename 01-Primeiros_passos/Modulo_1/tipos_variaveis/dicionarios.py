# Coleção não ordenada de pares, chaves e valores

# Criando um dicionário de exemplo
pessoa = {"nome": "João", "idade": 30, "cidade": "Sâo Paulo"}

# Exibindo o dicionário
print("Meu dicioário de exemplo:", pessoa)

#Acessando os valores por chave
print("Nome:", pessoa["nome"])
print("Idade:", pessoa["idade"])
print("Cidade:", pessoa["cidade"])

# Adicionando um novo elemento após a criação do dicionário, como valor conseguimos colocar até outro dicionário, lista e tupla
pessoa["sobrenome"] = "Silva"
print("Sobrenome:", pessoa["sobrenome"])
print("Meu dicioário de exemplo:", pessoa)

#atualizar um valor já existente
pessoa["idade"] = 31
print("Idade atualizada:", pessoa["idade"])

# Removendo um par de chave-valor
del pessoa["sobrenome"]
print("Meu dicioário de exemplo:", pessoa)

# Metodos: keys(), values(), itens()
chaves = list(pessoa.keys()) #precisamos transformar em lista para acessar o indice de um elemento
print("Chave do dicionário", chaves)
print("Primeira chave:", chaves[0])

# Metodo values
valores = list(pessoa.values())
print("Valores do dicionário:", valores)
print("Primeiro valor do dicionário:", valores[0])

# Metodos items
itens = list(pessoa.items())
print("Pares chaves-valores do dicionário:", itens)
print("Primeira chave-valor: %s = %s:" % (itens[0][0], itens[0][1])) #primeiro selecionasmos o indice do das tuplas, e depois o elemento dentro dela
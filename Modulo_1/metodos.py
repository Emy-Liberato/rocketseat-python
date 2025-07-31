nome = "Emilly"
sobrenome = "Liberato"
nome_completo = "Emilly Liberato"
telefone = "(19)97325-0502"
nome_x = "xEmilly Liberatox"

#esse metodo não muda o valor da variavel
# --------------------------------------------------------------
#METODOS
# --------------------------------------------------------------

#UPPER
#coloca a string em maisculo
print(nome.upper()) 

#LOWER
#coloca a string em minusculo
print(nome.lower()) 

#[] - indice
#pega a letra que esta no indice indentificado dentro do []
print(nome[0]) 

#COUNT
#conta a quanridade de letras, podendo passar um parametro para procurar um valor específico
print(nome_completo.count("e")) 

#FIND
#procura quais são as posições 
print(nome.find("i"))

#ENCODE
#converte a string 'nome' para bytes (codificação padrão é UTF-8)
print(nome.encode()) 

#DECODE
#converte os bytes de volta para string (decodifica).
print(nome.encode().decode()) 

#REPLACE
#substitui um elemento por outro, passamos dois argumentos, 1 o que será substituido, 2 o que vai substituir
print(nome_completo.replace("m", "a")) 
print(telefone.replace("(", "").replace(")", "").replace("-", ""))

#JOIN
#usada para separar o elemento com o separador desejado
print("-".join(nome))

#SPLIT
#converter string em listas, com base em caracter algo, o padrão de separação já é o espaço 
print(nome_completo.split(" "))
print(nome_completo.split())

#STRIP
#tira caracteres especificos do que esta no começo ou no final
print(nome_x.strip("x"))
print(nome_x.rstrip("x")) #apenas ao que esta na direita

# --------------------------------------------------------------
# COMPARADORES
# --------------------------------------------------------------

#STARTWITH
#verifica se a string começa com o elemento, devolve um boleano
print(nome_completo.startswith("El"))

#IN
#se o termo existe dentro da variavel que queremos comparar
print("abc" in nome_completo)

#NOT IN
#verifica se o termo NÃo existe na variavel
print("abc" not in nome_completo)
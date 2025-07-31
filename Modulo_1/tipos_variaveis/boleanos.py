#Condições verdadeiras
True

#Condições Falsa
False

#Condicionais

if True:
  print("Bloco If vai ser executado")
else:
  print("Bloco ELSE não será excutado")

#Operadores lógicos: and e or

#AND - só executa se as duas condições forem verdadeiras
if True and True:
  print("Bloco será executado")

if True and False:
  print("Bloco não será executado")

if False and False:
  print("Bloco não será executado")

#OR - Se uma condição foi verdadeira
if True or False:
  print("Bloco OR vai ser executado")

if False or False:
  print("Bloco OR não será executado")

if True or False:
  print("Bloco OR vai ser executado")
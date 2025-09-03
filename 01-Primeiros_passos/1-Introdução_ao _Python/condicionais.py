#  if, elif e else

# exemplo de if 
idade = int(input("Quanto anos você tem?"))
print("Exemplo de comando if")

if idade >= 18:
  print("Você é maior de idade.")
elif idade >= 12:
  print("Você é um adolescentes")
else:
  print("Você é menor de idade.")

mensagem = "Pode tirar a carteira de habilitação" if idade >= 18 else "Você não pode tira a carteira de habilitação"

print(mensagem)
# é um bloco de código reutilizavel que executa uma tarefa especifica toda vez que é chamado

# Exemplo
def saudacao(nome):
  print(f"Olá, {nome}!")

print("\n Chamando a função saudação:")
saudacao("Alice")
saudacao("Bob")

# Função com retorno
def quadradro(numero):
  resultado = numero ** 2
  return resultado

print("\nChamando função quadrado:")
resultado_quadradro = quadradro(5)
print("Resultado da função quadrado:", resultado_quadradro)

# Função com multiplos parametros
def soma(numero1, numero2):
  resultado = (numero1 + numero2)
  return resultado

print("\nChamando a função soma:")
numero1 = 25
numero2 = 30
resultado_soma = soma(numero1, numero2)
print("A soma do numero %s e numero %s é %s" % (numero1, numero2, resultado_soma))
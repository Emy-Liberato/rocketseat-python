print("Exemplo de importação de um módulo padrão:")
# import math 
# imporantando o modulo inteiro 

# importando apenas a função que estamos utlizando no código
from math import sqrt

raiz_quadrada = sqrt(25)
print(f"A raiz quedrada de 25 é {raiz_quadrada}")

print("\nExemplo de criação e utlizando de um módulo personalizado")
from meu_modulo import saudacao, dobro

mensagem = saudacao("Emilly")
resultado_dobro = dobro(5)
print(mensagem)
print(f"O dobro de 5 é {resultado_dobro}")
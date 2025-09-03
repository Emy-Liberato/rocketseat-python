# Declaração
nome_completo = "Emilly Liberato"

nome_completo_aspas = """Emilly
Liberato"""

nome_completo_quebra = "Emilly \
Liberato"

nome = "Emilly"
sobrenome = "Liberato"

#Formatação
print("Nome completo (1a forma):", nome_completo)
print("Nome completo (2a forma):" + nome_completo) 
print("Nome completo (3a forma):" + "Emilly" + "Liberato") 
print("Nome completo (4a forma):" + " Emilly", "Liberato") 
print("Nome completo (5a forma):", nome_completo_aspas) 
print("Nome completo (6a forma):", nome_completo_quebra) 
print("Nome completo (7a forma): %s" % nome_completo) 
print("Nome completo (8a forma): %s %s" % (nome, sobrenome)) #transforma as variaveis em string
print(f"Nome completo (9a forma): {nome} {sobrenome}" ) 
print("Nome completo (10a forma): {} {}".format(sobrenome, nome) ) 
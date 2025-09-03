#função adicionar contato na lista
def adicionar_contato(lista_contatos, nome, telefone, email):
    contato = {
        "Nome": nome, "Telefone": telefone, "E-mail": email, "Favorito": False
    }
    lista_contatos.append(contato)
    print(f"\ncontato {nome}, foi adicionado com sucesso.")

#função de vizualizar contato
def ver_contatos(lista_contatos):
    print("\nLista de contatos")
    for indice, contato in enumerate(lista_contatos, start=1):
        favorito = "❤️" if contato["Favorito"] else "  "
        nome = contato["Nome"]
        telefone = contato["Telefone"]
        email = contato["E-mail"]
        print(f"{indice}. [{favorito}] Nome: {nome}, Telefone: {telefone}, E-mail: {email} ")
    return

#função para editar contatos
def editar_contato(lista_contatos, indice_contato, nome, telefone, email):
    if 0 <= indice_contato < len(lista_contatos):
        lista_contatos[indice_contato]["Nome"] = nome
        lista_contatos[indice_contato]["Telefone"] = telefone
        lista_contatos[indice_contato]["E-mail"] = email
        print(f"Contato {indice_contato + 1} editado com sucesso!")
    else:
        print("Índice de contato inválido!")
    return

# função para favoritar contatos
def favoritar_contato(lista_contatos, indice_contato):
    if 0 <= indice_contato < len(lista_contatos):
        lista_contatos[indice_contato]["Favorito"] = True
        nome = lista_contatos[indice_contato]["Nome"]
        print(f"Contato '{nome}' foi favoritado com sucesso!")
    else:
        print("Índice de contato inválido!")
    return

# função para desfavoritar contatos
def desfavoritar_contato(lista_contatos, indice_contato):
    if 0 <= indice_contato < len(lista_contatos):
        lista_contatos[indice_contato]["Favorito"] = False
        nome = lista_contatos[indice_contato]["Nome"]
        print(f"Contato '{nome}' foi desfavoritado, e não estará mais na sua lista de favoritos")
    else:
        print("Esse contato não esta favoritado")
    return

#função para vizualizar lista de favoritos
def ver_lista_favoritados(lista_contatos):
    print("\n---Contatos favoritos---")
    encontrou_favorito = False
    for indice, contato in enumerate(lista_contatos, start=1):
        if contato["Favorito"]:
            encontrou_favorito = True
            nome = contato["Nome"]
            telefone = contato["Telefone"]
            email = contato["E-mail"]
            print(f"{indice}. [❤️] Nome: {nome}, Telefone: {telefone}, E-mail: {email}")
    return

def excluir_contato(lista_contatos, indice_contato):
    contato = lista_contatos[indice_contato]
    lista_contatos.remove(contato)
    print(f"Contato '{contato['Nome']}' foi excluído com sucesso!")

#lista com todos os contatos
lista_contatos = []

while True:
    print("\n----Menu de Contatos----")
    print("1 - Adicionar um contato")
    print("2 - Visualizar sua lista de contatos")
    print("3 - Editar um contato")
    print("4 - Favoritar um contato")
    print("5 - Desfavoritar um contato")
    print("6 - Visualizar contatos favoritados")
    print("7 - Excluir um contato")
    print("8 - Sair")

    escolha = input("Digite a sua escolha: ")

    if escolha == "1":
        print("Informe os dados do contato que deseja adicionar:")
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        email = input("E-mail:")

        adicionar_contato(lista_contatos, nome, telefone, email)

    elif escolha == "2":
        ver_contatos(lista_contatos)

    elif escolha == "3":
        ver_contatos(lista_contatos)
        indice_contato = int(input("Digite o índice do contato que deseja editar: ")) - 1
        novo_nome = input("Digite o novo Nome: ")
        novo_email = input("Digite o novo E-mail: ")
        novo_telefone = input("Digite o novo Telefone: ")
        editar_contato(lista_contatos, indice_contato, novo_nome, novo_telefone, novo_email)

    elif escolha == "4":
        ver_contatos(lista_contatos)
        indice_contato = int(input("Infome o indice do contato que deseja favoritar: ")) - 1
        favoritar_contato(lista_contatos, indice_contato)

    elif escolha == "5":
        ver_lista_favoritados(lista_contatos)
        indice_contato = int(input("Informe o indice do contato que deseja desfavoritar: ")) - 1
        desfavoritar_contato(lista_contatos, indice_contato)

    elif escolha == "6":
        ver_lista_favoritados(lista_contatos)

    elif escolha == "7":
        ver_contatos(lista_contatos)
        indice_contato = int(input("Informe o índice do contato que deseja excluir: ")) - 1
        excluir_contato(lista_contatos, indice_contato)

    elif escolha == "8":
        break

print("Programa finalizado!")
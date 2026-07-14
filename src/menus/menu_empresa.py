from crud.empresa import (
    cadastrar_empresa,
    listar_empresa,
    buscar_empresa,
    atualizar_empresa,
    remover_empresa
)


def menu_empresa():

    while True:

        print("\n===== EMPRESAS =====")
        print("1 - Cadastrar empresa")
        print("2 - Listar empresas")
        print("3 - Buscar empresa")
        print("4 - Atualizar empresa")
        print("5 - Remover empresa")
        print("0 - Voltar")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            cadastrar_empresa()

        elif opcao == "2":
            listar_empresa()

        elif opcao == "3":
            buscar_empresa()

        elif opcao == "4":
            atualizar_empresa()

        elif opcao == "5":
            remover_empresa()

        elif opcao == "0":
            break

        else:
            print("\nOpção inválida.")
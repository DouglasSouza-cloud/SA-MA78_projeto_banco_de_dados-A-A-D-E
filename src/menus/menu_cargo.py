from crud.cargo import (
    cadastrar_cargo,
    listar_cargo,
    buscar_cargo,
    atualizar_cargo,
    remover_cargo
)


def menu_cargo():

    while True:

        print("\n========================================")
        print("            MENU CARGOS")
        print("========================================")
        print("1 - Cadastrar Cargo")
        print("2 - Listar Cargos")
        print("3 - Buscar Cargo")
        print("4 - Atualizar Cargo")
        print("5 - Remover Cargo")
        print("0 - Voltar")
        print("========================================")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":

            cadastrar_cargo()

        elif opcao == "2":

            listar_cargo()

        elif opcao == "3":

            buscar_cargo()

        elif opcao == "4":

            atualizar_cargo()

        elif opcao == "5":

            remover_cargo()

        elif opcao == "0":

            print("\nRetornando ao menu principal...")
            break

        else:

            print("\nOpção inválida! Tente novamente.")
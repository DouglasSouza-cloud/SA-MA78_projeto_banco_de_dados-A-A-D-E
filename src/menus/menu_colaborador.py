from crud.colaborador import (
    cadastrar_colaborador,
    listar_colaborador,
    buscar_colaborador,
    atualizar_colaborador,
    remover_colaborador
)


def menu_colaborador():

    while True:

        print("\n========================================")
        print("         MENU COLABORADORES")
        print("========================================")
        print("1 - Cadastrar Colaborador")
        print("2 - Listar Colaboradores")
        print("3 - Buscar Colaborador")
        print("4 - Atualizar Colaborador")
        print("5 - Remover Colaborador")
        print("0 - Voltar")
        print("========================================")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":

            cadastrar_colaborador()

        elif opcao == "2":

            listar_colaborador()

        elif opcao == "3":

            buscar_colaborador()

        elif opcao == "4":

            atualizar_colaborador()

        elif opcao == "5":

            remover_colaborador()

        elif opcao == "0":

            print("\nRetornando ao menu principal...")
            break

        else:

            print("\nOpção inválida! Tente novamente.")
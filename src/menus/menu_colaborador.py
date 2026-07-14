from crud.colaborador import (
    cadastrar_colaborador,
    listar_colaborador,
    buscar_colaborador,
    atualizar_colaborador,
    remover_colaborador
)


def menu_colaborador():

    while True:

        print("\n===== COLABORADORES =====")
        print("1 - Cadastrar")
        print("2 - Listar")
        print("3 - Buscar")
        print("4 - Atualizar")
        print("5 - Remover")
        print("0 - Voltar")

        opcao = input("Escolha: ")

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
            break

        else:
            print("Opção inválida.")
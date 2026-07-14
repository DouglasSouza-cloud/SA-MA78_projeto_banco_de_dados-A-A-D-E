from menus.menu_cargo import menu_cargo
from menus.menu_colaborador import menu_colaborador

while True:

    print("\n========================================")
    print("       INOVE CONTABILIDADE")
    print("========================================")
    print("1 - Cargos")
    print("2 - Colaboradores")
    print("0 - Sair")
    print("========================================")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":

        menu_cargo()

    elif opcao == "2":

        menu_colaborador()

    elif opcao == "0":

        print("\nEncerrando o sistema...")
        break
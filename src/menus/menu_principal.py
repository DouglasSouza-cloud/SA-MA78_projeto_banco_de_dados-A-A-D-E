from menus.menu_inicial import menu_inove_colorido
from menus.menu_cargo import menu_cargo
from menus.menu_colaborador import menu_colaborador
from menus.menu_imposto import menu_imposto


def menu_principal():

    while True:

        opcao = menu_inove_colorido()


        if opcao == "1":

            menu_cargo()


        elif opcao == "2":

            menu_colaborador()


        elif opcao == "3":

            menu_imposto()


        elif opcao == "0":

            print("\nEncerrando o sistema...")
            break


        else:

            print("\nOpção inválida!")
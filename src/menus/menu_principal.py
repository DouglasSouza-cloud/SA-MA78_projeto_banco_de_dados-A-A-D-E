from menus.menu_inicial import menu_inove_colorido

from menus.menu_rh import menu_rh
from menus.menu_empresas import menu_empresas

from menus.menu_fiscal import menu_fiscal


def menu_principal():

    while True:

        opcao = menu_inove_colorido()

        if opcao == "1":

            menu_rh()

        elif opcao == "2":

            menu_empresas()

        elif opcao == "3":

            menu_fiscal()

        elif opcao == "0":

            print("\nEncerrando o sistema...")
            break

        else:

            print("\nOpção inválida!")
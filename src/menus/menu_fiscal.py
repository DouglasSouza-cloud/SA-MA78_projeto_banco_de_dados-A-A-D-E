from menus.menu_imposto import menu_imposto


# futuramente você vai criar esses:
# from menus.menu_documento_fiscal import menu_documento_fiscal
# from menus.menu_cronograma_tributario import menu_cronograma_tributario
# from menus.menu_guia_pagamento import menu_guia_pagamento


def menu_fiscal():

    while True:

        print("\n========================================")
        print("              MENU FISCAL")
        print("========================================")
        print("1 - Gerenciar Impostos")
        print("2 - Gerenciar Documentos Fiscais")
        print("3 - Gerenciar Cronograma Tributário")
        print("4 - Gerenciar Guias de Pagamento")
        print("0 - Voltar")
        print("========================================")

        opcao = input("Escolha uma opção: ")


        if opcao == "1":

            menu_imposto()


        elif opcao == "2":

            print("\nMenu de documentos fiscais ainda não criado.")


        elif opcao == "3":

            print("\nMenu de cronograma tributário ainda não criado.")


        elif opcao == "4":

            print("\nMenu de guias de pagamento ainda não criado.")


        elif opcao == "0":

            print("\nRetornando ao menu principal...")
            break


        else:

            print("\nOpção inválida! Tente novamente.")
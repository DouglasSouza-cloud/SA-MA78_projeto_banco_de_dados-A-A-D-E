from util.cores import (
    AZUL_CLARO,
    VERDE,
    AMARELO,
    VERMELHO,
    NEGRITO,
    RESET
)

from menus.menu_empresa import menu_empresa


def menu_empresas():

    while True:

        print(f"{AZUL_CLARO}╭────────────────────────────────────────────╮{RESET}")
        print(f"{AZUL_CLARO}│{RESET} {NEGRITO}{VERDE}          MÓDULO EMPRESAS{RESET}                {AZUL_CLARO}│{RESET}")
        print(f"{AZUL_CLARO}├────────────────────────────────────────────┤{RESET}")
        print(f"{AZUL_CLARO}│{RESET}                                            {AZUL_CLARO}│{RESET}")
        print(f"{AZUL_CLARO}│{RESET}   {AMARELO}[ 1 ]{RESET} - Empresas                        {AZUL_CLARO}│{RESET}")
        print(f"{AZUL_CLARO}│{RESET}   {AMARELO}[ 2 ]{RESET} - Contatos                        {AZUL_CLARO}│{RESET}")
        print(f"{AZUL_CLARO}│{RESET}   {AMARELO}[ 3 ]{RESET} - Sócios                          {AZUL_CLARO}│{RESET}")
        print(f"{AZUL_CLARO}│{RESET}   {AMARELO}[ 4 ]{RESET} - Certificados Digitais           {AZUL_CLARO}│{RESET}")
        print(f"{AZUL_CLARO}│{RESET}                                            {AZUL_CLARO}│{RESET}")
        print(f"{AZUL_CLARO}│{RESET}   {VERMELHO}[ 0 ]{RESET} - Voltar                          {AZUL_CLARO}│{RESET}")
        print(f"{AZUL_CLARO}│{RESET}                                            {AZUL_CLARO}│{RESET}")
        print(f"{AZUL_CLARO}╰────────────────────────────────────────────╯{RESET}")

        opcao = input(f" {NEGRITO}➤ Escolha uma opção:{RESET} ")

        if opcao == "1":

            menu_empresa()

        elif opcao == "2":

            print("\nMódulo em desenvolvimento.")

        elif opcao == "3":

            print("\nMódulo em desenvolvimento.")

        elif opcao == "4":

            print("\nMódulo em desenvolvimento.")

        elif opcao == "0":

            break

        else:

            print("\nOpção inválida!")
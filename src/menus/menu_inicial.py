def menu_inove_colorido():
    # Códigos de cor ANSI
    AZUL_CLARO = '\033[94m'
    VERDE = '\033[92m'
    AMARELO = '\033[93m'
    VERMELHO = '\033[91m'
    NEGRITO = '\033[1m'
    RESET = '\033[0m' # Volta para a cor padrão do terminal

    print(f"{AZUL_CLARO}╭────────────────────────────────────────────╮{RESET}")
    print(f"{AZUL_CLARO}│{RESET} {NEGRITO}{VERDE}          INOVE CONTABILIDADE{RESET}               {AZUL_CLARO}│{RESET}")
    print(f"{AZUL_CLARO}├────────────────────────────────────────────┤{RESET}")
    print(f"{AZUL_CLARO}│{RESET}                                            {AZUL_CLARO}│{RESET}")
    print(f"{AZUL_CLARO}│{RESET}   {AMARELO}[ 1 ]{RESET} - Cargos                           {AZUL_CLARO}│{RESET}")
    print(f"{AZUL_CLARO}│{RESET}   {AMARELO}[ 2 ]{RESET} - Colaboradores                    {AZUL_CLARO}│{RESET}")
    print(f"{AZUL_CLARO}│{RESET}   {VERMELHO}[ 0 ]{RESET} - Sair                             {AZUL_CLARO}│{RESET}")
    print(f"{AZUL_CLARO}│{RESET}                                            {AZUL_CLARO}│{RESET}")
    print(f"{AZUL_CLARO}╰────────────────────────────────────────────╯{RESET}")
    
    opcao = input(f" {NEGRITO}➤ Escolha uma opção:{RESET} ")
    return opcao
from menus.menu_colaborador import menu_colaborador
from menus.menu_empresa import menu_empresa

while True:

    print("\n===== INOVE CONTABILIDADE =====")
    print("1 - Colaboradores")
    print("2 - Empresas")
    print("0 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        menu_colaborador()   # <-- chama o menu

    elif opcao == "2":
        menu_empresa()

    elif opcao == "0":
        break
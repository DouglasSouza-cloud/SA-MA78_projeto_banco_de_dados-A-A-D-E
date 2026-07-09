from colaborador import(
listar_colaborador)

while True:

    print("\n====== SISTEMA INDUSTRIAL ======")
    print("1 - Listar colaboradores")
    print("2 - Cadastrar colaborador")
    print("3 - Atualizar salário")
    print("4 - Remover colaborador")
    print("0 - Sair")

    opcao=input("\nEscolha uma opção: ")
    # listar
    if opcao == "1":
        listar_colaborador()
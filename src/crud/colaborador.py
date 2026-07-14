from database import conectar

def cadastrar_colaborador():
    conexao = conectar()
    cursor = conexao.cursor()

    nome = input("Nome: ")
    cpf = input("CPF: ")
    email = input("Email: ")
    telefone = input("Telefone: ")
    salario = float(input("Salário: "))
    id_cargo = int(input("ID do Cargo: "))

    sql = """
        INSERT INTO colaborador
        (nome_colaborador,
         cpf_colaborador,
         email_colaborador,
         telefone_colaborador,
         salario,
         id_cargo)
        VALUES (%s,%s,%s,%s,%s,%s)
    """

    valores = (
        nome,
        cpf,
        email,
        telefone,
        salario,
        id_cargo
    )

    cursor.execute(sql, valores)
    conexao.commit()

    print("\nColaborador cadastrado com sucesso!")

    cursor.close()
    conexao.close()


def listar_colaborador():

    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
        SELECT
            id_colaborador,
            nome_colaborador,
            cpf_colaborador,
            email_colaborador,
            telefone_colaborador,
            salario,
            id_cargo
        FROM colaborador
        ORDER BY nome_colaborador
    """

    cursor.execute(sql)

    colaboradores = cursor.fetchall()

    if len(colaboradores) == 0:
        print("\nNenhum colaborador encontrado.")

    else:

        print("\n===== COLABORADORES =====")

        for colaborador in colaboradores:

            print(f"""
                    ID........: {colaborador[0]}
                    Nome......: {colaborador[1]}
                    CPF.......: {colaborador[2]}
                    Email.....: {colaborador[3]}
                    Telefone..: {colaborador[4]}
                    Salário...: R$ {colaborador[5]:.2f}
                    Cargo ID..: {colaborador[6]}
                """)

    cursor.close()
    conexao.close()

def buscar_colaborador():

    conexao = conectar()
    cursor = conexao.cursor()

    id_colaborador = int(input("Informe o ID: "))

    sql = """
        SELECT *
        FROM colaborador
        WHERE id_colaborador = %s
    """

    cursor.execute(sql, (id_colaborador,))

    colaborador = cursor.fetchone()

    if colaborador:
        print(colaborador)
    else:
        print("\nColaborador não encontrado.")

    cursor.close()
    conexao.close()

def atualizar_colaborador():

    conexao = conectar()
    cursor = conexao.cursor()

    id_colaborador = int(input("ID do colaborador: "))
    novo_salario = float(input("Novo salário: "))

    sql = """
        UPDATE colaborador
        SET salario = %s
        WHERE id_colaborador = %s
    """

    cursor.execute(sql, (novo_salario, id_colaborador))
    conexao.commit()

    print("\nSalário atualizado com sucesso!")

    cursor.close()
    conexao.close() 

def remover_colaborador():

    conexao = conectar()
    cursor = conexao.cursor()

    id_colaborador = int(input("ID do colaborador: "))

    sql = """
        DELETE FROM colaborador
        WHERE id_colaborador = %s
    """

    cursor.execute(sql, (id_colaborador,))
    conexao.commit()

    print("\nColaborador removido com sucesso!")

    cursor.close()
    conexao.close()
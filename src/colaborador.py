from database import conectar

def listar_colaborador():
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
        SELECT
            c.nome_colaborador,
            c.cpf_colaborador
        FROM colaborador c
    """

    cursor.execute(sql)
    dados = cursor.fetchall()

    cursor.close()
    conexao.close()

    return dados


from database import conectar

def listar_colaborador():
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
        SELECT
            nome_colaborador,
            cpf_colaborador
        FROM colaborador
    """

    cursor.execute(sql)
    dados = cursor.fetchall()

    cursor.close()
    conexao.close()

    return dados


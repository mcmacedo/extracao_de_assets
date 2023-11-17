from sqlalchemy import create_engine, text


def create_connection(config):
    """
    Realiza a conexão com o banco de dados

    Params:
        config: dict com os parâmetros definidos por environment

    Returns: engine (objeto de conexão)
    """
    engine = create_engine(config['engine_str'])
    
    print("Conexão realizada com sucesso")
    return engine.connect()


def create_ativos_table(engine):
    """
    Cria a tabela ativos
    """
    engine.execute(text("CREATE TABLE IF NOT EXISTS ativos (id INT AUTO_INCREMENT PRIMARY KEY, asset_id VARCHAR(255), gross_revenue INT, label VARCHAR(255));"))



def buscar_ativos_por_label(engine, label):
    """
    Busca os ativos por label

    Returns: result (list de ativos filtrados por label)
    """
    result = engine.execute(text(f"SELECT * FROM ativos WHERE label = {label};"))
    return result.fetchall()


def extrair_ativos(engine):
    """
    Busca todos os ativos do banco

    Returns: ativos (list de ativos)
    """
    ativos_descritos = engine.execute(text("SELECT * FROM ativos;"))

    return ativos_descritos.fetchall()

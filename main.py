from database import create_connection, create_ativos_table
from environ import get_argv_config, get_env_config


def parse_ativos_to_dicts_list(conexao, busca_ativos):
    ativos = busca_ativos(conexao)
    ativos_tratados = []
    
    for ativo in ativos:
        ativo_tratado = {
            "id": ativo[0],
            "asset_id": ativo[1],
            "gross_revenue": ativo[2],
            "label": ativo[3]
        }
        ativos_tratados.append(ativo_tratado)

    return ativos_tratados


def calcula_taxa_de_cambio(ativo):
    # Calcula a taxa de cambio
    cambio = ativo["gross_revenue"] = ativo["gross_revenue"] * 5.5
    return cambio


if __name__ == "__main__":
    conexao = None

    try:
        environment = get_argv_config()
        config = get_env_config(environment)
        conexao = create_connection(config)
        create_ativos_table(conexao)
        ativos_tratados = parse_ativos_to_dicts_list(conexao, config['ativos_src'])
        
        for ativo in ativos_tratados:
            cambio = calcula_taxa_de_cambio(ativo)
            print(cambio)
    except Exception as err:
        print(f"Err no sistema - {err}")
    finally:
        if conexao:
            conexao.close()
            print("Conexão fechada com sucesso")


# S.O.L.I.D.
# S - Single Responsability Principle = Uma função ou classe deve ter apenas uma responsabilidade
# O - Open Closed Principle = Uma função ou classe deve estar aberta para extensão, mas fechada para modificação
# L - Liskov Substitution Principle (DEPOIS)
# I - Interface Segregation Principle (DEPOIS)
# D - Dependency Inversion Principle = Sua funções ou classes devem depender de interfaces, não de implementações
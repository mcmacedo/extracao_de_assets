def connect(string_de_conexao):
    print(string_de_conexao)

db_host="localhost"
db_user="root"
db_password="root123"
db_name="extracao_de_assets"
db_port=3306


def extrair_ativos():
    # Extrai os ativos da tabela ativos
    ativos = [
        {
            "id": 1,
            "name": "Petrobras",
            "gross_revenue": 1000000
        },
        {
            "id": 2,
            "name": "Vale",
            "gross_revenue": 2000000
        },
        {
            "id": 3,
            "name": "Itau",
            "gross_revenue": 3000000
        },
        {
            "id": 4,
            "name": "Banco do Brasil",
            "gross_revenue": 4000000
        },
        {
            "id": 5,
            "name": "Bradesco",
            "gross_revenue": 5000000
        },
    ]
    return ativos


def calcula_taxa_de_cambio(asset):
    # Calcula a taxa de cambio
    cambio = asset["gross_revenue"] = asset["gross_revenue"] * 5.5
    return cambio


if __name__ == "__main__":
    conexao = connect(f"{db_host}, {db_user}, {db_password}, {db_name}, {db_port}")
    ativos = extrair_ativos()

    for asset in ativos:
        cambio = calcula_taxa_de_cambio(asset)
        print(cambio)
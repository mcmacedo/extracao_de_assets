import json


def extrair_arquivos_json(engine):
    ativos = []
    file = open('ativos.json')
    data = json.load(file)

    for ativo in data:
        ativos.append(tuple(ativo.values()))

    file.close()

    return ativos

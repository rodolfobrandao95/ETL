import json
import pandas as pd
import requests as r


def consume_api(year, month, state_code, city_code, save_directory):
    uri = 'http://www.transparencia.gov.br/api-de-dados/bolsa-familia-por-municipio/?mesAno={}&codigoIbge={}&pagina=1'.format(
        (year+month), (state_code+city_code))
    response = r.get(uri)

    if response.status_code == 200:
        with open(save_directory, mode='w', encoding='utf-8') as output:
            temp = json.loads(response.text)
            json.dump(temp, output, ensure_ascii=False)

    return response.status_code


def read_xls(file_directory, columns=[]):
    df = pd.read_excel(file_directory)

    if len(columns) > 0:
        df = [df[col] for col in columns]

    return df

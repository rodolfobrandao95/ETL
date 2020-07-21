import csv
import json
import requests as r


def set_date_range(year_range: tuple, month_range: tuple) -> list:
    '''
    Returns a list with year and month format as YYYYMM.
    '''

    dates = []
    for year in range(year_range[0], year_range[1] - 1):
        for month in range(month_range[0], month_range[1] - 1):
            dates.append(
                '{}0{}'.format(year, month) if month <= 9 else '{}{}'.format(year, month))

    return dates


def set_ibge_codes(file_path: str, column_value='') -> list:
    '''
    Reads a .csv file, and filters by column value, and returns
    a list with the IBGE codes in the API's endpoint format.
    Optional keywords arguments: column_value: value of the column to be filtered.
    '''

    ibge_codes = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        filtered = list(filter(lambda x: column_value in x, spamreader)
                        ) if column_value != '' else list(spamreader)

        for arr in filtered:
            ibge_codes.append('{}{}'.format(arr[1], arr[2]))

    return ibge_codes


def gather_data(dates: list, ibge_codes: list, save_path: str) -> None:
    '''
    Collects data from the API, by passing the dates and IBGE codes
    formatted, and saves a JSON file in the specified path.
    '''

    uris = []
    returned_json = []

    for code in ibge_codes:
        for date in dates:
            uris.append(
                'http://www.transparencia.gov.br/api-de-dados/bolsa-familia-por-municipio/?mesAno={}&codigoIbge={}&pagina=1'.format(
                    date, code
                ))

    for uri in uris:
        try:
            response = r.get(uri)
            if response.status_code == 200 and response.json():
                returned_json.append(response.json()[0])
        except ValueError:
            print('ValueError exception for: {}'.format(uri))
        except Exception as e:
            blocked = True
            while blocked:
                response = r.get(uri)
                blocked = False

            print(repr(e))

    with open(save_path, 'w+', encoding='utf-8') as jsonfile:
        all_json = json.dumps(returned_json, indent=4, ensure_ascii=False)
        jsonfile.write(all_json)

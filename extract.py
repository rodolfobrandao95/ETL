import csv
import json
import multiprocessing as m
import requests as r


def get_date_range(year_range, month_range):
    dates = []

    for i in range(year_range[0], year_range[1]):
        for j in range(month_range[0], month_range[1]):
            dates.append(
                '{}0{}'.format(i, j) if j <= 9 else '{}{}'.format(i, j))

    return dates


def get_ibge_codes(file_path, filter_by_column):
    ibge_codes = []

    with open(file_path, newline='', encoding='utf-8') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        filtered = list(filter(lambda x: filter_by_column in x, spamreader))

        for arr in filtered:
            ibge_codes.append('{}{}'.format(arr[1], arr[2]))

    return ibge_codes


def gather_data(dates, ibge_codes, save_path):
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


if __name__ == '__main__':
    jobs = []
    dates = get_date_range((2016, 2020), (1, 13))
    ibge_codes = get_ibge_codes('csv/municipios_IBGE.csv', 'SE')

    for i in range(0, 10):
        process = m.Process(target=gather_data, args=(
            dates, ibge_codes, 'JSON/data.json'))

        jobs.append(process)

    for job in jobs:
        job.start()

    for job in jobs:
        job.join()

    print('Extraction process complete.')

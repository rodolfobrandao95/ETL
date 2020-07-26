import csv
import json


state_regions = {
    'AC': 'Norte',
    'AL': 'Nordeste',
    'AP': 'Norte',
    'AM': 'Norte',
    'BA': 'Nordeste',
    'CE': 'Nordeste',
    'DF': 'Centro-Oeste',
    'ES': 'Sudeste',
    'GO': 'Centro-Oeste',
    'MA': 'Nordeste',
    'MT': 'Centro-Oeste',
    'MS': 'Centro-Oeste',
    'MG': 'Sudeste',
    'PA': 'Norte',
    'PB': 'Nordeste',
    'PR': 'Sul',
    'PE': 'Nordeste',
    'PI': 'Nordeste',
    'RJ': 'Sudeste',
    'RN': 'Nordeste',
    'RS': 'Sul',
    'RO': 'Norte',
    'RR': 'Norte',
    'SC': 'Sul',
    'SP': 'Sudeste',
    'SE': 'Nordeste',
    'TO': 'Norte'
}


def build_time_dimension(year_range: tuple, month_range: tuple, save_path: str) -> None:
    '''
    Writes a .csv file containing the data about time dimension,
    based on the year and month range defined,
    and saves it in the specified path.
    '''

    with open(save_path, 'w+', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)

        spamwriter.writerow(
            ['id', 'year', 'month_number', 'bimonth_number', 'quarter_number', 'half_year_number'])

        for year in range(year_range[0], year_range[1] + 1):
            for month in range(month_range[0], month_range[1] + 1):
                id = '{}0{}'.format(
                    year, month) if month <= 9 else '{}{}'.format(year, month)
                bimonth = month // 2 if month % 2 == 0 else (month // 2) + 1
                quarter = month // 3 if month % 3 == 0 else (month // 3) + 1
                half_year = month // 6 if month % 6 == 0 else (month // 6) + 1

                spamwriter.writerow(
                    [id, year, month, bimonth, quarter, half_year])


def build_city_dimension(reading_file: str, save_path: str, column_value='') -> None:
    '''
    Reads a .csv file containing the data about the cities
    and saves another one, in the specified path, with the proper city dimension.
    Optional keywords arguments: column_value: value of the column to be filtered.
    '''

    with open(save_path, 'w+', newline='', encoding='utf-8') as saving_csvfile:
        spamwriter = csv.writer(saving_csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)

        spamwriter.writerow(
            ['id', 'city_name', 'state_initials', 'state_region'])

        with open(reading_file, newline='', encoding='utf-8') as reading_csvfile:
            spamreader = csv.reader(
                reading_csvfile, delimiter=',', quotechar='|')
            filtered = list(filter(lambda x: column_value in x, spamreader)
                            ) if column_value != '' else list(spamreader)

            for row in filtered:
                id = '{}{}'.format(row[1], row[2])
                city_name = row[3].replace("'", '', 1)
                state_region = state_regions[row[0]]
                state_initials = row[0]
                spamwriter.writerow(
                    [id, city_name, state_initials, state_region])


def build_fate_dimension(reading_file: str, save_path: str) -> None:
    '''
    Reads a .json file containing the API's data and saves a .csv file,
    in the specified path, with the proper fate dimension.
    '''

    with open(save_path, 'w+', newline='', encoding='utf-8') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)

        spamwriter.writerow(['TIME_DM_id', 'CITY_DM_id',
                             'beneficiaries_number', 'amount_value'])

        with open(reading_file, 'r', encoding='utf-8') as jsonfile:
            json_data = json.load(jsonfile)
            for item in json_data:
                TIME_DM_id = '{}{}'.format(
                    item['dataReferencia'][6:], item['dataReferencia'][3:5])
                CITY_DM_id = item['municipio']['codigoIBGE']
                beneficiaries_number = item['quantidadeBeneficiados']
                amount_value = item['valor']

                spamwriter.writerow(
                    [TIME_DM_id, CITY_DM_id, beneficiaries_number, amount_value])

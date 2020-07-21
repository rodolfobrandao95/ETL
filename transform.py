import csv
import json


state_regions = {
    "AC": "Norte",
    "AL": "Nordeste",
    "AP": "Norte",
    "AM": "Norte",
    "BA": "Nordeste",
    "CE": "Nordeste",
    "DF": "Centro-Oeste",
    "ES": "Sudeste",
    "GO": "Centro-Oeste",
    "MA": "Nordeste",
    "MT": "Centro-Oeste",
    "MS": "Centro-Oeste",
    "MG": "Sudeste",
    "PA": "Norte",
    "PB": "Nordeste",
    "PR": "Sul",
    "PE": "Nordeste",
    "PI": "Nordeste",
    "RJ": "Sudeste",
    "RN": "Nordeste",
    "RS": "Sul",
    "RO": "Norte",
    "RR": "Norte",
    "SC": "Sul",
    "SP": "Sudeste",
    "SE": "Nordeste",
    "TO": "Norte"
}


def get_time_dimension(year_range, month_range, save_path):
    with open(save_path, "w+", newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(
            ["id", "year", "month", "bimonth", "trimester", "semester"])

        for year in range(year_range[0], year_range[1]):
            for month in range(month_range[0], month_range[1]):
                id = "{}0{}".format(
                    year, month) if month <= 9 else "{}{}".format(year, month)
                bimonth = month // 2 if month % 2 == 0 else (month // 2) + 1
                trimester = month // 3 if month % 3 == 0 else (month // 3) + 1
                semester = month // 6 if month % 6 == 0 else (month // 6) + 1

                spamwriter.writerow(
                    [id, year, month, bimonth, trimester, semester])


def get_city_dimension(csv_file_path, save_path, column_value=""):
    with open(save_path, "w+", newline='', encoding="utf-8") as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(["id", "city_name", "city_region", "state_name"])

        with open(csv_file_path, newline='', encoding="utf-8") as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            filtered = list(filter(lambda x: column_value in x, spamreader)
                            ) if column_value != "" else list(spamreader)

            for row in filtered:
                id = "{}{}".format(row[1], row[2])
                city_name = row[3]
                city_region = state_regions[row[0]]
                state_name = row[0]
                spamwriter.writerow([id, city_name, city_region, state_name])


def get_fate_dimension(json_file_path, save_path):
    fate_dimension = []

    with open(save_path, "w+", newline='', encoding="utf-8") as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(["TIME_DM_id", "CITY_DM_id",
                             "beneficiaries_number", "amount_value"])

        with open(json_file_path, "r", encoding="utf-8") as jsonfile:
            json_data = json.load(jsonfile)
            for item in json_data:
                TIME_DM_id = "{}{}".format(
                    item["dataReferencia"][6:], item["dataReferencia"][3:5])
                CITY_DM_id = item["municipio"]["codigoIBGE"]
                beneficiaries_number = item["quantidadeBeneficiados"]
                amount_value = item["valor"]

                spamwriter.writerow(
                    [TIME_DM_id, CITY_DM_id, beneficiaries_number, amount_value])

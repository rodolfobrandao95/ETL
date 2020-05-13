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


def get_time_dimension(year_range):
    year_period = []

    for year in range(year_range[0], year_range[1]):
        for month in range(1, 13):
            id = "{}0{}".format(
                year, month) if month <= 9 else "{}{}".format(year, month)
            bimonth = month // 2 if month % 2 == 0 else (month // 2) + 1
            trimester = month // 3 if month % 3 == 0 else (month // 3) + 1
            semester = month // 6 if month % 6 == 0 else (month // 6) + 1
            year_period.append((id, year, month, bimonth, trimester, semester))

    return year_period


def get_city_dimension():
    return


if __name__ == "__main__":
    year_period = get_time_dimension((2016, 2020))

    with open("csv/time_dimension.csv", "w+", newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(
            ["id", "year", "month", "bimonth", "trimester", "semester"])

        for period in year_period:
            spamwriter.writerow(
                [period[0], period[1], period[2], period[3], period[4], period[4]])

    print("Transform process complete.")

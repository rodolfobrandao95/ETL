import extract as e


def main():
    # print(e.consume_api('2019', '01', '28', '00308', 'JSON/data.json'))
    print(e.read_xls('xls/municipios_IBGE.xlsx'))


if __name__ == "__main__":
    main()

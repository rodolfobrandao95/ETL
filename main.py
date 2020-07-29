import extract as extract_layer
import load as load_layer
import transform as transform_layer
import multiprocessing as m


if __name__ == '__main__':
    # Extract:
    jobs = []
    dates = extract_layer.set_date_range((2016, 2019), (1, 12))
    ibge_codes = extract_layer.set_ibge_codes('csv/municipios_IBGE.csv', 'SE')

    for i in range(0, 10):
        process = m.Process(target=extract_layer.gather_data, args=(
            dates, ibge_codes, 'JSON/data.json'))
        jobs.append(process)

    for job in jobs:
        job.start()

    for job in jobs:
        job.join()

    print('Extract process complete.')

    # Transform:
    transform_layer.build_temporal_dimension(
        (2016, 2019), (1, 12), 'csv/time_dimension.csv')

    transform_layer.build_spatial_dimension(
        'csv/municipios_IBGE.csv', 'csv/city_dimension.csv', column_value='SE')

    transform_layer.build_fate_dimension(
        'JSON/data.json', 'csv/fate_dimension.csv')

    print('Transform process complete.')

    # # Load:
    database_info = {
        'pyodbc_drive': 'ODBC Driver 17 for SQL Server',
        'server': 'RODOLFO-PC',
        'database': 'etl',
        'username': '',
        'password': ''
    }

    table_info = {
        0: {
            'schema': 'dbo',
            'name': 'fate_dm',
            'constraints': [
                'fate_dm_pk',
                'city_dm_fate_dm_fk',
                'time_dm_fate_dm_fk'
            ]
        },
        1: {
            'schema': 'dbo',
            'name': 'time_dm',
            'constraints': [
                'time_dm_pk'
            ]
        },
        2: {
            'schema': 'dbo',
            'name': 'city_dm',
            'constraints': [
                'city_dm_pk'
            ]
        }
    }

    load_layer.build_database(database_info, 'sql/star_model.sql')

    load_layer.load_database('csv/time_dimension.csv',
                             database_info, 'time_dm', schema='dbo')

    load_layer.load_database('csv/city_dimension.csv',
                             database_info, 'city_dm', schema='dbo')

    load_layer.load_database('csv/fate_dimension.csv',
                             database_info, 'fate_dm', schema='dbo')

    print('Load process complete.')

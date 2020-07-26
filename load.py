import csv
import pyodbc
import re as regex


def build_database(database_info: dict, reading_file: str) -> None:
    '''
    Accesses the database and execute the "CREATE TABLE" DML statement from a .sql file.
    '''

    try:
        connection_string = 'Trusted_Connection=yes;DRIVER={};SERVER={};DATABASE={};UID={};PWD={}'.format(
            database_info['pyodbc_drive'], database_info['server'], database_info['database'], database_info['username'], database_info['password'])
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        with open(reading_file, 'r') as sqlfile:
            raw_text = sqlfile.read()
            cursor.execute(raw_text)
            connection.commit()
            connection.close()

        print('Database built.')
    except pyodbc.Error as e:
        print(e)
    except Exception as e:
        print(e)


def load_database(reading_file: str, database_info: dict, table_name: str, schema='') -> None:
    '''
    Accesses the database and execute the "INSERT INTO" DML statement
    from a .csv file, based on the specified table.
    '''

    try:
        connection_string = 'Trusted_Connection=yes;DRIVER={};SERVER={};DATABASE={};UID={};PWD={}'.format(
            database_info['pyodbc_drive'], database_info['server'], database_info['database'], database_info['username'], database_info['password'])
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()
        prefix = ''

        with open(reading_file, newline='', encoding='utf-8') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',')
            headers = next(spamreader)
            prefix = ('INSERT INTO [{}] VALUES ('.format(
                table_name) if schema == '' else 'INSERT INTO [{}].[{}]('.format(schema, table_name)) + ', '.join(headers) + ')\nVALUES ('
            rowcount = 0

            for columns in spamreader:
                values = [
                    "'" + value + "'" if regex.match('[a-zA-Z]', value) else value for value in columns]
                insert_statement = prefix + ', '.join(values) + ');\n'
                cursor.execute(insert_statement)
                rowcount += cursor.rowcount
                print(insert_statement)

            print(str(rowcount) + ' register(s) inserted.')

            connection.commit()
            connection.close()
    except pyodbc.Error as e:
        print(e)
    except Exception as e:
        print(e)


def clear_database(database_info: dict, table_info: dict) -> None:
    '''
    Accesses the database and execute the "DELETE FROM" DDL statement on the specified table(s).
    '''

    try:
        connection_string = 'Trusted_Connection=yes;DRIVER={};SERVER={};DATABASE={};UID={};PWD={}'.format(
            database_info['pyodbc_drive'], database_info['server'], database_info['database'], database_info['username'], database_info['password'])
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        for key, value in table_info:
            drop_statement = 'DELETE TABLE ' + (table['name'] + ';' if table['schema'] == '' else '{}.{};'.format(
                table['schema'], table['name']))
            cursor.execute(drop_statement)
            print(drop_statement)

            pass

        connection.commit()
        connection.close()

        print('Database cleaned.')
    except pyodbc.Error as e:
        print(e)
    except Exception as e:
        print(e)


def drop_database(database_info: dict, table_info: dict) -> None:
    '''
    Accesses the database and execute the "DROP TABLE" DML statement on the specified table(s).
    '''

    try:
        connection_string = 'Trusted_Connection=yes;DRIVER={};SERVER={};DATABASE={};UID={};PWD={}'.format(
            database_info['pyodbc_drive'], database_info['server'], database_info['database'], database_info['username'], database_info['password'])
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        for key, table in table_info.items():
            drop_statement = 'DROP TABLE ' + (table['name'] + ';' if table['schema'] == '' else '{}.{};'.format(
                table['schema'], table['name']))
            cursor.execute(drop_statement)
            print(drop_statement)

        connection.commit()
        connection.close()

        print('Database droped.')
    except pyodbc.Error as e:
        print(e)
    except Exception as e:
        print(e)

import csv
# import pyodbc


# server = "tcp:myserver.database.windows.net"
# database = "mydb"
# username = ""
# password = ""
# connection = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};SERVER=" +
#                             server+";DATABASE="+database+";UID="+username+";PWD=" + password)
# cursor = connection.cursor()


def generate_dml_from_csv(reading_file: str, save_path: str, table_name: str, schema='') -> None:
    '''
    Converts a .csv file into a .sql file, with the
    DML INSERT command, based on the table name specified.
    Optional keywords arguments: schema: name of the database schema.
    '''

    prefix = ''
    dml = ''

    with open(save_path, 'w+', encoding='utf-8') as sqlfile:
        with open(reading_file, newline='', encoding='utf-8') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',')
            headers = next(spamreader)

            prefix = ('INSERT INTO [{}] VALUES ('.format(
                table_name) if schema == '' else 'INSERT INTO [{}].[{}] ('.format(schema, table_name)) + ', '.join(headers) + ')\nVALUES ('

            for columns in spamreader:
                dml += prefix + \
                    ', '.join(columns).replace("'", '', 1) + ');\n\n'

        sqlfile.write(dml)
    sqlfile.close()

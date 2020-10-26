# ------------------------------------------------------------------------ #
# Title: Query GageInsight Database
# Description: sqlite query returning (gage_id, desc, company, serial_num, manufacturer, model_num, cert_template)

# ------------------------------------------------------------------------ #
import pyodbc

if __name__ == "__main__":
    raise Exception("This file is not meant to ran by itself")

# Connection Details
server = 'CES24'
database = 'GIMSSQL'
username = 'username'
password = 'password'
cnxn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor = cnxn.cursor()


# SQL Query
def fetch(gageid):
    # gage_id, desc, company, serial_num, mfg, model_num, cert_template
    cursor.execute("SELECT gages.gage_sn, gages.gage_descr, gages.company, gages.gage_id, gages.manufacturer,"
                   "gages.model_num, gages.cert_type FROM gages WHERE gages.gage_sn = " + "'" + gageid + "'" + ";")

    # for row in cursor.fetchall():
    #     print(row)
    # print(cursor.fetchone())
    return cursor.fetchone()


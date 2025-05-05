import pyodbc as odbc
import pandas as pd
import sqlalchemy as sa

DRIVER_NAME='SQL Server'
SERVER_NAME='SMSK'
DATABASE_NAME='THYKARGO'

connection_string = f"""
    DRIVER={{{DRIVER_NAME}}};
    SERVER={SERVER_NAME};
    DATABASE={DATABASE_NAME};
    Trust_Connection=yes;

"""
conn = odbc.connect(connection_string)


engine = sa.create_engine('mssql+pyodbc://SMSK/THYKARGO')

print(pd.read_sql("select * from RUSSIA", engine))



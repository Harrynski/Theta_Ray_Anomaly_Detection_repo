import pandas as pd
import numpy as np
import os
from dotenv import load_dotenv
import pyodbc


#Query from Database
def db_connect(env_path, query_name, db_name, server_name='Server', user_name='User', user_password='Pass'):
    
    load_dotenv(env_path)

    server = os.getenv(server_name)
    database = os.getenv(db_name)
    user = os.getenv(user_name) 
    password = os.getenv(user_password)
    query = os.getenv(query_name)

    cnxn_string = (f"Driver={{SQL Server Native Client 11.0}};"
            f"Server={server};"
            f"Database={database};"
            f"UID={user};"
            f"PWD={password};")
    
    cnxn = pyodbc.connect(cnxn_string)
    output = pd.read_sql(query, cnxn)
    cnxn.close()

    return(output)

envi_path = 'query_all.env'

MT = db_connect(envi_path, query_name='query_MT', db_name='Database_MT')

TC = db_connect(envi_path, query_name='query_TC', db_name='Database_TC')
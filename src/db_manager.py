import sqlite3
import pandas as pd

DB_PATH = "db/medallion.db"

def get_connection():
    """
    Returns a connection to the database.
    """
    return sqlite3.connect(DB_PATH)

def write_to_table(df, table_name, if_exists="replace"):
    """
    Writes a DataFrame in a table on the database
    """
    conn = get_connection()
    df.to_sql(table_name, conn, if_exists=if_exists, index=False)
    conn.close()

def read_from_table(table_name):
    """
    Reads a table from the db.
    """
    conn = get_connection()
    df = pd.read_sql(f"SELECT * FROM {table_name}", conn)
    conn.close()
    return df
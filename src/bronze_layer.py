import pandas as pd
from .db_manager import write_to_table

# file_path='opt/airflow/data/transactions.csv'
def load_bronze_data(file_path):
    """
    Loads the unprocessed data from the CSV and loards them into the table 'bronze_transactions' in the db.
    """
    df = pd.read_csv(file_path)
    write_to_table(df, "bronze_transactions")
    return df

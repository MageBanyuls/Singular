import pandas as pd
from .db_manager import read_from_table, write_to_table
from .data_cleaning import handle_missing_data, convert_data_types, remove_outliers


def clean_silver_layer():
    """
    Cleans the data from de bronze layer an saves it in the silver layer.
    
    """

    # Reading the raw data
    df=read_from_table('bronze_transactions')

    # Dropping null values

    df= handle_missing_data(df)

    # Converting data types
    df= convert_data_types(df)

    # Remove outliers with the percentil 0.01 and 0.99 from price

    df = remove_outliers(df, 'item_price')
    df = remove_outliers(df, 'quantity')

    # Write it into the db

    write_to_table(df, 'silver_transactions')

    return df




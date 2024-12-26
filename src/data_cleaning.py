import pandas as pd




def handle_missing_data(df):
    """
    Erase rows with missing fields
    """
    return df.dropna()

def convert_data_types(df):
    """
    Converts date to datetime, price to float and quatity to interger
    """
    df['transaction_date'] = pd.to_datetime(df['transaction_date'])
    df['item_price'] = df['item_price'].astype(float)
    df['quantity'] = df['quantity'].astype(int)
    return df

def remove_outliers(df, column, lower_percentile=0.01, upper_percentile=0.99):
    """
    Erase outliers in a specific column that are out from the lower and upper percentile
    """
    lower_bound = df[column].quantile(lower_percentile)
    upper_bound = df[column].quantile(upper_percentile)
    return df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]
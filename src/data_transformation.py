from .db_manager import read_from_table, write_to_table
import pandas as pd


def add_total_amount():
    """
    Add column `total_amount` to the cleaned data
    """
    df = read_from_table("silver_transactions")

    df['total_amount'] = df['item_price'] * df['quantity']

    write_to_table(df, "silver_transactions")

    return df

def calculate_total_spent_by_user():
    """
    Calculates total by user_id and stores it in a new table.
    """
    df = read_from_table("silver_transactions")

    user_totals = df.groupby('user_id', as_index=False)['total_amount'].sum()

    top_10_users = user_totals.sort_values('total_amount', ascending=False).head(10)

    write_to_table(user_totals, "user_totals")

    return user_totals, top_10_users

def generate_time_series_report():
    """
    Time series report sales by day.
    """
    df = read_from_table("silver_transactions")

    print(df['transaction_date'].dtypes)
    df['transaction_date'] = pd.to_datetime(df['transaction_date'])
    daily_sales = df.groupby(df['transaction_date'].dt.date)['total_amount'].sum().reset_index()

    daily_sales.rename(columns={"transaction_date": "date", "total_amount": "daily_sales"}, inplace=True)

    write_to_table(daily_sales, "daily_sales")

    return daily_sales


def generate_monthly_sales_report():
    """
    Monthly sales report.
    """
    df = read_from_table("silver_transactions")

    df['transaction_date'] = pd.to_datetime(df['transaction_date'])

    monthly_sales = df.groupby(df['transaction_date'].dt.to_period('M'))['total_amount'].sum().reset_index()

    monthly_sales.rename(columns={"transaction_date": "month", "total_amount": "monthly_sales"}, inplace=True)

    monthly_sales['month'] = monthly_sales['month'].dt.strftime('%Y-%m')
    write_to_table(monthly_sales, "monthly_sales")

    return monthly_sales




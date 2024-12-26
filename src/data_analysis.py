import pandas as pd
from .db_manager import read_from_table, write_to_table


def identify_top_categories():
    """
    Identifies the top 3 categories based on the total amount sold.
    """
    df = read_from_table("silver_transactions")

    category_totals = df.groupby('item_category', as_index=False)['total_amount'].sum()

    top_categories = category_totals.sort_values('total_amount', ascending=False).head(3)

    write_to_table(top_categories, "top_categories")

    return top_categories

def segment_customers():

    """
    Segments users in 'low_spenders', 'medium_spenders' and 'high_spenders'.
    """

    user_totals = read_from_table("user_totals")
    
    low_threshold = user_totals['total_amount'].quantile(0.33)
    high_threshold = user_totals['total_amount'].quantile(0.66)

    def categorize(amount):
        if amount <= low_threshold:
            return 'low_spender'
        elif amount <= high_threshold:
            return 'medium_spender'
        else:
            return 'high_spender'

    user_totals['spending_category'] = user_totals['total_amount'].apply(categorize)
    write_to_table(user_totals, "segmented_users")
    return user_totals


def retention_analysis():
    """
    Calculate the users percentage with multiple purchases and analyze retention.
    """
    df = read_from_table("silver_transactions")


    user_purchase_counts = df.groupby('user_id', as_index=False)['transaction_id'].count()
    print(user_purchase_counts.head(10))

    user_purchase_counts.rename(columns={'transaction_id': 'purchase_count'}, inplace=True)

    
    multiple_purchasers = user_purchase_counts[user_purchase_counts['purchase_count'] > 1]

    if len(user_purchase_counts) > 0:
        retention_rate = round(len(multiple_purchasers) / len(user_purchase_counts) * 100)
    else:
        retention_rate = 0


    retention_data = pd.DataFrame({
        "total_users": [len(user_purchase_counts)],
        "multiple_purchasers": [len(multiple_purchasers)],
        "retention_rate": [retention_rate]
    })
    write_to_table(retention_data, "retention_analysis")
    return retention_data
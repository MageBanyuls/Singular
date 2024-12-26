import matplotlib.pyplot as plt
import seaborn as sns

from matplotlib.backends.backend_pdf import PdfPages
from .data_analysis import identify_top_categories, retention_analysis
from .data_transformation import calculate_total_spent_by_user, generate_time_series_report, generate_monthly_sales_report



def plot_top_categories(top_categories):

    sns.barplot(x='item_category', y='total_amount', data=top_categories, palette='viridis')
    plt.title('Top 3 most sold categories')
    plt.xlabel('Category')
    plt.ylabel('Total Sold')
    plt.xticks(rotation=45)
    plt.tight_layout()



def plot_total_spent_by_user(user_totals, top_10_users):

    sns.barplot(x='user_id', y='total_amount', data=top_10_users, palette='viridis')
    plt.title('Top 10 buyers')
    plt.xlabel('UserId')
    plt.ylabel('Total expended')
    plt.xticks(rotation=45)
    plt.tight_layout()



def plot_daily_sales(daily_sales):
    sns.lineplot(x='date', y='daily_sales', data=daily_sales, marker='o')
    plt.title('Daily sales')
    plt.xlabel('Date')
    plt.ylabel('Daily sale')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()

    
def plot_monthly_sales(Monthly_sales):
    sns.barplot(x='month', y='monthly_sales', data=Monthly_sales, hue='month', palette='viridis')
    plt.title('Monthly sales')
    plt.xlabel('Date')
    plt.ylabel('Monthly sale')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()


def generate_pdf_report(top_categories, user_totals,top_10_users, daily_sales, monthly_sales):
    pdf_path = 'sales_report.pdf'

    with PdfPages(pdf_path) as pdf:
        # top categories
        plt.figure(figsize=(10, 6))
        plot_top_categories(top_categories)
        pdf.savefig()
        plt.close()

        # totals spended by user
        plt.figure(figsize=(12, 8))
        plot_total_spent_by_user(user_totals, top_10_users)
        pdf.savefig()
        plt.close()

        # daily sales
        plt.figure(figsize=(12, 8))
        plot_daily_sales(daily_sales)
        pdf.savefig()  
        plt.close()

        # monthly sales
        plt.figure(figsize=(12, 8))
        plot_monthly_sales(Monthly_sales=monthly_sales)
        pdf.savefig()  
        plt.close()
    print(f"Report done in {pdf_path}")


def create_and_generate_report():
    top_categories = identify_top_categories()
    user_totals, top_10_users = calculate_total_spent_by_user()
    daily_sales = generate_time_series_report()
    monthly_sales=generate_monthly_sales_report()

    generate_pdf_report(top_categories, user_totals,top_10_users, daily_sales, monthly_sales)

from .bronze_layer import load_bronze_data
from .silver_layer import clean_silver_layer
from .gold_layer import run_gold_layer_funcs
from .graphs import create_and_generate_report

file_path='data/transactions.csv'

def main():
    print("Starting data processing...")
    
    # Bronze layer
    load_bronze_data(file_path)

    #  Silver layer
    clean_silver_layer()

    # Gold layer
    run_gold_layer_funcs()

    # Generate report
    create_and_generate_report()

    print("Data processing finished")
    

if __name__ == "__main__":
    main()

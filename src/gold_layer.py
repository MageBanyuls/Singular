from .data_transformation import *
from .data_analysis import *


def run_gold_layer_funcs():

    """
    Runs all the functions that make the gold layer.
    """

    add_total_amount()

    calculate_total_spent_by_user()

    generate_time_series_report()

    identify_top_categories()

    segment_customers()

    retention_analysis()



if __name__ == "__main__":
    run_gold_layer_funcs()


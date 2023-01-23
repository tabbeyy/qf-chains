"""
This skeleton file uses pandas for reading and working with the CSV files.

"""

import pandas as pd

def load_chains(ticker: str) -> tuple[pd.DataFrame, pd.DataFrame]:
    calls_df = pd.read_csv(f"{ticker}_calls.csv")
    puts_df = pd.read_csv(f"{ticker}_puts.csv")
    
    return calls_df, puts_df


calls_df, puts_df = load_chains(ticker="KFC")

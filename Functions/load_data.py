# load in the data
import pandas as pd

def load_data(filepath):
    return pd.read_excel(filepath, header = 8, sheet_name=None)

def load_tabell_data(filepath):
    return pd.read_excel(filepath, header= 7, sheet_name="Tabell 1B")
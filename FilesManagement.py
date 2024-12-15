import os
import pandas as pd
import EntryClass

def insert_purchase_into_excel(purchase):
    return

def read_excel(purchase):
    file_name = f"Finanzas_{purchase.month}_{purchase.year}.xlsx"
    folder_path = f"Mensuales"
    file_path = os.path.join(folder_path,file_name)
    df = pd.read_excel(file_path)
    return df
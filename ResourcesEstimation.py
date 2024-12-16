import pandas as pd
import FilesManagement
import EntryClass
import GlobalVariables
from datetime import datetime

def calculate_available_balance():
    aux_purchase = EntryClass.Purchase("aux", 
                                "0", 
                                "1",
                                GlobalVariables.CUOTA_DEFAULT,
                                datetime.today().strftime("%d"),
                                datetime.today().strftime("%m"),
                                datetime.today().strftime("%Y"))
    
    current_month_path = FilesManagement.create_file_path(aux_purchase)
    current_month_expenses = pd.read_excel(current_month_path)
    total_expenses = calculate_month_total_expenses(current_month_expenses)
    available_balance = int(GlobalVariables.SUELDO - total_expenses)
    return available_balance
    
def calculate_month_total_expenses(df):
    expenses = []
    for _, row in df.iterrows():
        expense = row.get("Monto", 0) / row.get("Cuotas", 1)
        expenses.append(expense)
    return sum(expenses)
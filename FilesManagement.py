import os
import pandas as pd
from datetime import datetime
import EntryClass

def create_file_path(purchase):
    """Crea el path del archivo correspondiente al purchase específico."""
    file_name = f"Finanzas_{purchase.month}_{purchase.year}.xlsx"
    folder_path = "Mensuales"
    file_path = os.path.join(folder_path, file_name)
    return file_path

def transfer_purchases_with_payments(first_purchase_new_month):
    """Transfiere todas las compras realizadas en cuotas aumentando la cuota actual."""

    new_month_file_path = create_file_path(first_purchase_new_month)

    current_month = int(first_purchase_new_month.month)
    current_year = int(first_purchase_new_month.year)

    if current_month == 1:
        previous_month = 12
        previous_year = current_year - 1
    else:
        previous_month = current_month - 1
        previous_year = current_year

    previous_month_file = f"Finanzas_{previous_month}_{previous_year}.xlsx"
    folder_path = "Mensuales"
    previous_month_path = os.path.join(folder_path, previous_month_file)

    if not os.path.exists(previous_month_path):
        print(f"El archivo {previous_month_path} no existe.")
        return

    df = pd.read_excel(previous_month_path)

    df_filtered = df[df['Cuotas'] > 1]

    purchases = EntryClass.Purchase.from_dataframe(df_filtered)

    for purchase in purchases:
        purchase.quota += 1
        purchase.month = str(current_month)
        purchase.year = str(current_year)
        
        insert_purchase_into_excel(purchase)
    
    print(f"Las compras han sido transferidas exitosamente a {new_month_file_path}.")

def create_new_excel(purchase):
    """Crea un nuevo archivo Excel con la estructura inicial y agrega la primera fila."""
    file_path = create_file_path(purchase)

    data = {
        "Monto": [purchase.amount],
        "Cuota": [purchase.quota],
        "Cuotas": [purchase.payments],
        "Fecha": [f"{purchase.day}-{purchase.month}-{purchase.year}"],
        "Description": [purchase.description]
    }

    df = pd.DataFrame(data)
    df.to_excel(file_path, index=False)
    print(f"Archivo creado: {file_path}")
    
    transfer_purchases_with_payments(purchase)

def insert_purchase_into_excel(purchase):
    """Agrega una nueva compra a un archivo Excel. Crea el archivo si no existe."""
    file_name = f"Finanzas_{purchase.month}_{purchase.year}.xlsx"
    folder_path = "Mensuales"
    file_path = os.path.join(folder_path, file_name)
    
    fecha_str = f"{purchase.day}-{purchase.month}-{purchase.year}"
    
    if not os.path.exists(file_path):
        print("El archivo no existe. Creando uno nuevo...")
        create_new_excel(purchase)
    else:
        print("El archivo existe. Agregando nueva fila...")
        df = pd.read_excel(file_path)
        
        df['Monto'] = pd.to_numeric(df['Monto'], errors='coerce')
        df['Cuota'] = pd.to_numeric(df['Cuota'], errors='coerce')
        df['Cuotas'] = pd.to_numeric(df['Cuotas'], errors='coerce')
        
        new_data = {
            "Monto": purchase.amount,
            "Cuota": purchase.quota,
            "Cuotas": purchase.payments,
            "Fecha": fecha_str,
            "Description": purchase.description
        }
        
        df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
        
        df['Monto'] = df['Monto'].astype(int)
        df['Cuota'] = df['Cuota'].astype(int)
        df['Cuotas'] = df['Cuotas'].astype(int)
        
        df.to_excel(file_path, index=False)
        print(f"Fila agregada al archivo: {file_path}")
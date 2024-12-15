from datetime import datetime
import GlobalVariables
import EntryClass

def get_purchase_data_from_user():
    new_entry = EntryClass.Purchase(input("Descripción: "), input("Monto: "), input("Cuotas: "))
    day = datetime.today().strftime("%d")
    month = datetime.today().strftime("%m")
    year = datetime.today().strftime("%Y")
    
    if int(day) >= GlobalVariables.DIA_FACTURACION:
        month = str(int(month)+1)
    
    if int(month) % 12 == 1:
        month = str(f"{int(month)-12}".zfill(2))
        year = str(int(year)+1)
    
    return new_entry.description, new_entry.amount, new_entry.quota, day, month, year
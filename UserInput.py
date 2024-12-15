import GlobalVariables
import EntryClass

def get_purchase_data_from_user():
    new_entry = EntryClass.Purchase(input("Descripción: "), 
                                    input("Monto: "), 
                                    input("Cuotas: "),
                                    input("Día?: "),
                                    input("Mes?: "),
                                    input("Año?: "))
    
    if int(new_entry.day) >= GlobalVariables.DIA_FACTURACION:
        new_entry.month = str(int(new_entry.month)+1)
    
    if int(new_entry.month) % 12 == 1:
        new_entry.month = str(f"{int(new_entry.month)-12}".zfill(2))
        new_entry.year = str(int(new_entry.year)+1)
    
    return new_entry
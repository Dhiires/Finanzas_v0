import UserInput
import FilesManagement

new_entry = UserInput.get_purchase_data_from_user()

print(f"Descripción compra: {new_entry.description}\nMonto: {new_entry.amount}\nCuota actual: {new_entry.quota}\nCuotas: {new_entry.payments}\nFecha: {new_entry.day}-{new_entry.month}-{new_entry.year}")

FilesManagement.insert_purchase_into_excel(new_entry)
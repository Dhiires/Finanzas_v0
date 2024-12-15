import UserInput
import FilesManagement

new_entry = UserInput.get_purchase_data_from_user()

print(f"Descripción compra: {new_entry.description}\nMonto: {new_entry.amount}\nCuotas: {new_entry.quota}\nDía: {new_entry.day}\nMes: {new_entry.month}\nAño: {new_entry.year}")

FilesManagement.insert_purchase_into_excel(new_entry)
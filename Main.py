import UserInput

description, amount, quota, day, month, year = UserInput.get_purchase_data_from_user()

print(f"Descripción compra: {description}\nMonto: {amount}\nCuotas: {quota}\nDía: {day}\nMes: {month}\nAño: {year}")
from datetime import datetime

class Purchase:
    
    def __init__(self, description, amount, quota, day, month, year) -> None:
        self.description = description
        self.amount = amount
        self.quota = quota
        self.day = datetime.today().strftime("%d") if day == "" else day
        self.month = datetime.today().strftime("%m") if month == "" else month
        self.year = datetime.today().strftime("%Y") if year == "" else year
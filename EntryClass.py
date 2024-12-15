from datetime import datetime

class Purchase:
    
    def __init__(self, description, amount, payments, quota, day, month, year) -> None:
        self.description = description
        self.amount = amount if amount != "" else 0
        self.quota = quota
        self.payments = payments if payments != "" else 1
        self.day = datetime.today().strftime("%d") if day == "" else day
        self.month = datetime.today().strftime("%m") if month == "" else month
        self.year = datetime.today().strftime("%Y") if year == "" else year
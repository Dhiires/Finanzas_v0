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
        
    @classmethod
    def from_dataframe(cls, df):
        """Convierte un DataFrame con columnas específicas en una lista de objetos Purchase."""
        purchase_list = []
        for _, row in df.iterrows():
            fecha_str = row.get("Fecha", "")
            fecha_parts = fecha_str.split("-")
            year = fecha_parts[0] if len(fecha_parts) > 0 else ""
            month = fecha_parts[1] if len(fecha_parts) > 1 else ""
            day = fecha_parts[2] if len(fecha_parts) > 2 else ""

            purchase = cls(
                description=row.get("Description", ""),
                amount=row.get("Monto", 0),
                payments=row.get("Cuotas", 1),
                quota=row.get("Cuota", 1),
                day=day,
                month=month,
                year=year
            )
            purchase_list.append(purchase)
        return purchase_list 
class Bill:
    
    def __init__(self, description, amount, individual) -> None:
        self.description = description
        self.amount = amount
        self.individual = individual
        
    @classmethod
    def fetch_bill_info_from_dataframe(cls, df):
        bill_list = []
        for _, row in df.iterrow():
            bill = cls(
                description = row.get("Descripcion",""),
                amount = row.get("Monto",""),
                individual = row.get("Individual","Si")
                )
            bill_list.append(bill)
        return bill_list
from datetime import datetime
class Expense:
    def __init__(self,name,amount,category,description):
        self.name=name
        self.amount=amount
        self.category=category
        self.description=description
        self.date=datetime.now().strftime("%Y-%m-%d")
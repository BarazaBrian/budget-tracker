class Transaction:
    def __init__(self, date, amount, category, description, ttype):
        self.date = date
        self.amount = float(amount)
        self.category = category.lower().strip()
        self.description = description
        self.type = ttype  # 'income' or 'expense'

class Income(Transaction):
    def __init__(self, date, amount, category, description):
        super().__init__(date, amount, category, description, "income")


class Expense(Transaction):
    def __init__(self, date, amount, category, description):
        super().__init__(date, amount, category, description, "expense")

class BudgetTracker:
    def __init__(self):
        self.transactions = []   # list to store income + expenses

def add_income(self):
        print("\nAdding income...")
        date = input("Date (YYYY-MM-DD): ")
        amount = self.get_amount()
        category = input("Category: ")
        description = input("Description: ")

        inc = Income(date, amount, category, description)
        self.transactions.append(inc)
        print("Income added successfully!")
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

def add_expense(self):
        print("\nAdding expense...")
        date = input("Date (YYYY-MM-DD): ")
        amount = self.get_amount()
        category = input("Category: ")
        description = input("Description: ")

        exp = Expense(date, amount, category, description)
        self.transactions.append(exp)
        print("Expense added successfully!")

def list_transactions(self):
        print("\n--- All Transactions ---")
        if len(self.transactions) == 0:
            print("No transactions added yet.")
            return

        for t in self.transactions:
            print(t)

def filter_transactions(self):
        print("\nFilter by:")
        print("1) Type (income/expense)")
        print("2) Category")
        print("3) Month (YYYY-MM)")
        choice = input("Choose option: ")

        if choice == "1":
            ttype = input("Enter type (income/expense): ").strip().lower()
            for t in self.transactions:
                if t.type == ttype:
                    print(t)

        elif choice == "2":
            category = input("Enter category: ")
            for t in self.transactions:
                if t.category.lower() == category.lower():
                    print(t)

        elif choice == "3":
            month = input("Enter month (YYYY-MM): ")
            for t in self.transactions:
                if t.date.startswith(month):
                    print(t)

        else:
            print("Invalid choice!")
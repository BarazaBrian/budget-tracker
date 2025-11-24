from tracker import BudgetTracker

def show_menu():
    print("\n===== Budget Tracker =====")
    print("1) Add Income")
    print("2) Add Expense")
    print("3) List Transactions")
    print("4) Filter Transactions")
    print("5) Show Summary")
    print("0) Exit")

def main():
    tracker = BudgetTracker()

    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            tracker.add_income()

        elif choice == "2":
            tracker.add_expense()

        elif choice == "3":
            tracker.list_transactions()

        elif choice == "4":
            tracker.filter_transactions()

        elif choice == "5":
            tracker.show_summary()

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
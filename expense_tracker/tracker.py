import json
from transaction import Transaction


class Expensetracker:
    def __init__(self):
        self.file_name = "transaction.json"

    def load_transactions(self):
        try:
            with open(self.file_name, "r", encoding="utf-8") as file:
                transaction_data = json.load(file)

            transactions = []

            for data in transaction_data:
                transaction = Transaction.from_dict(data)
                transactions.append(transaction)

            return transactions

        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_transactions(self, transactions):
        transaction_data = []

        for transaction in transactions:
            transaction_data.append(transaction.to_dict())

        with open(self.file_name, "w", encoding="utf-8") as file:
            json.dump(
                transaction_data,
                file,
                indent=4,
                ensure_ascii=False,
            )

    def add_transaction(self):
        try:
            amount = float(input("Enter amount: "))

            category = input("Enter category: ").strip()
            transaction_type = (
                input("Enter transaction type (income/expense): ").strip().lower()
            )

            description = input("Enter description (optional): ").strip()

            transactions = self.load_transactions()

            new_transaction = Transaction(
                amount,
                category,
                transaction_type,
                description,
            )

            transactions.append(new_transaction)
            self.save_transactions(transactions)

            print("Transaction added successfully!")

        except ValueError as error:
            print(error)
    def view_transactions(self):
        transactions = self.load_transactions()

        if len(transactions) == 0:
            print("No transactions found!")
            return

        print("\n===== Transactions =====")

        for index, transaction in enumerate(
            transactions,
            start=1,
        ):
            print("\n-------------------------")
            print(f"{index}. {transaction.category}")
            print(f"Amount: {transaction.amount}")
            print(f"Type: {transaction.transaction_type}")
            print(f"Description: {transaction.description}")
            print(f"Date: {transaction.created_at}")
    def select_transaction(self):
        transactions = self.load_transactions()

        if len(transactions) == 0:
            print("No transactions found!")
            return None, None

        self.view_transactions()

        try:
            number = int(input("Enter transaction number: "))
        except ValueError:
            print("Please enter a valid number!")
            return None, None

        index = number - 1

        if index < 0 or index >= len(transactions):
            print("Invalid transaction number!")
            return None, None

        return transactions, index
    def edit_transaction(self):
        transactions, index = self.select_transaction()

        if transactions is None:
            return

        old_transaction = transactions[index]

        try:
            amount = float(input("Enter new amount: "))
            category = input("Enter new category: ").strip()

            transaction_type = input(
                "Enter new type (income/expense): "
            ).strip().lower()

            description = input(
                "Enter new description: "
            ).strip()

            updated_transaction = Transaction(
                amount,
                category,
                transaction_type,
                description,
            )

            updated_transaction.created_at = old_transaction.created_at

            transactions[index] = updated_transaction

            self.save_transactions(transactions)

            print("Transaction updated successfully!")

        except ValueError as error:
            print(error)

    def delete_transaction(self):
        transactions, index = self.select_transaction()

        if transactions is None:
            return

        deleted_transaction = transactions.pop(index)

        self.save_transactions(transactions)

        print(
            f"{deleted_transaction.category} transaction "
            f"deleted successfully!"
        )

    def analyze_transactions(self):
        transactions = self.load_transactions()

        if len(transactions) == 0:
            print("No transactions found!")
            return

        total_income = 0
        total_expense = 0

        for transaction in transactions:
            if transaction.transaction_type == "income":
                total_income += transaction.amount

            elif transaction.transaction_type == "expense":
                total_expense += transaction.amount

        balance = total_income - total_expense

        print("\n===== Financial Analysis =====")
        print(f"Total Income: {total_income}")
        print(f"Total Expense: {total_expense}")
        print(f"Balance: {balance}")


    def show_main(self):
        print("\n===== Expense Tracker =====")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Edit Transaction")
        print("4. Delete Transaction")
        print("5. Analyze Transactions")
        print("6. Exit")

    def run(self):
        while True:
            self.show_main()
            choice = input("Enter your choice: ").strip()

            if choice == "1":
                self.add_transaction()

            elif choice == "2":
                self.view_transactions()

            elif choice == "3":
                self.edit_transaction()

            elif choice == "4":
                self.delete_transaction()

            elif choice == "5":
                self.analyze_transactions()

            elif choice == "6":
                print("Goodbye 👋")
                break

            else:
                print("Invalid choice!")
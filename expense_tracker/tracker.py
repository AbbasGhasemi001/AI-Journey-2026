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

from datetime import date


class Transaction:
    def __init__(
        self,
        amount,
        category,
        transaction_type,
        description="",
    ):
        if amount <= 0:
            raise ValueError("Amount must be greater than zero!")

        if transaction_type not in ("income", "expense"):
            raise ValueError("Transaction type must be income or expense!")
        self.amount = amount
        self.category = category
        self.transaction_type = transaction_type
        self.description = description
        self.created_at = date.today().strftime("%Y-%m-%d")

    def to_dict(self):
        transaction_data = {
            "amount": self.amount,
            "category": self.category,
            "transaction_type": self.transaction_type,
            "description": self.description,
            "created_at": self.created_at,
        }

        return transaction_data

    @staticmethod
    def from_dict(data):
        transaction = Transaction(
            data["amount"],
            data["category"],
            data["transaction_type"],
            data["description"],
        )

        transaction.created_at = data["created_at"]

        return transaction

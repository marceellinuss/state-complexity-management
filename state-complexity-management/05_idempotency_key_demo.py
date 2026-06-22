"""
Praktikum 7E. Idempotency Key

Payment callback bisa datang dua kali.
Efek bisnis tidak boleh dobel.

Jalankan:
python 05_idempotency_key_demo.py
"""


class PaymentService:

    def __init__(self):
        self.balance = 0
        self.processed_transactions = set()

    def process_callback(self, transaction_id, amount):

        if transaction_id in self.processed_transactions:
            print("Duplicate callback blocked:", transaction_id)
            return

        self.balance += amount

        self.processed_transactions.add(transaction_id)

        print("Payment processed:", transaction_id)


service = PaymentService()

print("=== IDEMPOTENCY KEY DEMO ===")

service.process_callback("TX-001", 100000)
service.process_callback("TX-001", 100000)

print("\nFinal balance:", service.balance)
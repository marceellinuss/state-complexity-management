"""
Praktikum 7G. Challenge
"""

class InsecureTransfer:

    def __init__(self, sender, receiver, amount):

        self.sender = sender
        self.receiver = receiver
        self.amount = amount

        self.status = "CREATED"

    def set_status(self, status):
        self.status = status


print("=== FAILURE CASE ===")

transfer = InsecureTransfer(
    sender="alice",
    receiver="alice",
    amount=-100000
)

transfer.set_status("COMPLETED")

print(vars(transfer))

print("\nMasalah:")
print("1. sender dan receiver sama")
print("2. amount negatif")
print("3. status bebas")
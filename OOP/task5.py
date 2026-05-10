from abc import ABC, abstractmethod

class PaymentMethod(ABC):

    @abstractmethod
    def pay(self, amount):
        pass

    @abstractmethod
    def refund(self, amount):
        pass

    def log_transaction(self, amount):
        print(f"[LOG] Транзакція на суму {amount} грн")

class CreditCardPayment(PaymentMethod):

    def __init__(self, card_number):
        self.card_number = card_number

    def pay(self, amount):
        self.log_transaction(amount)

        hidden = "****" + self.card_number[-4:]

        print(f"Оплата {amount} грн з кредитної картки {hidden}")

    def refund(self, amount):
        print(f"Повернення {amount} грн на кредитну картку")

class PayPalPayment(PaymentMethod):

    def __init__(self, email):
        self.email = email

    def pay(self, amount):
        self.log_transaction(amount)

        print(f"Оплата {amount} грн через PayPal акаунт {self.email}")

    def refund(self, amount):
        print(f"Повернення {amount} грн на PayPal акаунт {self.email}")

class CryptoPayment(PaymentMethod):

    def __init__(self, wallet_address):
        self.wallet_address = wallet_address

    def pay(self, amount):
        self.log_transaction(amount)

        print(f"Оплата {amount} грн криптовалютою з гаманця {self.wallet_address}")

    def refund(self, amount):
        print("Повернення коштів для криптовалюти неможливе")

payments = [
    CreditCardPayment("1234567812345678"),
    PayPalPayment("user@gmail.com"),
    CryptoPayment("0xA1B2C3D4")
]

for payment in payments:
    payment.pay(100)
    print()

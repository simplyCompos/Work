from abc import ABC, abstractmethod

class Notifier(ABC):

    @abstractmethod
    def send(self, message):
        pass

class EmailNotifier(Notifier):

    def __init__(self, email):
        self.email = email

    def send(self, message):
        print(f"[EMAIL] Повідомлення '{message}' надіслано на {self.email}")

class SMSNotifier(Notifier):

    def __init__(self, phone):
        self.phone = phone

    def send(self, message):
        print(f"[SMS] Повідомлення '{message}' надіслано на номер {self.phone}")

class TelegramNotifier(Notifier):

    def __init__(self, username):
        self.username = username

    def send(self, message):
        print(f"[TELEGRAM] Повідомлення '{message}' надіслано користувачу @{self.username}")

class NotificationManager:

    def __init__(self, notifier)
        self.notifier = notifier

    def notify(self, message):
        self.notifier.send(message)

email_notifier = EmailNotifier("user@gmail.com")
sms_notifier = SMSNotifier("+380991112233")
telegram_notifier = TelegramNotifier("compoc")

manager1 = NotificationManager(email_notifier)
manager1.notify("Ваше замовлення оформлено")

print()

manager2 = NotificationManager(sms_notifier)
manager2.notify("Код підтвердження: 1234")

print()

manager3 = NotificationManager(telegram_notifier)
manager3.notify("Нове повідомлення у чаті")

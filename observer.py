
from abc import ABC, abstractmethod
from datetime import datetime


# Observer interface
class Observer(ABC):

    @abstractmethod
    def update(self, message):
        pass


# Concrete observer
class Subscriber(Observer):

    def __init__(self, name):
        self.name = name
        self.notifications = []

    def update(self, message):
        self.notifications.append(message)
        print(f"[{self.name}] Отримано сповіщення: {message}")


# Notification publisher
class Publisher:

    def __init__(self):
        self.subscribers = []
        self.history = []

    def subscribe(self, subscriber):
        if subscriber not in self.subscribers:
            self.subscribers.append(subscriber)
            print(f"Підписника {subscriber.name} додано.")

    def unsubscribe(self, subscriber):
        if subscriber in self.subscribers:
            self.subscribers.remove(subscriber)
            print(f"Підписника {subscriber.name} видалено.")
        else:
            print("Такого підписника не існує.")

    def show_subscribers(self):
        if not self.subscribers:
            print("Список підписників порожній.")
            return

        print("\nСписок підписників:")
        for number, subscriber in enumerate(self.subscribers, 1):
            print(f"{number}. {subscriber.name}")

    def notify(self, message):
        if not self.subscribers:
            print("Немає підписників для надсилання сповіщення.")
            return

        self.history.append({
            "message": message,
            "date": datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        })

        print("\nРозсилання сповіщень:")

        for subscriber in self.subscribers:
            subscriber.update(message)

        print("Розсилання завершено.")

    def show_history(self):
        if not self.history:
            print("Історія сповіщень порожня.")
            return

        print("\nІсторія сповіщень:")

        for number, notification in enumerate(self.history, 1):
            print(f"{number}. [{notification['date']}]")
            print(f"   {notification['message']}")


# Main application
class NotificationApp:

    def __init__(self):
        self.publisher = Publisher()

    def run(self):
        while True:
            print("\n================================")
            print("       СИСТЕМА СПОВІЩЕНЬ")
            print("================================")
            print("1. Додати підписника")
            print("2. Видалити підписника")
            print("3. Показати список підписників")
            print("4. Опублікувати сповіщення")
            print("5. Показати історію сповіщень")
            print("0. Вихід")
            print("================================")

            choice = input("Оберіть дію: ")

            if choice == "1":
                self.add_subscriber()

            elif choice == "2":
                self.remove_subscriber()

            elif choice == "3":
                self.publisher.show_subscribers()

            elif choice == "4":
                self.publish_notification()

            elif choice == "5":
                self.publisher.show_history()

            elif choice == "0":
                print("Програму завершено.")
                break

            else:
                print("Помилка! Оберіть пункт із меню.")

    def add_subscriber(self):
        name = input("Введіть ім'я підписника: ").strip()

        if not name:
            print("Ім'я не може бути порожнім.")
            return

        subscriber = Subscriber(name)
        self.publisher.subscribe(subscriber)

    def remove_subscriber(self):
        self.publisher.show_subscribers()

        if not self.publisher.subscribers:
            return

        try:
            number = int(input("Введіть номер підписника: "))

            if 1 <= number <= len(self.publisher.subscribers):
                subscriber = self.publisher.subscribers[number - 1]
                self.publisher.unsubscribe(subscriber)
            else:
                print("Неправильний номер.")

        except ValueError:
            print("Введіть ціле число.")

    def publish_notification(self):
        message = input("Введіть текст сповіщення: ").strip()

        if not message:
            print("Повідомлення не може бути порожнім.")
            return

        self.publisher.notify(message)


# Application entry point
if __name__ == "__main__":
    app = NotificationApp()
    app.run()


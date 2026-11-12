
from abc import ABC, abstractmethod
from datetime import datetime


# Интерфейс наблюдателя
class Observer(ABC):

    @abstractmethod
    def update(self, message):
        pass


# Конкретный наблюдатель
class Subscriber(Observer):

    def __init__(self, name):
        self.name = name
        self.notifications = []

    def update(self, message):
        self.notifications.append(message)
        print(f"[{self.name}] Получено уведомление: {message}")


# Издатель уведомлений
class Publisher:

    def __init__(self):
        self.subscribers = []
        self.history = []

    def subscribe(self, subscriber):
        if subscriber not in self.subscribers:
            self.subscribers.append(subscriber)
            print(f"Подписчик {subscriber.name} добавлен.")

    def unsubscribe(self, subscriber):
        if subscriber in self.subscribers:
            self.subscribers.remove(subscriber)
            print(f"Подписчик {subscriber.name} удалён.")
        else:
            print("Такого подписчика нет.")

    def show_subscribers(self):
        if not self.subscribers:
            print("Список подписчиков пуст.")
            return

        print("\nСписок подписчиков:")
        for number, subscriber in enumerate(self.subscribers, 1):
            print(f"{number}. {subscriber.name}")

    def notify(self, message):
        if not self.subscribers:
            print("Нет подписчиков для отправки уведомления.")
            return

        self.history.append({
            "message": message,
            "date": datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        })

        print("\nРассылка уведомлений:")

        for subscriber in self.subscribers:
            subscriber.update(message)

        print("Рассылка завершена.")

    def show_history(self):
        if not self.history:
            print("История уведомлений пуста.")
            return

        print("\nИстория уведомлений:")

        for number, notification in enumerate(self.history, 1):
            print(f"{number}. [{notification['date']}]")
            print(f"   {notification['message']}")


# Основное приложение
class NotificationApp:

    def __init__(self):
        self.publisher = Publisher()

    def run(self):
        while True:
            print("\n================================")
            print("      СИСТЕМА УВЕДОМЛЕНИЙ")
            print("================================")
            print("1. Добавить подписчика")
            print("2. Удалить подписчика")
            print("3. Показать подписчиков")
            print("4. Опубликовать уведомление")
            print("5. Показать историю уведомлений")
            print("0. Выход")
            print("================================")

            choice = input("Выберите действие: ")

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
                print("Программа завершена.")
                break

            else:
                print("Ошибка! Выберите пункт из меню.")

    def add_subscriber(self):
        name = input("Введите имя подписчика: ").strip()

        if not name:
            print("Имя не может быть пустым.")
            return

        subscriber = Subscriber(name)
        self.publisher.subscribe(subscriber)

    def remove_subscriber(self):
        self.publisher.show_subscribers()

        if not self.publisher.subscribers:
            return

        try:
            number = int(input("Введите номер подписчика: "))

            if 1 <= number <= len(self.publisher.subscribers):
                subscriber = self.publisher.subscribers[number - 1]
                self.publisher.unsubscribe(subscriber)
            else:
                print("Неверный номер.")

        except ValueError:
            print("Введите целое число.")

    def publish_notification(self):
        message = input("Введите текст уведомления: ").strip()

        if not message:
            print("Сообщение не может быть пустым.")
            return

        self.publisher.notify(message)


# Запуск программы
if __name__ == "__main__":
    app = NotificationApp()
    app.run()

from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def notify(self, message: str) -> None:
        pass

class EmailNotification(Notification):
    def notify(self, message: str) -> None:
        print(f"Sending Email with message: {message}")

class SMSNotification(Notification):
    def notify(self, message: str) -> None:
        print(f"Sending SMS with message: {message}")

class PushNotification(Notification):
    def notify(self, message: str) -> None:
        print(f"Sending Push Notification with message: {message}")

class NotificationFactory:
    @staticmethod
    def create_notification(channel: str) -> Notification:
        if channel == "email":
            return EmailNotification()
        elif channel == "sms":
            return SMSNotification()
        elif channel == "push":
            return PushNotification()
        else:
            raise ValueError(f"Unknown channel: {channel}")

if __name__ == "__main__":
    # Choose the notification type
    notification_type = "email"  # Can be "sms", "push", etc.
    
    # Create notification using the factory
    notification = NotificationFactory.create_notification(notification_type)
    
    # Send a message
    notification.notify("Hello, this is a test notification!")

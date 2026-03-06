from .repositories import MessageRepository

class ChatService:
    def __init__(self):
        self.repo = MessageRepository()

    def send_message(self, user, content):
        return self.repo.create_message(user, content)
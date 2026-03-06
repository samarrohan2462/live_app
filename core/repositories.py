from core.models import Message

class MessageRepository:
    def get_all_messages(self):
        return Message.objects.all()

    def create_message(self, user, content):
        return Message.objects.create(user=user, content=content)
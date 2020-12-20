# chat/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from datetime import datetime

from .models import (
    Message,
    User,
    ChatRoom,
)

class ChatConsumer(AsyncWebsocketConsumer):

    @database_sync_to_async
    def save_message(self, message, room_id, user_id):
        user = User.objects.get(pk=user_id)
        professional = user.professional
        current_room = ChatRoom.objects.get(pk=room_id)
        Message.objects.create(
            chat_room=current_room,
            user=professional,
            message=message
        )

    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        self.user = self.scope['user']
        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        user_id = text_data_json['user']
        await self.save_message(message, self.room_name, user_id)
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'user': user_id,
                'time': str(datetime.now().day) + " " + str(datetime.now().strftime("%b")) +
                        " " + str(datetime.now().strftime("%I:%M" " %p")),
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'user': event['user'],
            'time': event['time'],
        }))
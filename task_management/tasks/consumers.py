from channels.generic.websocket import AsyncWebsocketConsumer
import json

class TaskConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.project_name = self.scope['url_route']['kwargs']['project_name']
        self.project_group_name = f"project_{self.project_name}"

        await self.channel_layer.group_add(
            self.project_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.project_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        task_data = json.loads(text_data)
        await self.channel_layer.group_send(
            self.project_group_name,
            {
                'type': 'task_update',
                'message': task_data['message']
            }
        )

    async def task_update(self, event):
        message = event['message']
        await self.send(text_data=json.dumps({
            'message': message
        }))

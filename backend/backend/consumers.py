import json

from channels.generic.websocket import AsyncWebsocketConsumer

class Player(AsyncWebsocketConsumer):
    async def websocket_connect(self, message):
        return await super().websocket_connect(message)
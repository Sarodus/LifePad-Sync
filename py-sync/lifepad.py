import json
from microdot.websocket import WebSocket

class LifePad:
    def __init__(self, id: str, ws: WebSocket):
        self.id = id
        self.life = 20
        self.background = '#000000'
        self.image = ''
        self.foreground = '#ffffff'
        self.ws = ws

    async def send_command(self, command: str, payload: str | int):
        if self.ws:
            print(f"Sending command: {command} with payload: {payload} to {self.id} {self.ws}")
            await self.ws.send(json.dumps({ 'command': command, 'payload': payload }))

    def process_command(self, command: str, payload: str | int | dict):
        if command == 'life':
            self.life = payload
        elif command == 'status':
            self.life = payload.get('life')
            self.background = payload.get('background')
            self.image = payload.get('image')
            self.foreground = payload.get('foreground')
        elif command == 'image':
            self.image = payload
        elif command == 'background':
            self.background = payload
            self.image = ''
        elif command == 'foreground':
            self.foreground = payload

    def get_status(self):
        return {
            'id': self.id,
            'life': self.life,
            'background': self.background,
            'image': self.image,
            'foreground': self.foreground
        }


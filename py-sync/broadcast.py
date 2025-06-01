import json
from microdot.websocket import WebSocket

class Broadcast:
    def __init__(self, lifepads: dict):
        self.connections = set()
        self.lifepads = lifepads

    def add(self, ws: WebSocket):
        self.connections.add(ws)

    def remove(self, ws: WebSocket):
        self.connections.remove(ws)

    async def send(self, message: str):
        print('Broadcasting status....')
        for ws in self.connections:
            try:
                await ws.send(message)
            except Exception as e:
                print(f"Error broadcasting to client: {e}")
                # Remove broken connections
                self.connections.discard(ws)

    def _status_payload(self):
        return [
            pad.get_status()
            for pad in self.lifepads.values()
        ]

    def status_message(self):
        return json.dumps({ 'command': 'status', 'payload': self._status_payload()})


    async def process_command(self, data: str):
        try:
            payload = json.loads(data)
            connection_id = payload.get('id')
            command = payload.get('command')
            payload = payload.get('payload')

            print(f"Processing command: {command} with payload: {payload} for connection: {connection_id}")

            self.lifepads[connection_id].process_command(command, payload)
            await self.lifepads[connection_id].send_command(command, payload)
        except Exception as e:
            print(f"Error processing command: {e}")

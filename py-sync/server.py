import json
from microdot import Microdot, send_file, Request
from microdot.websocket import with_websocket, WebSocket
from broadcast import Broadcast
from lifepad import LifePad

# Increase max line length for WebSocket handshake headers
Request.max_readline = 16384  # 16KB - enough for browser headers

port = 5000
app = Microdot()

lifepads = {}
broadcast = Broadcast(lifepads)



@app.route('/lifepad')
@with_websocket
async def lifepad_websocket_broadcast(request, ws):
    broadcast.add(ws)
    try:
        # Send status of all lifepads
        await ws.send(broadcast.status_message())

        while True:
            data = await ws.receive()
            if data is None:  # Connection closed
                break

            await broadcast.process_command(data)

            # Send updated status
            await ws.send(broadcast.status_message())

    except Exception as e:
        print(f"WebSocket error for status endpoint: {e}")
    finally:
        broadcast.remove(ws)
        print("Status WebSocket disconnected")


@app.route('/lifepad/<id>')
@with_websocket
async def lifepad_websocket(request, ws, id):
    client_id = id
    print(f"WebSocket connected: {client_id}")
    
    # Store the lifepad
    life_pad = LifePad(client_id, ws)
    lifepads[client_id] = life_pad

    await broadcast.send(broadcast.status_message())

    try:
        while True:
            data = await ws.receive()
            if data is None:  # Connection closed
                break
            print(f"Received from {client_id}: {data}")
            
            # Parse and process the command
            try:
                message = json.loads(data)
                command = message.get('command')
                payload = message.get('payload')
                life_pad.process_command(command, payload)
            except json.JSONDecodeError:
                print(f"Invalid JSON from {client_id}: {data}")
            
            # Echo the data back
            await ws.send(data)

            # Broadcast the updated status to all connected clients
            await broadcast.send(broadcast.status_message())
            
    except Exception as e:
        print(f"WebSocket error for {client_id}: {e}")
    finally:
        # Clean up the lifepad
        if client_id in lifepads:
            del lifepads[client_id]
        # Broadcast status update after client disconnects
        await broadcast.send(broadcast.status_message())
        print(f"WebSocket disconnected: {client_id}")

# Add proper CORS headers
@app.before_request
async def before_request(request):
    if request.method == 'OPTIONS':
        return '', 200, {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET, POST, OPTIONS, UPGRADE',
            'Access-Control-Allow-Headers': 'Content-Type, Authorization, Upgrade, Connection, Sec-WebSocket-Key, Sec-WebSocket-Version, Sec-WebSocket-Protocol',
            'Access-Control-Allow-Credentials': 'true'
        }

@app.after_request
async def after_request(request, response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    return response


if __name__ == "__main__":
    try:
        app.run(port=port, debug=True, host='0.0.0.0')
    except KeyboardInterrupt:
        print("Server stopped")
        pass

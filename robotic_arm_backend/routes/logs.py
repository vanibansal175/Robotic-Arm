from fastapi import APIRouter, WebSocket, WebSocketDisconnect
import asyncio

router = APIRouter()

active_connections = []


@router.websocket("/ws/logs")
async def websocket_logs(websocket: WebSocket):
    await websocket.accept()
    active_connections.append(websocket)

    try:
        while True:
            await asyncio.sleep(1)  
    except WebSocketDisconnect:
        active_connections.remove(websocket)


async def broadcast_log(message: str, type: str = "info"):
    print("Sending log:", message)  

    dead_connections = []

    for connection in active_connections:
        try:
            await connection.send_json({
                "message": message,
                "type": type
            })
        except:
            dead_connections.append(connection)

    for conn in dead_connections:
        active_connections.remove(conn)


@router.get("/test-log")
async def test_log():
    await broadcast_log("Test log working ", "success")
    return {"status": "sent"}
from fastapi import FastAPI, WebSocketDisconnect
from fastapi.websockets import WebSocket

from typing import List
import asyncio
import uvicorn
import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__) + "/.."))

from config import log_queue



app = FastAPI()

connections: List[WebSocket] = []


@app.websocket("/logs")
async def logs(websocket: WebSocket	):
	await websocket.accept()
	connections.append(websocket)

	try:
		while True:
			while not log_queue.empty():
				log_entry = log_queue.get()
				for conn in connections:
					await conn.send_text(log_entry)
				await asyncio.sleep(0.5)  # Ожидание новых логов
	except WebSocketDisconnect:
		connections.remove(websocket)

if __name__ == "__main__":
	uvicorn.run(app, port = 8000)
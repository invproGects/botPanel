from fastapi import FastAPI, WebSocketDisconnect
from fastapi.websockets import WebSocket
from fastapi.middleware.cors import CORSMiddleware

from typing import List
import asyncio
import uvicorn
import sys
import os
import logging

sys.path.append(os.path.abspath(os.path.dirname(__file__) + "/.."))

from config import log_queue, settings

logging.basicConfig(
	level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(message)s"
)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Разрешаем все источники для тестирования
    allow_credentials=True,
    allow_methods=["*"],  # Разрешаем все методы
    allow_headers=["*"],  # Разрешаем все заголовки
)

@app.middleware("http")
async def add_csp_header(request, call_next):
    response = await call_next(request)
    response.headers["Content-Security-Policy"] = (
        "default-src 'self'; "
        "connect-src 'self' ws://127.0.0.1:5500"  # Разрешаем WebSocket соединения с локального хоста
    )
    return response



connections: List[WebSocket] = []

@app.get("/test")
async def test():
	return "Hello World"


@app.websocket("/ws/logs")
async def logs(websocket: WebSocket):
	logging.debug("Attempting to accept connection")
	await websocket.accept()
	logging.debug("Connection accepted")

	connections.append(websocket)

	await websocket.send_text("<b>Running Log Console by BBot Team</b>")

	try:
		while True:
			while not log_queue.empty():
				log_entry = log_queue.get()

				for conn in connections:
					await conn.send_text(log_entry)
				await asyncio.sleep(0.25)  # Ожидание новых логов
			await asyncio.sleep(0.25)
	except WebSocketDisconnect:
		connections.remove(websocket)


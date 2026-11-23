import websocket
import json
import os

url = "wss://stream.binance.com:9443/ws/btcusdt@trade"

os.makedirs("data/raw", exist_ok=True)

def on_message(ws, message):
    data = json.loads(message)

    record = {
        "symbol": data["s"],
        "price": float(data["p"]),
        "quantity": float(data["q"]),
        "trade_time": data["T"],
        "trade_id": data["t"],
    }

    with open("data/raw/trades.jsonl", "a") as file:
        file.write(json.dumps(record) + "\n")

    print(record)

ws = websocket.WebSocketApp(
    url,
    on_message=on_message
)

ws.run_forever()
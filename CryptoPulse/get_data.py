
import websocket
import json

url = "wss://stream.binance.com:9443/ws/btcusdt@trade"

def on_message(ws, message):
    data = json.loads(message)

    print({
        "symbol": data["s"],
        "price": data["p"],
        "quantity": data["q"],
        "trade_time": data["T"]
    })

ws = websocket.WebSocketApp(
    url,
    on_message=on_message
)

ws.run_forever()

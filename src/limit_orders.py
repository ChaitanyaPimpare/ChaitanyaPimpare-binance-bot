import os
import sys
import logging
import uuid
from binance.client import Client
from dotenv import load_dotenv

# Load keys
load_dotenv()
api_key = os.getenv("BINANCE_API_KEY")
api_secret = os.getenv("BINANCE_API_SECRET")

# Logging setup
logging.basicConfig(filename='bot.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Init Spot Testnet client
client = Client(api_key, api_secret)
client.API_URL = 'https://testnet.binance.vision/api'

def place_oco_order(symbol, side, quantity, tp_price, sl_price, sl_limit_price):
    try:
        order = client.create_oco_order(
            symbol=symbol,
            side=side,
            quantity=quantity,
            price=tp_price,
            stopPrice=sl_price,
            stopLimitPrice=sl_limit_price,
            stopLimitTimeInForce='GTC'
        )
        logging.info(f"OCO Spot order placed: {order}")
        print(" Spot OCO order placed successfully.")
    except Exception as e:
        logging.error(f"Error placing Spot OCO order: {e}")
        print(" Failed to place Spot OCO order:", e)

if __name__ == "__main__":
    if len(sys.argv) != 7:
        print("Usage: python src/advanced/spot_oco.py <symbol> <BUY|SELL> <quantity> <tp_price> <sl_price> <sl_limit_price>")
        sys.exit(1)

    symbol = sys.argv[1].upper()
    side = sys.argv[2].upper()
    quantity = float(sys.argv[3])
    tp_price = str(sys.argv[4])
    sl_price = str(sys.argv[5])
    sl_limit_price = str(sys.argv[6])

    if side not in ["BUY", "SELL"]:
        print(" Invalid side. Use BUY or SELL.")
        sys.exit(1)

    place_oco_order(symbol, side, quantity, tp_price, sl_price, sl_limit_price)

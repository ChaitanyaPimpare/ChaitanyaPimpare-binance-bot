
import os
import sys
import logging
from binance.client import Client
from dotenv import load_dotenv

# Load API keys from .env file
load_dotenv()

api_key = os.getenv("BINANCE_API_KEY")
api_secret = os.getenv("BINANCE_API_SECRET")

# Initialize Binance client for SPOT TESTNET
client = Client(api_key, api_secret)
client.API_URL = 'https://testnet.binance.vision/api' 

# Setup logging
logging.basicConfig(
    filename='bot.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def place_market_order(symbol, side, quantity):
    try:
        order = client.create_order(
            symbol=symbol,
            side=side,
            type='MARKET',
            quantity=quantity
        )
        logging.info(f"Market order placed: {order}")
        print(" Market order placed successfully!")
    except Exception as e:
        logging.error(f"Error placing market order: {e}")
        print(" Error placing market order:", e)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python src/market_orders.py <symbol> <BUY|SELL> <quantity>")
        sys.exit(1)

    symbol = sys.argv[1].upper()
    side = sys.argv[2].upper()
    quantity = float(sys.argv[3])

    if side not in ["BUY", "SELL"]:
        print(" Invalid order side. Use BUY or SELL.")
        sys.exit(1)

    place_market_order(symbol, side, quantity)

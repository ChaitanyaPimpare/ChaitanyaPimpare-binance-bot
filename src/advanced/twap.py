import os
import sys
import time
import logging
from binance.client import Client
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("BINANCE_API_KEY")
api_secret = os.getenv("BINANCE_API_SECRET")

client = Client(api_key, api_secret)
client.API_URL = 'https://testnet.binance.vision/api'

# Logging
logging.basicConfig(filename='bot.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def place_twap_order(symbol, side, total_quantity, intervals, interval_seconds):
    qty_per_order = round(total_quantity / intervals, 4)

    print(f"🧠 TWAP: {intervals} × {qty_per_order} orders every {interval_seconds}s")

    for i in range(intervals):
        try:
            order = client.create_order(
                symbol=symbol,
                side=side,
                type='MARKET',
                quantity=qty_per_order
            )
            logging.info(f"TWAP order {i+1}/{intervals}: {order}")
            print(f" Order {i+1}/{intervals} placed")
        except Exception as e:
            logging.error(f"TWAP order {i+1} failed: {e}")
            print(f" Order {i+1} failed:", e)

        if i < intervals - 1:
            time.sleep(interval_seconds)

if __name__ == "__main__":
    if len(sys.argv) != 6:
        print("Usage: python src/twap_order.py <symbol> <BUY|SELL> <total_quantity> <intervals> <interval_seconds>")
        sys.exit(1)

    symbol = sys.argv[1].upper()
    side = sys.argv[2].upper()
    total_quantity = float(sys.argv[3])
    intervals = int(sys.argv[4])
    interval_seconds = int(sys.argv[5])

    place_twap_order(symbol, side, total_quantity, intervals, interval_seconds)

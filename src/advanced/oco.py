import os
import sys
import logging
from binance.client import Client
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_key = os.getenv("BINANCE_API_KEY")
api_secret = os.getenv("BINANCE_API_SECRET")

# Setup logging
logging.basicConfig(filename='bot.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Init client for Binance Futures Testnet
client = Client(api_key, api_secret)
client.FUTURES_BASE_URL = 'https://testnet.binancefuture.com'

def place_oco_like_order(symbol, side, quantity, tp_price, sl_price):
    try:
        opposite_side = "SELL" if side == "BUY" else "BUY"

        # Take-Profit Limit Order
        tp_order = client.futures_create_order(
            symbol=symbol,
            side=opposite_side,
            type='LIMIT',
            quantity=quantity,
            price=tp_price,
            timeInForce='GTC',
            reduceOnly=True
        )

        # Stop-Loss Market Order
        sl_order = client.futures_create_order(
            symbol=symbol,
            side=opposite_side,
            type='STOP_MARKET',
            stopPrice=sl_price,
            closePosition=True
        )

        logging.info(f"OCO-Like Orders placed: TP={tp_order['orderId']}, SL={sl_order['orderId']}")
        print("✅ OCO-like (TP + SL) orders placed!")

    except Exception as e:
        logging.error(f"OCO-like Order Error: {e}")
        print(" Error placing OCO order:", e)

if __name__ == "__main__":
    if len(sys.argv) != 6:
        print("Usage: python src/advanced/oco.py <symbol> <BUY|SELL> <quantity> <take_profit_price> <stop_loss_price>")
        sys.exit(1)

    symbol = sys.argv[1].upper()
    side = sys.argv[2].upper()
    quantity = float(sys.argv[3])
    tp_price = str(sys.argv[4])
    sl_price = str(sys.argv[5])

    if side not in ["BUY", "SELL"]:
        print(" Invalid side. Use BUY or SELL.")
        sys.exit(1)

    place_oco_like_order(symbol, side, quantity, tp_price, sl_price)

# 📈 Binance Futures Order Bot

A CLI-based trading bot designed for Binance **USDT-M Futures Testnet**, supporting core and advanced order types, including TWAP and OCO strategies, with structured logging and input validation.

---

## 🎯 Objective

Automate order placements on Binance Futures with:
- Core orders (Market, Limit)
- Advanced strategies (TWAP, OCO)
- CLI control
- Environment-based API key handling
- Robust logging

---

## 📁 Project Structure

binance_bot/
├── src/
│ ├── market_orders.py # Core: Market order logic
│ ├── limit_orders.py # Core: Limit order logic
│ └── advanced/
│ ├── oco.py # Advanced: Simulated OCO (TP + SL using Futures)
│ └── twap.py # Advanced: TWAP strategy
├── bot.log # Logs of all actions
├── .env # API keys (not committed)
├── report.pdf # Analysis, screenshots, explanation
└── README.md # Setup, usage instructions

---

## ⚙️ Setup

### 1. 📦 Install Dependencies

```bash
pip install python-binance python-dotenv

2. 🔐 Environment Variables
Create a .env file in the root directory:

env
BINANCE_API_KEY=your_testnet_api_key
BINANCE_API_SECRET=your_testnet_secret_key

3. ✅ Use Binance Futures Testnet
Generate keys from: https://testnet.binancefuture.com

Add test USDT via “Mock Trading” wallet

Ensure all calls use the testnet endpoint

🚀 How to Run (Examples)
▶️ Market Order
bash
python src/market_orders.py BTCUSDT BUY 0.01

▶️ Limit Order
bash
python src/limit_orders.py BTCUSDT SELL 0.02 61000

🧠 Advanced Orders
▶️ TWAP (Time-Weighted Average Price)
Split a large order into chunks over time.
bash
python src/advanced/twap.py BTCUSDT BUY 0.05 5 10
→ Buys 0.05 BTC in 5 chunks (0.01 each), every 10 seconds.

▶️ OCO (Take-Profit + Stop-Loss)
Simulate One-Cancels-the-Other using two Futures orders.
bash
python src/advanced/oco.py BTCUSDT SELL 0.01 61000 59000
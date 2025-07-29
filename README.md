# 📈 Binance Futures Order Bot

A CLI-based trading bot for the **Binance USDT-M Futures Testnet**, supporting both core (Market, Limit) and advanced (TWAP, OCO) order types. It includes structured logging, input validation, and uses environment variables for secure API handling.

---

## 🎯 Objective

Automate futures trading via command-line with:

- ✅ Market & Limit Orders  
- 🧠 TWAP (Time-Weighted Average Price)  
- 🔄 OCO (Simulated Take-Profit + Stop-Loss)  
- 🛡 Environment-secured API Keys  
- 📋 Structured Logging to `bot.log`

---

## 📁 Project Structure

```
binance_bot/
├── src/
│   ├── market_orders.py       # Market order logic
│   ├── limit_orders.py        # Limit order logic
│   └── advanced/
│       ├── oco.py             # OCO (TP + SL Simulation)
│       └── twap.py            # TWAP Strategy
├── bot.log                    # Action logs
├── .env                       # Secret API keys (not committed)
├── .env.example               # Example key structure
├── report.pdf                 # Report with screenshots & details
└── README.md                  # You're here!
```

---

## ⚙️ Setup Instructions

### 1️⃣ Install Python Dependencies

```bash
pip install python-binance python-dotenv
```

---

### 2️⃣ Create a `.env` File

Create a file named `.env` in the root directory and add your Binance Testnet API keys:

```env
BINANCE_API_KEY=your_testnet_api_key
BINANCE_API_SECRET=your_testnet_secret_key
```

> ⚠️ Do NOT commit `.env` to GitHub. Use `.env.example` to share key format safely.

---

### 3️⃣ Use Binance Futures Testnet

- Go to: [https://testnet.binancefuture.com](https://testnet.binancefuture.com)
- Create API Key with Futures trading access
- Add mock USDT from the "Mock Trading" section
- Ensure scripts use the testnet endpoint:

```python
client.FUTURES_URL = 'https://testnet.binancefuture.com'
```

---

## 🚀 How to Run (Example Commands)

### ▶️ Market Order

```bash
python src/market_orders.py BTCUSDT BUY 0.01
```

---

### ▶️ Limit Order

```bash
python src/limit_orders.py BTCUSDT SELL 0.02 61000
```

---

## 🧠 Advanced Orders

### ▶️ TWAP (Time-Weighted Average Price)

Splits a large order into smaller chunks over time.

```bash
python src/advanced/twap.py BTCUSDT BUY 0.05 5 10
```

➡️ Places 5 orders of 0.01 BTC every 10 seconds.

---

### ▶️ OCO (Simulated TP + SL)

Places two orders: a take-profit limit and a stop-loss market order.

```bash
python src/advanced/oco.py BTCUSDT SELL 0.01 61000 59000
```

➡️ Take-Profit at 61000  
➡️ Stop-Loss at 59000

---

## 📋 Logs

All actions are logged in `bot.log`. Example:

```
2025-07-27 10:31:45 - INFO - Market order placed: {'symbol': 'BTCUSDT', 'side': 'BUY', 'qty': 0.01}
2025-07-27 10:32:10 - INFO - TWAP Order 1/5 placed
2025-07-27 11:00:13 - ERROR - OCO Order Error: APIError(code=-2015)
```

---

## 🔐 Notes

- Add `.env`, `bot.log`, and `__pycache__/` to `.gitignore`.
- Never push `.env` to public repositories.
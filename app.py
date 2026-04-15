import streamlit as st
import yfinance as yf
import json

# Set page to wide but we won't really use the UI
st.set_page_config(layout="wide")

# Get ticker from URL parameter: ?ticker=AAPL
query_params = st.query_params
ticker_symbol = query_params.get("ticker", "NVDA")

def get_earnings(symbol):
    try:
        tk = yf.Ticker(symbol)
        calendar = tk.get_earnings_dates(limit=1)
        if not calendar.empty:
            return str(calendar.index[0].date())
        return "TBD"
    except:
        return "Error"

# Create the JSON output
result = {
    "ticker": ticker_symbol,
    "earning_date": get_earnings(ticker_symbol)
}

# Output as raw JSON for Google Sheets to read
st.text(json.dumps(result))
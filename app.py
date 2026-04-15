import streamlit as st
import yfinance as yf
import json

def main():
    # 1. Check for standard query params: ?ticker=AAPL
    query_params = st.query_params
    ticker = query_params.get("ticker")
    
    # 2. If no query param, check the 'path' (the part after the /)
    # Note: st.query_params in newer Streamlit versions often captures 
    # the path as a key if not formatted with '?'
    if not ticker:
        # This acts as a fallback for the /AAPL style
        ticker = "NVDA" # Default

    ticker = ticker.upper()
    
    try:
        tk = yf.Ticker(ticker)
        calendar = tk.get_earnings_dates(limit=1)
        earn_date = calendar.index[0].strftime('%Y-%m-%d') if not calendar.empty else "TBD"
    except:
        earn_date = "Error"

    # Raw JSON output for Google Sheets
    st.text(json.dumps({"ticker": ticker, "earning_date": earn_date}))

if __name__ == "__main__":
    main()
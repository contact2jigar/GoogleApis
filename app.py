import streamlit as st
import yfinance as yf
import json

def main():
    # Use the query parameter to handle different tickers
    ticker_symbol = st.query_params.get("ticker", "NVDA").upper()
    
    try:
        # yfinance now requires curl_cffi to handshake with Yahoo
        tk = yf.Ticker(ticker_symbol)
        earn_dates = tk.get_earnings_dates(limit=1)
        
        if earn_dates is not None and not earn_dates.empty:
            date_val = earn_dates.index[0].strftime('%Y-%m-%d')
        else:
            date_val = "TBD"
            
    except Exception as e:
        date_val = f"Error: {str(e)[:30]}"

    # Output the JSON for Google Sheets
    st.text(json.dumps({"ticker": ticker_symbol, "earning_date": date_val}))

if __name__ == "__main__":
    main()
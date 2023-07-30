# import module
import streamlit as st
import yfinance as yf
import datetime

# Title
st.write("Stock Price Analyzer !!!")


# symbol = "AAPL"

symbol = st.selectbox(
    "Which Stock Symbol do you want?", ("AAPL", "NFLX", "GOOG", "TSLA", "MSFT")
)

col1, col2 = st.columns(2)
with col1:
    start_date = st.date_input(
        "Start date", datetime.date(2019, 7, 6)
    )  # default dates 6th July and end date
with col2:
    end_date = st.date_input("Start date", datetime.date(2019, 7, 10))


ticker_data = yf.Ticker(symbol)
ticker_df = ticker_data.history(period="1d", start=start_date, end=end_date)

# Historical data is free but live data is paid
# Low - lowest
# Close- closing price.... and other terms mentioned in columns
st.write(f"""{symbol}'s Stock price data""")
st.dataframe(ticker_df)


st.write(f"""{symbol}'s Closing Price Chart""")

# Line Chart for Close
st.line_chart(ticker_df["Close"])

st.write(f"""{symbol}'s Volume Price Chart""")

# Line Chart for Volume
st.line_chart(ticker_df["Volume"])

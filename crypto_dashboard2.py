import streamlit as st
import requests
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
import plotly.graph_objects as go

# Function to fetch historical data from Binance API
def fetch_historical_data(symbol="BTCUSDT", interval="1h", limit=100):
    url = f"https://api.binance.com/api/v3/klines?symbol={symbol}&interval={interval}&limit={limit}"
    response = requests.get(url)
    data = response.json()
    df = pd.DataFrame(data, columns=[
        "Open time", "Open", "High", "Low", "Close", "Volume",
        "Close time", "Quote asset volume", "Number of trades",
        "Taker buy base asset volume", "Taker buy quote asset volume", "Ignore"
    ])
    df["Open"] = df["Open"].astype(float)
    df["Close"] = df["Close"].astype(float)
    df["High"] = df["High"].astype(float)
    df["Low"] = df["Low"].astype(float)
    df["Time"] = pd.to_datetime(df["Open time"], unit="ms")
    return df[["Time", "Open", "High", "Low", "Close"]]

# Train a simple Linear Regression model
def train_model(df):
    df["Next Close"] = df["Close"].shift(-1) # Target is next close price
    df = df[:-1] # Remove last row with NaN target
    X = df[["Open", "High", "Low", "Close"]]
    y = df["Next Close"]

    # Split into train and test sets (80% train, 20% test)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Evaluate the model on the test set
    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)  # Calculate MAE
    r2 = r2_score(y_test, y_pred)  # Calculate R² Score

    return model, mae, r2, X_test, y_test, y_pred

# Streamlit layout
st.sidebar.title("Crypto 🪙 Currency Dashboard")
st.title("Crypto 🪙 Currency with Prediction")

# Select symbol
symbol = st.sidebar.selectbox("Select Cryptocurrency Pair", ["BTCUSDT", "ETHUSDT", "BNBUSDT", "ADAUSDT", "SOLUSDT"])

# Fetch historical data
st.write(f"### Historical Data for {symbol}")
historical_data = fetch_historical_data(symbol)
st.dataframe(historical_data)

# Train model and display accuracy
model, mae, r2, X_test, y_test, y_pred = train_model(historical_data)
st.write("### Model Evaluation")
st.metric("Mean Absolute Error (MAE)", f"{mae:.2f}")
st.metric("R² Score", f"{r2:.2f}")

# Add a chart to display predictions vs actual
st.write("### Prediction vs Actual")
fig = go.Figure()
fig.add_trace(go.Scatter(x=y_test.index, y=y_test, mode="lines", name="Actual"))
fig.add_trace(go.Scatter(x=y_test.index, y=y_pred, mode="lines", name="Predicted"))
fig.update_layout(title="Prediction vs Actual Close Prices", xaxis_title="Index", yaxis_title="Price", template="plotly_dark")
st.plotly_chart(fig)

# Add future prediction
st.write("### Future Prediction")
last_row = historical_data.iloc[-1][["Open", "High", "Low", "Close"]].values.reshape(1, -1)
next_prediction = model.predict(last_row)[0]
st.metric("Predicted Next Close Price", f"${next_prediction:.2f}")
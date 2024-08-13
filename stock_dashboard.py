import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf
from datetime import date, timedelta

# Setting up the dashboard title and sidebar
st.title('Stock Analysis Dashboard')
st.sidebar.title('Stock Selection and Settings')

# Select the stock tickers
tickers = st.sidebar.multiselect(
    'Select stock tickers:',
    options=['RELIANCE.NS', 'TCS.NS', 'INFY.NS', 'HDFCBANK.NS'],
    default=['RELIANCE.NS', 'TCS.NS']
)

# Define the time period for the data
end = date.today().strftime("%Y-%m-%d")
start = st.sidebar.date_input('Start date', value=date.today() - timedelta(days=365))
start = start.strftime("%Y-%m-%d")

# Download the stock data
if tickers:
    data = yf.download(tickers=tickers, start=start, end=end, progress=True)
    st.write(data.head())
    
    # Resetting the index
    data = data.reset_index()

    # Melting the DataFrame
    data_melted = data.melt(id_vars=['Date'], var_name=['Attribute', 'Ticker'])

    # Pivot the melted data
    data_pivoted = data_melted.pivot_table(index=['Date', 'Ticker'], columns='Attribute', values='value', aggfunc='first')

    # Reset index to turn multi-index into columns
    stock_data = data_pivoted.reset_index()

    # Converting the Date column to datetime
    stock_data['Date'] = pd.to_datetime(stock_data['Date'])

    # Set the index to Date
    stock_data = stock_data.set_index('Date')

    # Plotting the stock prices
    st.subheader('Stock Prices Over Time')
    plt.figure(figsize=(20, 8))
    sns.lineplot(data=stock_data, x='Date', y='Adj Close', hue='Ticker')
    plt.title('Stock price over time')
    plt.xlabel('Date')
    plt.ylabel('Adjusted Close Price')
    plt.legend(loc='upper left')
    sns.set(style='darkgrid')
    plt.xticks(rotation=30)
    st.pyplot(plt)

    # Calculating the moving averages
    short_window = st.sidebar.slider('Short Moving Average Window', 10, 100, 50)
    long_window = st.sidebar.slider('Long Moving Average Window', 100, 300, 200)

    # Setting unique tickers
    un_tickers = stock_data['Ticker'].unique()

    # Loop through the data, calculate moving averages, and plot the results
    for ticker in un_tickers:
        ticker_df = stock_data[stock_data['Ticker'] == ticker].copy()

        # Calculate rolling mean for short and long windows
        ticker_df['Short_MA'] = ticker_df['Close'].rolling(window=short_window).mean()
        ticker_df['Long_MA'] = ticker_df['Close'].rolling(window=long_window).mean()

        # Plotting the data
        st.subheader(f'{ticker} - Close Prices and Moving Averages')
        plt.figure(figsize=(12, 6))
        plt.plot(ticker_df.index, ticker_df['Close'], label='Close Price', alpha=0.5)
        plt.plot(ticker_df.index, ticker_df['Short_MA'], label=f'Short MA ({short_window} days)', linewidth=2)
        plt.plot(ticker_df.index, ticker_df['Long_MA'], label=f'Long MA ({long_window} days)', linewidth=2)
        plt.title(f'{ticker} - Close Prices and Moving Averages')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.legend()
        sns.set(style='darkgrid')
        plt.tight_layout()
        plt.xticks(rotation=30)
        st.pyplot(plt)

        # Plotting the volume traded
        st.subheader(f'{ticker} - Volume Traded')
        plt.figure(figsize=(12, 6))
        plt.bar(ticker_df.index, ticker_df['Volume'], label='Volume Traded', alpha=0.5)
        plt.title(f'{ticker} - Volume Traded')
        plt.xlabel('Date')
        plt.ylabel('Volume')
        plt.legend()
        sns.set(style='darkgrid')
        plt.tight_layout()
        plt.xticks(rotation=30)
        st.pyplot(plt)

    # Calculating daily returns
    stock_data['Daily_returns'] = stock_data.groupby('Ticker')['Close'].pct_change()

    # Plotting the distribution of daily returns
    st.subheader('Distribution of Daily Returns')
    plt.figure(figsize=(15, 8))
    sns.set(style='darkgrid')
    for ticker in un_tickers:
        ticker_df1 = stock_data[stock_data['Ticker'] == ticker]
        sns.histplot(ticker_df1['Daily_returns'].dropna(), bins=50, kde=True, label=ticker, alpha=0.5)
    plt.title('Distribution of Daily Returns', fontsize=17)
    plt.xlabel('Daily Return')
    plt.ylabel('Frequency')
    plt.legend(title='Ticker', title_fontsize='13', fontsize='11')
    plt.grid(True)
    plt.tight_layout()
    plt.xticks(rotation=30)
    st.pyplot(plt)

    # Calculating the correlation matrix
    st.subheader('Correlation Matrix of Daily Returns')
    stock_pivot = stock_data.pivot_table(index='Date', columns='Ticker', values='Daily_returns')
    correlation_matrix = stock_pivot.corr()

    # Plotting the heatmap of the correlation matrix
    plt.figure(figsize=(12, 10))
    sns.set(style='whitegrid')
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
    plt.title('Correlation Matrix of Daily Returns', fontsize=16)
    plt.xticks(rotation=30)
    plt.yticks(rotation=30)
    plt.tight_layout()
    st.pyplot(plt)

    # Calculating expected returns and volatility
    st.subheader('Expected Returns and Volatility')
    expected_returns = stock_pivot.mean() * 252  # annualize the returns
    volatility = stock_pivot.std() * np.sqrt(252)  # annualize the volatility

    # Creating a DataFrame for returns and volatility
    stock_stats = pd.DataFrame({
        'Expected Returns': expected_returns,
        'Volatility': volatility
    })
    st.write(stock_stats)


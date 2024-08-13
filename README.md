

# Stock Analysis Dashboard

This Streamlit application provides an interactive dashboard to analyze the historical performance of selected stocks. The dashboard enables users to visualize stock prices, moving averages, volume traded, and daily returns. Additionally, it calculates and displays the correlation matrix between stocks and their expected returns and volatility.

## Features

- **Stock Price Visualization**: Line plots showing adjusted close prices over a selected time period.
- **Moving Averages**: Visualization of short-term and long-term moving averages for each selected stock.
- **Volume Traded**: Bar charts displaying the volume of stocks traded over time.
- **Daily Returns Distribution**: Histograms representing the distribution of daily returns for each stock.
- **Correlation Matrix**: Heatmap showing the correlation between the daily returns of the selected stocks.
- **Expected Returns and Volatility**: Table displaying the annualized expected returns and volatility of each stock.

## Prerequisites

- Python 3.x
- Streamlit
- Required Python libraries:
  - `numpy`
  - `pandas`
  - `matplotlib`
  - `seaborn`
  - `yfinance`
  
You can install the necessary libraries by running:
```bash
pip install requirements.txt
```

## How to Run the Application

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/YvvonM/portfolio_optimization.git
   ```
   
2. **Navigate to the project directory**:
   ```bash
   cd stock-analysis-dashboard
   ```
   
3. **Run the Streamlit application**:
   ```bash
   streamlit run stock_dashboard.py
   ```

4. **Open the application**: After running the above command, the application should automatically open in your default web browser. If not, open your browser and navigate to the local server URL provided in the terminal.

## Usage

1. **Select Stock Tickers**: Use the sidebar to select the stock tickers you wish to analyze. The options available are `RELIANCE.NS`, `TCS.NS`, `INFY.NS`, and `HDFCBANK.NS`.
   
2. **Set the Time Period**: Choose the start date for the analysis period. The end date defaults to the current date.

3. **Adjust Moving Averages**: Set the short-term and long-term moving average windows using the sliders in the sidebar.

4. **Explore Visualizations**: The dashboard will update to reflect your selections, providing insights into stock performance, correlations, and expected returns.

## Example Dashboard
![Screenshot from 2024-08-13 11-22-54](https://github.com/user-attachments/assets/eedf4724-ad90-40ae-b5d0-198aba295c03)


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request if you have any improvements or suggestions.

## Contact

For any questions or feedback, please reach out to [Yvvon Majala](mailto:yvvonjemymahmajala@gmail.com).


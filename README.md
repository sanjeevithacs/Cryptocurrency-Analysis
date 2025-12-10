# Cryptocurrency-Analysis


A Streamlit-based web application for analyzing cryptocurrency price data and making simple price predictions using machine learning.

## Features

- Real-time cryptocurrency price data from Binance API
- Interactive price charts using Plotly
- Simple price prediction using Linear Regression
- Support for multiple cryptocurrencies
- Adjustable time intervals for analysis

## Prerequisites

- Python 3.8+
- pip (Python package manager)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/sanjeevithacs/Cryptocurrency-Analysis.git
   cd Cryptocurrency-Analysis
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

   Or install them individually:
   ```bash
   pip install streamlit requests pandas numpy scikit-learn plotly
   ```

## Usage

1. Run the Streamlit application:
   ```bash
   streamlit run crypto_dashboard2.py
   ```

2. The application will open in your default web browser at `http://localhost:8501`

3. Use the sidebar to:
   - Select different cryptocurrencies
   - Choose time intervals
   - Adjust the number of data points

## Features in Detail

- **Price Visualization**: Interactive candlestick charts showing open, high, low, and close prices
- **Price Prediction**: Simple linear regression model to predict future price movements
- **Technical Indicators**: Basic technical analysis indicators
- **Responsive Design**: Works on both desktop and mobile devices

## Project Structure

```
cryptocurrency-analysis/
├── crypto_dashboard2.py     # Main application file
├── README.md                # This file
└── requirements.txt         # Project dependencies
```

## Dependencies

- streamlit
- requests
- pandas
- numpy
- scikit-learn
- plotly

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This application is for educational purposes only. The predictions provided by this application should not be considered as financial advice. Always do your own research before making any investment decisions.

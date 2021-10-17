# Libreries
from pycoingecko import CoinGeckoAPI
import pandas as pd
import streamlit as st

# Activate API connection
cg = CoinGeckoAPI()

MarketData = cg.get_coins_markets(vs_currency='usd', per_page=250, page=1)
MarketData = pd.DataFrame(MarketData)
#print(MarketData)


st.markdown('''# **CryptoMarket App**
A simple cryptocurrency price app pulling price data from *CoinGecko*.
''')

st.header('** Top 250 Crypto by Market Cap **')
st.markdown('''Top 5 Crypto by MarketCap''')

st.header('** Top 250 Crypto by Market Cap **')

name = 'BTCUSD'
price = 60000
perc = f'{0.05}%'

col1, col2, col3, col4, col5 = st.columns(5)
st.markdown('''Top 5 Crypto by Market Captalisation''')
col1.metric(name, price, perc)
col2.metric(name, price, perc)
col3.metric(name, price, perc)
col4.metric(name, price, perc)
col5.metric(name, price, perc)

st.markdown('''Top 5 performers (24h)''')
col1.metric(name, price, perc)
col2.metric(name, price, perc)
col3.metric(name, price, perc)
col4.metric(name, price, perc)
col5.metric(name, price, perc)

st.markdown('''Worst 5 performers (24h)''')
col1.metric(name, price, perc)
col2.metric(name, price, perc)
col3.metric(name, price, perc)
col4.metric(name, price, perc)
col5.metric(name, price, perc)

st.header('**All Price**')
st.dataframe(MarketData)

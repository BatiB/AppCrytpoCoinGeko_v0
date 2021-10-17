# Libreries
from pycoingecko import CoinGeckoAPI
import pandas as pd
import streamlit as st

# Activate API connection
cg = CoinGeckoAPI()

MarketData = cg.get_coins_markets(vs_currency='usd', per_page=250, page=1)
MarketData = pd.DataFrame(MarketData)
#print(MarketData)

name = 'BTCUSD'
price = 61234.56
perc = f'{5.15}%'

# ------------------
#       App
# ------------------

st.markdown('''# ** Bati CryptoMarket App**
A simple cryptocurrency price app pulling price data from *CoinGecko*.
''')
st.header('** Top 250 Crypto by Market Cap **')

st.markdown('')
st.markdown('''Top 5 Crypto by Market Captalisation''')
col1, col2, col3, col4, col5 = st.columns(5)

col1.metric(name, price, perc)
col2.metric(name, price, perc)
col3.metric(name, price, perc)
col4.metric(name, price, perc)
col5.metric(name, price, perc)

st.markdown('')
st.markdown('''Top 5 performers (24h)''')
col1, col2, col3, col4, col5 = st.columns(5)
col1.metric(name, price, perc)
col2.metric(name, price, perc)
col3.metric(name, price, perc)
col4.metric(name, price, perc)
col5.metric(name, price, perc)

st.markdown('')
st.markdown('''Worst 5 performers (24h)''')
col1, col2, col3, col4, col5 = st.columns(5)
col1.metric(name, price, perc)
col2.metric(name, price, perc)
col3.metric(name, price, perc)
col4.metric(name, price, perc)
col5.metric(name, price, perc)

st.header('**All Price**')
st.dataframe(MarketData)

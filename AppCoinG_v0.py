# Libreries
from pycoingecko import CoinGeckoAPI
import pandas as pd
import streamlit as st

# Activate API connection
cg = CoinGeckoAPI()

MarketData = cg.get_coins_markets(vs_currency='usd', per_page=250, page=1)
MarketData = pd.DataFrame(MarketData)
#print(MarketData)

Col1 = MarketData.loc[[0], ['name', 'current_price', 'price_change_percentage_24h']]
#print(Col1)

st.markdown('''# **CryptoMarket App**
A simple cryptocurrency price app pulling price data from *CoinGecko*.
''')

st.header('** TOP 100 CRYPTO **')


st.markdown('''Top 5 Crypto per MarketCap''')
col1, col2, col3, col4, col5 = st.columns(5)
col1.metric(Col1['name'], Col1['current_price', Col1['price_change_percentage_24h']])


#col2.metric(MarketData.loc[[1], ['name', 'current_price', 'price_change_percentage_24h']])
#col3.metric(MarketData.loc[[2], ['name', 'current_price', 'price_change_percentage_24h']])
#col4.metric(MarketData.loc[[3], ['name', 'current_price', 'price_change_percentage_24h']])
#col5.metric(MarketData.loc[[4], ['name', 'current_price', 'price_change_percentage_24h']])

st.header('**All Price**')
st.dataframe(MarketData)

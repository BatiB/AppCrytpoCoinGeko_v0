# Libreries
from pycoingecko import CoinGeckoAPI
import pandas as pd
import streamlit as st

# Activate API connection
cg = CoinGeckoAPI()

MarketData = cg.get_coins_markets(vs_currency='usd', per_page=250, page=1)
MarketData = pd.DataFrame(MarketData)

MarketData.set_index('market_cap_rank', inplace=True)
MarketData.drop(['id', 'image', 'fully_diluted_valuation', 'total_volume', 'high_24h', 'low_24h', 'price_change_24h', 'market_cap_change_24h', 'market_cap_change_percentage_24h', 'max_supply', 'atl', 'atl_change_percentage', 'atl_date', 'roi', 'last_updated'], axis=1, inplace=True)

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
st.header('** Highlights **')

st.markdown('')
st.markdown('Top 5 Crypto')
col1, col2, col3, col4, col5 = st.columns(5)

col1.metric(name, price, perc)
col2.metric(name, price, perc)
col3.metric(name, price, perc)
col4.metric(name, price, perc)
col5.metric(name, price, perc)

st.markdown('')
st.markdown('Top 5 performers (24h)')
col1, col2, col3, col4, col5 = st.columns(5)
col1.metric(name, price, perc)
col2.metric(name, price, perc)
col3.metric(name, price, perc)
col4.metric(name, price, perc)
col5.metric(name, price, perc)

st.markdown('')
st.markdown('Worst 5 performers (24h)')
col1, col2, col3, col4, col5 = st.columns(5)
col1.metric(name, price, perc)
col2.metric(name, price, perc)
col3.metric(name, price, perc)
col4.metric(name, price, perc)
col5.metric(name, price, perc)

st.header('**Top 250 by Market Capitalisation**')
#st.dataframe(MarketData)

col1, col2, col3 = st.columns(3)

N = 10
#rank = np.linspace(1, N, N)
#rank = rank.astype(int)
rank1 = [1,2,3,4,5,6,7,8,9,10]
name1 = ['BTCUSD'] * N
price1 = [61234.56] * N
perc1 = [f'{0.05}%'] * N


for i in range(0, 10):
    cols = st.columns(4)
    cols[0].write(rank1[i])
    cols[1].write(name1[i])
    cols[2].write(price1[i])
    cols[3].write(perc1[i])


#for i in range(N):
#  col1.metric(name1[i], price1[i], perc1[i])
#  col2.metric(name1[i], price1[i], perc1[i])
#  col3.metric(name1[i], price1[i], perc1[i])




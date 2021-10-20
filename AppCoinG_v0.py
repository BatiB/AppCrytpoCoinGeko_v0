# Libreries
from pycoingecko import CoinGeckoAPI
import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

# Activate API connection
cg = CoinGeckoAPI()

# Get Data
MarketData = cg.get_coins_markets(vs_currency='usd', per_page=250, page=1)
MarketData = pd.DataFrame(MarketData)
MarketData.set_index('market_cap_rank', inplace=True)
MarketData.drop(['id', 'image', 'fully_diluted_valuation', 'total_volume', 'high_24h', 'low_24h', 'price_change_24h', 'market_cap_change_24h', 'market_cap_change_percentage_24h', 'max_supply', 'atl', 'atl_change_percentage', 'atl_date', 'roi', 'last_updated'], axis=1, inplace=True)

# Sort Change 24H % Max
Max_MarketData = MarketData.copy()
Max_MarketData.sort_values(by=['price_change_percentage_24h'], ascending=False, inplace=True)

# Sort Change 24H % min
Min_MarketData = MarketData.copy()
Min_MarketData.sort_values(by=['price_change_percentage_24h'], ascending=True, inplace=True)

name = 'BTCUSD'
price = 61234.56
perc = f'{5.15}%'

# ------------------
#       App
# ------------------

st.markdown('''# ** Bati CryptoMarket App**
A simple cryptocurrency price app pulling price data from *CoinGecko*.
''')

# Table 1
st.header('** Highlights **')

st.markdown('')
st.markdown('Top 5 Crypto')

cols = st.columns(5)
for i in range(5):
    name1 = MarketData.iloc[i]['name']
    price1 = MarketData.iloc[i]['current_price']
    perc1 = MarketData.iloc[i]['price_change_percentage_24h']
                
    cols[i].metric(name1, price1, f'{perc1}%')

st.markdown('')
st.markdown('Top 5 performers (24h)')

cols = st.columns(5)
for i in range(5):
    name1 = Max_MarketData.iloc[i]['name']
    price1 = Max_MarketData.iloc[i]['current_price']
    perc1 = Max_MarketData.iloc[i]['price_change_percentage_24h']
                
    cols[i].metric(name1, price1, f'{perc1}%')

st.markdown('')
st.markdown('Worst 5 performers (24h)')

cols = st.columns(5)
for i in range(5):
    name1 = Min_MarketData.iloc[i]['name']
    price1 = Min_MarketData.iloc[i]['current_price']
    perc1 = Min_MarketData.iloc[i]['price_change_percentage_24h']
                
    cols[i].metric(name1, price1, f'{perc1}%')

# ------------------------------
# Table 2
st.markdown('')
st.header('**Top 10 by Market Capitalisation**')

N = 10
#rank = np.linspace(1, N, N)
#rank = rank.astype(int)
rank1 = [1,2,3,4,5,6,7,8,9,10]
name1 = ['BTCUSD'] * N
price1 = [61234.56] * N
perc1 = [f'{0.05}%'] * N

cols = st.columns(6)

# head
cols[0].write('RANK')
cols[1].write('SYMBOL')
cols[2].write('PRICE')
cols[3].write('24H (%)')
cols[4].write('XXXX')
cols[5].write('YYYY')

# fill table
for i in range(0, 10):    
    cols[0].write(f'{rank1[i]}')
    cols[1].write(name1[i])
    cols[2].write(f'{price1[i]}')
    cols[3].write(perc1[i])
    cols[4].write(f'{price1[i]}')
    cols[5].write(f'{price1[i]}')

# ------------------------------
# Table 3

st.markdown('')
st.header('**Top 250 by Market Capitalisation**')
st.dataframe(MarketData)

st.markdown('')
st.write(MarketData)

# ------------------------------
# Test Plotly

st.markdown('')
st.header('**Line Plot**')

a = np.linspace(1,10,10)
b = a ** 2

plotly_figure = px.line(x = a,
                        y = b,
                       title = 'trial')

st.plotly_chart(plotly_figure)
# ------------------------------
st.markdown('')
st.header('**Scatter Plot**')

fig0 = px.scatter(x=[0, 1, 2, 3, 4],
                 y=[0, 1, 4, 9, 16])

st.plotly_chart(fig0)

# ------------------------------
st.markdown('')
st.header('**Scatter Plot 1**')

c = np.linspace(1,10,10)
d = a ** 2

# Fig 1
fig1 = px.scatter(x = c,
                   y = d,
                  color = c)

st.plotly_chart(fig1)

# Fig 2
fig2 = px.scatter(x = c,
                  y = d,
                  color = c,
                  color_continuous_scale=px.colors.sequential.Viridis)

st.plotly_chart(fig2)

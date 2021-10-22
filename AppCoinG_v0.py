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
# ------------------------------
# Line
# ------------------------------

st.markdown('')
st.header('**Line Plot**')

a = np.linspace(1,10,10)
b = a ** 2

plotly_figure = px.line(x = a,
                        y = b,
                       title = 'trial')

st.plotly_chart(plotly_figure)

# ------------------------------
# Scatter
# ------------------------------

st.markdown('')
st.header('**Scatter Plot**')

c = np.linspace(1,10,10)
d = c ** 2

# Fig 1
Temp = ["plotly", "plotly_white", "plotly_dark", "ggplot2", "seaborn", "simple_white", "none"]

fig1 = px.scatter(x = c,
                   y = d,
                  color = c,
                  color_continuous_scale=px.colors.sequential.Inferno,
                  template=Temp[5])

st.plotly_chart(fig1)

# ------------------------------
# Fig 2
#Temp = 'plotly_dark'
fig2 = px.scatter(x = c,
                  y = d,
                  color = c,
                  color_continuous_scale=px.colors.sequential.Viridis,
                  template=Temp[2])

st.plotly_chart(fig2)

# ------------------------------
# Histogram
# ------------------------------
# Fig 3

st.markdown('')
st.header('**Histogram**')

e = np.linspace(1,100,100)
f = np.log(e)

fig3 = px.bar(x = e, y = f, labels={'x':'total_bill', 'y':'count'})
st.plotly_chart(fig3)

# ------------------------------
# Fig 4

e = np.linspace(1,100,100)
f = np.log(e)

fig4 = px.bar(x = e,
              y = f,
              labels={'x':'total_bill', 'y':'count'},
              color = f)
st.plotly_chart(fig4)

# ------------------------------
# Fig 5

e = np.linspace(1,100,100)
f = np.log(e)

fig5 = px.bar(x = e,
              y = f,
              labels={'x':'total_bill', 'y':'count'},
              color = f,
              color_continuous_scale=px.colors.sequential.Viridis,
              template = Temp[2])
st.plotly_chart(fig5)

# ------------------------------
# Time series
# ------------------------------

st.markdown('')
st.header('**Time series**')

# ------------------------------
# Not working (error datetime)

#HistoryPrice = cg.get_coin_market_chart_by_id(id='ethereum', vs_currency='usd', days=295)
#HistoryPrice = pd.DataFrame(HistoryPrice)

#PriceHist = pd.DataFrame(HistoryPrice['prices'])
#PriceHist.rename(columns={0: 'Date', 1: 'Price'}, inplace=True)
#PriceHist['Date'] = pd.to_datetime(PriceHist['Date'], unit='ms')

#fig6 = px.line(df, x='Date', y='Price', title='Time Series with Rangeslider')
#fig6.update_xaxes(rangeslider_visible=True)
#st.plotly_chart(fig6)
# ------------------------------
# Fig 7

df1 = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')
fig7 = px.line(df1, x='Date', y='AAPL.High', title='Time Series with Rangeslider')
fig7.update_xaxes(rangeslider_visible=True)

st.plotly_chart(fig7)

# ------------------------------
# Fig 8

df1 = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')
fig8 = px.line(df1, x='Date', y='AAPL.High', title='Time Series with Rangeslider')
fig8.update_xaxes(rangeslider_visible=True)

fig8.update_xaxes(
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(count=1, label="1m", step="month", stepmode="backward"),
            dict(count=6, label="6m", step="month", stepmode="backward"),
            dict(count=1, label="YTD", step="year", stepmode="todate"),
            dict(count=1, label="1y", step="year", stepmode="backward"),
            dict(step="all")
        ])
    )
)

st.plotly_chart(fig8)





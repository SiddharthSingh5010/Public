import pandas as pd 
import matplotlib.pyplot as plt
from pycoingecko import CoinGeckoAPI
cg=CoinGeckoAPI()
btd=cg.get_coin_market_chart_by_id(id='bitcoin',vs_currency='usd',days=90)
t=btd['prices']
data=pd.DataFrame(t,columns=['Timestamp','Price'])
data['Date']=pd.to_datetime(data['Timestamp'],unit='ms')
data.drop('Timestamp',axis=1)
fig = plt.figure(figsize=(20, 5))
ax = fig.add_subplot(111)
ax.set_ylabel("Price")
ax.set_xlabel("Date")
ax.set_title("BITCOIN CHART")
ax.grid()
ax.plot(data['Date'],data['Price'])
plt.show()
#import libraries

import pandas as pd
import pandas_datareader.data as pdr
import datetime
from datetime import date
#import libraries
import plotly.offline as py
import plotly.graph_objs as go

start = datetime.datetime(2021,2,19)
end = date.today()
df = pdr.DataReader('btc-USD','yahoo',start,end)


data = [go.Candlestick(x=df.index,
                       open=df.Open,
                       high=df.High,
                       low=df.Low,
                       close=df.Close)]

layout = go.Layout(title='Bitcoin Candlestick with Range Slider',
                   xaxis={'rangeslider':{'visible':True}})

fig = go.Figure(data=data,layout=layout)

py.iplot(fig,filename='bitcoin_candlestick')

numbers = list(df.High)
window_size = 20

i = 0
moving_averages = []

while i < len(numbers) - window_size + 1:
    this_window = numbers[i : i + window_size]
    #get current window
    window_average = sum(this_window) / window_size
    moving_averages.append(window_average)
    i += 1

#print( moving_averages )

moving_averages

from matplotlib import pyplot as plt

plt.show(moving_averages)

plt.plot(t, moving_averages)

plt.xlabel('time (s)')
plt.ylabel('voltage (mV)')
plt.title('About as simple as it gets, folks')
plt.grid(True)
plt.savefig("test.png")
plt.show()

df
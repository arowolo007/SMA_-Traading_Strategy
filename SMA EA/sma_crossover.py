import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('/Users/Arowolo/OneDrive/Desktop/loreon058/SMA EA/TSLA.csv')
data = data.set_index(pd.DatetimeIndex(data['Date']))
data = data.drop('Date', axis=1)

price = data[['Close']]
price.columns = ['close']

# create 20 days simple moving average column
price['20_SMA'] = price['close'].rolling(window = 20, min_periods = 1).mean()

# create 50 days simple moving average column
price['50_SMA'] = price['close'].rolling(window = 50, min_periods = 1).mean()


from pandas_datareader import data as pdr
import matplotlib.pyplot as plt
import yfinance as yfin
from datetime import datetime

yfin.pdr_override()

start_date = datetime(2007,1,1)
end_date = datetime(2020,3,3)

kospi = pdr.get_data_yahoo('AAPL', start_date, end_date)

fig = plt.figure(figsize=(12, 4), dpi=300)

plt.plot(kospi['High'], label="KOSPI", color='#b000b0')
plt.show()

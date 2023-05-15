from pandas_datareader import data as pdr
import matplotlib.pyplot as plt
import yfinance as yfin
yfin.pdr_override()

lge = pdr.get_data_yahoo('066570.KS')
sec = pdr.get_data_yahoo('005930.KS')

fig = plt.figure(figsize=(12, 4), dpi=300)

plt.plot(lge['Close'], label="LGE", color='C3')
plt.plot(sec['Close'], label="SEC", color='C0')

plt.grid(True, linestyle='-.')
plt.legend()
plt.show()

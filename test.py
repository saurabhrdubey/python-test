from nsepy import get_history
from datetime import date
import pandas as pd
from nsepy.derivatives import get_expiry_date
expiry = get_expiry_date(year=2015, month=12)
print expiry
tcs = get_history(symbol='TCS',start=date(2015,1,1),end=date(2015,12,31))
print tcs
tcs.insert(0, 'Date',  pd.to_datetime(tcs.index,format='%Y-%m-%d') )
type(tcs.index)
c = type(tcs.Date)
print c
tcs.to_csv('tcs_stock.csv', encoding='utf-8', index=False)

#############################################################
infy = get_history(symbol='INFY',start=date(2015,1,1),end=date(2015,12,31))
print infy
infy.insert(0,'Date',pd.to_datetime(infy.index,format='%Y-%m-%d'))
print(type(infy.index))
print(type(infy.Date))
infy.Date.dt
infy.to_csv('infy_stock.csv', encoding='utf-8', index=False)

#############################################################
nifty_it = get_history(symbol="NIFTYIT",start=date(2015,1,1),end=date(2015,12,31),index=True)
print nifty_it
nifty_it.insert(0, 'Date',  pd.to_datetime(nifty_it.index,format='%Y-%m-%d'))
print(type(nifty_it.index))
print(type(nifty_it.Date))
nifty_it.Date.dt
nifty_it.to_csv('nifty_it_index.csv', encoding='utf-8', index=False)

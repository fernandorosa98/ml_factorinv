import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

os.chdir('C:\\Users\\ferna\\OneDrive\\Downloads\\Code\\Python\\ML_Factor')

data_raw = pd.read_csv('data/data_ml.csv', index_col=0) 

idx_date = (data_raw['date'] > '1999-12-31') & (data_raw['date'] < '2019-01-01')
data_ml = data_raw.loc[idx_date,:].copy()

data_ml['date'] = pd.to_datetime(data_ml['date'], format = '%Y-%m-%d')

features=list(data_ml.iloc[:,3:95].columns) # Keep the feature's column names (hard-coded, beware!)
features_short =["Div_Yld", "Eps", "Mkt_Cap_12M_Usd", "Mom_11M_Usd", "Ocf", "Pb", "Vol1Y_Usd"]

df_median = data_ml.loc[:,['date','R1M_Usd','R12M_Usd']].groupby('date').median()
df_median.columns = ['R1M_Usd_median','R12M_Usd_median']

df = pd.merge(data_ml,df_median, how = 'left', on = 'date')
    
data_ml['R1M_Usd_C'] = np.where(df['R1M_Usd']>df['R1M_Usd_median'],1,0)
data_ml['R12M_Usd_C'] = np.where(df['R12M_Usd']>df['R12M_Usd_median'],1,0)

sep_date  = '2014-01-15'
idx_train = data_ml['date'].index[data_ml['date'] < sep_date]
idx_test  = data_ml['date'].index[data_ml['date'] >= sep_date]

sep_val  = '2010-01-15'
sep_test = '2014-01-15'
idx_train2 = data_ml['date'].index[(data_ml['date'] < sep_val)]
idx_val2   = data_ml['date'].index[(data_ml['date'] >= sep_val) & (data_ml['date'] < sep_test)]
idx_test2  = data_ml['date'].index[data_ml['date'] >= sep_test]

stock_ids  = data_ml['stock_id'].unique() # ids of stocks.
stock_days = data_ml[['date','stock_id']].groupby('stock_id').count().reset_index() # number of dates per stock_id.
stock_ids_short = stock_days[stock_days.loc[:,'date'] == stock_days.loc[:,'date'].max()].loc[:,'stock_id'].to_list() # stocks present in all days.
is_stock_ids_short = data_ml['stock_id'].isin(stock_ids_short)

returns = data_ml[is_stock_ids_short].pivot(index = 'date', columns = 'stock_id', values = 'R1M_Usd')

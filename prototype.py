from math import exp, expm1
import pandas as pd
import numpy as np
import math


### Process: To be completed

### Read data

def read_news_data(news_path):
    '''Read news file'''

    df = pd.read_csv(news_path)
    # Filter out only when EUR have either positive or negative sentiment
    df.rename(columns={'EUR_sent':'ccy_sent'}, inplace=True)
    df = df[df['ccy_sent'].isin(['Negative', 'Very Negative', 'Positive', 'Very Positive'])]
    # Change the sentiment result to numeric value
    df['ccy_sent'].replace({'Positive': 60, 'Very Positive': 60, 'Negative': 60, 'Very Negative': 60}, inplace=True)
    # Adjust the newsTime to the minutes level to align with min level market data
    df.newsTime = pd.to_datetime(df.newsTime)
    df['newsTime'] = df['newsTime'].apply(lambda x: x.ceil('min'))
    # Remove the unrelated columns in news dataframe
    df = df[['newsTime', 'ccy_sent']]

    return df

def read_market_data(market_path):
    '''read and process minute level market data
        Note: this function only works for the data format downloaded from hisdata.com
        with EST time
    '''

    # Read the minute data
    df_min = pd.read_csv(market_path, sep=';', names=["Timestamp", "Open", "High", "Low", "Close", "NA"])
    df_min.drop(columns=['NA'])
    df_min.Timestamp = pd.to_datetime(df_min.Timestamp)

    ### Adjust the EST time to UTC+8 time to align with the news time
    df_min.Timestamp = df_min.Timestamp + pd.Timedelta(hours=13)
    return df_min


### Process dataframe with calculations

# 1. News data

def cal_sent_index(a, b, time_delta,init_val):
    '''Calculate the index at each time'''
    value = init_val*math.exp(-a*time_delta + b)
    return value

def sent_index_df(init_time, a, b, time_delta, init_val):
    """Place the calculated index into dataframe"""
    index_list = []
    for i in range (0,time_delta):
        index_list.append(cal_sent_index(a,b,i,init_val))
    index_series = pd.Series(index_list)
    index_series = index_series.transpose()
    time_window = pd.date_range(init_time,periods=10, freq='min')
    new_dict = {'datetime': time_window, 'sent_index_{0}'.format(init_time):index_series}
    df_sent = pd.DataFrame(new_dict)
    return df_sent


def df_sent_idx(df_news):
    '''Calculate the sentiment index at each minute of a news dataframe
    using exponential decay with time
    '''
    a = 1
    b = 0
    time_delta = 10
    df_combine = pd.DataFrame(columns = ['datetime'])
    for index, value in df_news.iterrows():
        print ("now processing index:",index,"out of total:", df_news.index.max())
        df_sent = sent_index_df(pd.to_datetime(value['newsTime']),a,b,time_delta, value['ccy_sent'])
        df_combine = pd.merge(df_combine, df_sent, on='datetime', how='outer')
    df_combine = df_combine.rename(columns={'datetime': 'Timestamp'})
    return df_combine

# Market data

def ATR_calc(df,window):
    '''Calculate the ATR for the dataframe
    df: The input dataframe
    window: The window size for the moving average calculation
    '''
    df['ATR1'] = abs (df['High'] - df['Low'])
    df['ATR2'] = abs (df['High'] - df['Close'].shift())
    df['ATR3'] = abs (df['Low'] - df['Close'].shift())
    df['TrueRange'] = df[['ATR1', 'ATR2', 'ATR3']].max(axis=1)
    df['ATR'] = df['TrueRange'].ewm(span = window).mean()
    df = df.drop(columns=['ATR1', 'ATR2','ATR3','TrueRange'])
    return df

### Combining two sets of data frame to create final one

def combine_news_market_df(df_market, df_news):

    df_final = pd.merge(df_market, df_news, on='Timestamp', how='outer')
    print (df_final.shape)
    # Add the sentiment together
    selected_cols = [col for col in df_final.columns if 'sent_index' in col]
    df_final['sum'] = df_final[selected_cols].sum(axis=1)

    # slice the final dataframe and ignore the last few rows
    df_final_cal = df_final[['Timestamp','Open','High','Low','Close','sum','ATR']].iloc[:33060]
    return df_final_cal


### Final calculation
def vol_sent_correlation(df_final):
    '''Output the correlation between news sentiment and volatility'''
    x_ts = df_final[df_final.columns[0]]
    x_open = df_final[df_final.columns[1]]
    x_high = df_final[df_final.columns[2]]
    x_low = df_final[df_final.columns[3]]
    x_close = df_final[df_final.columns[4]]
    x_sum = df_final[df_final.columns[5]]
    x_vol = df_final[df_final.columns[6]]
    #x_abssum = df_final[df_final.columns[7]]

    vol_sent_correlation = x_sum.corr(x_vol)
    print (x_sum.nunique())
    return vol_sent_correlation



if __name__ == '__main__':

    # Read
    df_market = read_market_data(market_path='./data/EURUSD/EURUSD_M_201810.csv')
    df_news = read_news_data(news_path='./data/EURUSD/EUR_pri_sub_or_filter.csv')

    # Processing
    df_market_processed = ATR_calc(df_market, window=5)
    df_news_processed = df_sent_idx(df_news)

    # Combining
    df_combine = combine_news_market_df(df_market_processed,df_news_processed)

    # Final calculation
    print(vol_sent_correlation(df_combine))



# Try different currencies:
# USDJPY
# 1. Get USD/JPY Nov Data
# 2. Get JPY Nov news
#

# Try different months
# EURUSD on Oct and Nov
# 1. Get USD/JPY Nov Data
# 2. Get JPY Nov news

# Try different filters
# Using EUR Oct data
# Filter 1: Pri - Central bank only
# Filter 2: Pri - or - urgent
# Filter 3: Pri - Central bank only - urgent
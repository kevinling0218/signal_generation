# Primary currency filter
import pandas as pd

from text_cleaner import text_cleaner
from curr_replacer import curr_replacer
from curr_occur import curr_occur

######## Read dataframe ###################

def read_news_dataframe(path):
    df_news = pd.read_csv(path)
    return df_news

######## Filter algorithm ##############

def primary_currency_text(text):
    '''
    Returns the most mentioned currency in given text
    '''
    text = text_cleaner(text)
    text = curr_replacer(text)
    curr_occur_dic = curr_occur(text)

    # Finding maximum value in the curr_occur_dic
    keys, values = list(curr_occur_dic.keys()), list(curr_occur_dic.values())
    max_val = max(values)
    max_key = keys[values.index(max_val)]

    return max_key

def primary_currency_title(text):
    '''
    Returns every currency mentioned in the text
    '''
    text = text_cleaner(text)
    text = curr_replacer(text)
    curr_occur_dic = curr_occur(text)
    curr_occur_dic = {k:v for k,v in curr_occur_dic.items() if v!=0} # Get rid of zeros

    return list(curr_occur_dic.keys())

### Obtain primary currency sentiment

def primary_sentiment(primary_currency, sentiment):

    '''Return the sentiment value of the primary currency'''

    try:
        sentiment_dict = eval(sentiment)
        if type(sentiment_dict)==dict:
            for key, value in sentiment_dict.items():
                if key == primary_currency:
                    print (value)
                    return value
    except:
        return "Unknown"

### Subject filter

bank_codes = ['M:8','M:I','M:QF', # Central bank
            'N2:IMF','M:Q', # IMF
            'M:Y','P:4296937871','N2:FED','N2:F1', # Federal Reserve
            'N2:1'] # Interest Rates

politics_codes = ['M:2', 'M:4','M:9','M:B','M:C','M:G','M:N','M:R','M:T','M:X',
'M:AJ','M:DF','M:DU','M:E9','M:EG','M:EI','M:EL','M:EM','M:EQ','M:F7','M:LK','M:M0',
'M:MW','M:MX','M:MY','M:MZ','M:N4','M:N5','M:N6','M:N8','M:N9','M:NX','M:RA','M:RB',
'M:RC','M:RD','M:1P3','M:1R7','M:1SJ','M:1U0','M:1V6','M:1V7','M:1V8','M:1W4','M:1W8',
'P:1000314762','P:1000314702','P:1000339175','P:1000314708','P:1000314701','P:1000314821',
'P:400266','P:1000314703','P:1000314713','P:1000314761','P:1000314696','P:1000318127',
'P:1001097640','P:1000314845','P:1000314704','P:1000314706','P:1000314710','P:1000314711',
'P:1000314712','P:1000339176','P:1000314794','P:1000314759','P:1000339177','P:1000339178',
'P:1000339179','P:1000314718','P:1000314720','P:1000314721','P:1000314722','P:1000314724',
'P:1000314725','P:1000314733','P:1000314697','P:1000314698','P:1000314699','P:1000314700',
'P:1002115542','P:1000487182','P:1003534517','N2:WAR','N2:IMM','N2:VIO','N2:DEF','N2:DIP',
'N2:VOTE','N2:POL','N2:TRD','N2:LAW','N2:TAX','N2:WASH','N2:CVN','N2:INTAG','N2:GFIN',
'N2:TRF','N2:SDS','N2:CWP','N2:AID','N2:WELF','N2:BOMB','N2:SECUR','N2:HRGT','N2:NGO',
'N2:HUMA','N2:ADVO','N2:NUCL','N2:WRM','N2:CIV','N2:CENS','N2:DAT','N2:DEFBUY',
'N2:INSURG','N2:VOTP','N2:VOTS','N2:VOTH','N2:VOTG','N2:BRU','N2:POTUS','N2:BRI',
'N2:LRIGHV','N2:TERRO','N2:ISISR','N2:TERRO1','N2:HRIGHT','N2:HRIGHV',
'N2:G0','N2:TRUMP','N2:OBOR']

def central_bank_filter(labels):
    """
    labels: a list or set of Reuters codes
    True if at least one of the labels are about banks, IMF, FED, interest rates
    """
    if len(set(bank_codes)&set(labels)) > 0:
        return True
    else:
        return False

def politics_filter(labels):
    """
    labels: a list or set of Reuters codes
    True if at least one of the labels are about politics
    """
    if len(set(politics_codes)&set(labels)) > 0:
        return True
    else:
        return False

def check_central_bank(subjects):
    """Sometimes the subjects are not the content that we want, filter that out"""
    try:
        return central_bank_filter(eval(subjects))
    except:
        return "Unknown"

def check_political(subjects):
    """Sometimes the subjects are not the content that we want, filter that out"""
    try:
        return politics_filter(eval(subjects))
    except:
        return "Unknown"

def combine_topic_filter(row, filter_type):
    """Combine both filter by or, and"""
    if filter_type == "or":
        if (row['is_central_bank'] == True) or (row['is_political'] == True):
            return True
        else:
            return False
    if filter_type == "and":
        if (row['is_central_bank'] == True) and (row['is_political'] == True):
            return True
        else:
            return False

########### Perform filtering for the dataframe ##########################

def add_sentiment_to_df(df_news,primary_ccy):
    '''Add the primary currency sentiment into a column of data base'''

    df_news['ccy_sent'] = df_news['sentiment'].apply(lambda x: primary_sentiment(primary_ccy,x))
    return df_news

def apply_primary_currency_filter(df_news,primary_ccy):
    '''Adding the column of primary currency'''

    # Sometimes there are column of Unnamed, drop the columns
    df_news = df_news.loc[:, ~df_news.columns.str.contains('^Unnamed')]
    df_news['primary_currency'] = df_news['body'].astype(str).apply(primary_currency_text)
    df_primary = df_news[df_news['primary_currency']==primary_ccy]
    return df_primary

def apply_central_bank_filter(df_news):
    '''Applying central bank filter to the dataframe'''

    df_news['is_central_bank'] = df_news.subjects.apply(lambda x: check_central_bank(x))
    return df_news

def apply_politics_filter(df_news):
    df_news['is_political'] = df_news.subjects.apply(lambda x: check_political(x))
    return df_news

def apply_combined_topic_filter(df_news,filter_type):
    if filter_type == 'and':
        df_news['and_filter'] = df_news.apply(lambda row: combine_topic_filter(row, 'and'), axis=1)
    if filter_type == 'or':
        df_news['or_filter'] = df_news.apply(lambda row: combine_topic_filter(row, 'or'), axis=1)
    return df_news

def apply_urgency_filter(df_news):
    '''Applying urgency filter'''
    df_news = df_news.loc[df_news['messageType'].isin(['1', '2'])]
    return df_news




#################### Output the document as csv #############################


#
path = '../data/News/JPY-News.csv'
df = read_news_dataframe(path=path)

### process the raw news datafrma (may not be required all the time)
column_list = ['Title', 'News ID', 'Currency', 'News Time', 'Source', 'Sentiment',
       'News Text', 'Subjects', 'Take Sequence', 'Message Type', 'sentiment',
       'content', 'subject', 'takeSequence', 'urgency']
df.columns = column_list

# Add sentiment
df_JPY_1 = add_sentiment_to_df(df_news=df, primary_ccy='JPY')

# Add primary currency filter
df_JPY_2 = add_sentiment_to_df(df_news=)


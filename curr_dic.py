'''
Here we can edit dictionaries of terms associated with each currency.
The final output, curr_dic, is a dictionary of these terms and their associated currency.
'''

curr_lis = ['USD','EUR','GBP','JPY','AUD',
            'CAD','CNY','SGD','KRW','CHF',
             'HKD','IDR','INR','MXN','MYR',
             'NOK','NZD','SEK','THB','ZAR']

country_name_variants = {
'USD': ['United States','America','U.S.','USA','U.S.A.','The United States of America','United States of America','The United States'], # US is tricky
'EUR': ['Europe','EU','E.U.','The European Union','European Union',
        'Andorra',
        'Austria',
        'Belgium',
        'Cyprus',
        'Estonia',
        'Finland',
        'France',
        'Germany',
        'Greece',
        'Ireland',
        'Italy',
        'Kosovo',
        'Latvia',
        'Lithuania',
        'Luxembourg',
        'Malta',
        'Monaco',
        'Montenegro',
        'Netherlands','The Netherlands',
        'Portugal',
        'San Marino',
        'Slovakia',
        'Slovenia',
        'Spain',
        'Vatican City', 'The Vatican'],
'JPY': ['Japan'],
'GBP': ['Britain','UK','U.K.','United Kingdom','England'],
'AUD': ['Australia','Aus.'],
'CAD': ['Canada'],
'CNY': ['China', 'PRC','P.R.C.', "People's Republic of China"],
'SGD': ['Singapore',"S'pore"],
'KRW': ['South Korea','S.Korea','S. Korea', 'Korea'], # Make sure to delete "North Korea" first
'CHF': ['Switzerland'],
'HKD': ['Hong Kong','HK','H.K.'],
'IDR': ['Indonesia'],
'INR': ['India'],
'MXN': ['Mexico'],
'MYR': ['Malaysia'],
'NOK': ['Norway'],
'NZD': ['New Zealand','NZ','N.Z.'],
'SEK': ['Sweden'],
'THB': ['Thailand'],
'ZAR': ['South Africa','S.Africa','S. Africa']
}
demonyms = {
'USD': ['American','Americans'],
'EUR': ['European','Europeans',
        'Andorran','Andorrans',
        'Austrian','Austrians',
        'Belgian','Belgians',
        'Cypriot','Cypriots',
        'Estonian','Estonians',
        'Finnish','Finns',
        'French',
        'German','Germans',
        'Greek','Greeks',
        'Irish',
        'Italian','Italians',
        'Kosovar','Kosovan','Kosovars','Kosovans',
        'Latvian','Latvians',
        'Lithuanian','Lithuanians',
        'Luxembourgish',
        'Maltese',
        'Monacan','Monacans',
        'Montenegrin','Montenegrins',
        'Dutch',
        'Portuguese',
        'Sammarinese',
        'Slovak','Slovaks','Slovakian','Slovakians',
        'Slovenian','Slovene','Slovenians','Slovenes',
        'Spanish','Spaniard','Spaniards',
        'Vatican'],
'JPY': ['Japanese'],
'GBP': ['British','English','Briton','Britons'],
'AUD': ['Australian','Australians','Aussie','Aussies'],
'CAD': ['Canadian','Canadians'],
'CNY': ['Chinese'],
'SGD': ['Singaporean','Singaporeans','S.porean','S.poreans',"S'porean","S'poreans"],
'KRW': ['Korean','Koreans'], # Must remove North Korean and North Koreans
'CHF': ['Swiss'],
'HKD': ['Hong Kongese'],
'IDR': ['Indonesian','Indonesians'],
'INR': ['Indian','Indians'],
'MXN': ['Mexican','Mexicans'],
'MYR': ['Malaysian','Malay','Malaysians','Malays'],
'NOK': ['Norewegian','Norwegians'],
'NZD': ['New Zealander','New Zealanders','Kiwi','Kiwis'],
'SEK': ['Swedish','Swede','Swedes'],
'THB': ['Thai','Thais'],
'ZAR': ['South African','South Africans']
}
currency_name_variants = {
'USD': ['USD','US Dollar','U.S. Dollar','U.S.Dollar','US.Dollar', 'American Dollar','US Dollars','U.S. Dollars','U.S.Dollars','US.Dollars','Greenback','Greenbacks','American Dollars','US$','U.S.$', 'Dollars','Dollar'], # Dollar is tricky
'EUR': ['EUR','Euro','Euros','The Common Currency'],
'JPY': ['JPY','Yen', 'Japanese Yen'],
'GBP': ['GBP','Pound','Sterling', 'British Pound','Pound Sterling'],
'AUD': ['AUD','Australian Dollar','Aussie Dollar','Australian Dollars','Aussie Dollars'],
'CAD': ['CAD','Canadian Dollar','Canadian Dollars','Loonie','Loonies'],
'CNY': ['CNY','Yuan','Renminbi', "China's Yuan",'Chinese Yuan'],
'SGD': ['SGD','Singaporean Dollar','Singaporean Dollars','Sing Dollar','Sing Dollars'],
'KRW': ['KRW','Won','South Korean Won','Korean Won'], # Must remove North Korean Won
'CHF': ['CHF','Franc','Francs','Swiss Franc','Swiss Francs'],
'HKD': ['HKD','Hong Kong Dollar','Hong Kong Dollars','HK Dollar','HK Dollars', 'H.K. Dollar','H.K. Dollars','H.K.Dollar','H.K.Dollars'],
'IDR': ['IDR','Rupiah','Rupiahs','Indonesian Rupiah','Indonesian Rupiahs'],
'INR': ['INR','Rupee','Rupees','Indian Rupee','Indian Rupees'],
'MXN': ['MXN','Peso','Pesos', 'Mexican Peso','Mexican Pesos'],
'MYR': ['MYR','Ringgit','Ringgits','Malaysian Ringgit','Malaysian Ringgits'],
'NOK': ['NOK','Krone','Kroner', 'Norwegian Krone','Norwegian Kroner','Norwegian Crown'],
'NZD': ['NZD','New Zealand Dollar','NZ Dollar','N.Z.Dollar','N.Z. Dollar','New Zealand Dollars','NZ Dollars','N.Z.Dollars','N.Z. Dollars'],
'SEK': ['SEK','Krona','Kronor', 'Swedish Krona','Swedish Kronor','Swedish Crown'],
'THB': ['THB','Baht','Bahts','Thai Baht','Thai Bahts'],
'ZAR': ['ZAR','Rand','Rands','South African Rand','South African Rands']
}
important_cities = {
'USD': ['Washington','New York','Silicon Valley'],
'EUR': ['Paris',
        'Athens',
        'Dublin',
        'Rome',
        'Amsterdam',
        'Lisbon',
        'Madrid','Barcelona'],
'JPY': ['Tokyo','Kyoto'],
'GBP': ['London'],
'AUD': ['Canberra','Melbourne','Sydney'],
'CAD': ['Ottawa','Toronto','Vancouver'],
'CNY': ['Beijing','Shanghai'],
'SGD': [],
'KRW': ['Seoul'],
'CHF': ['Bern','Geneva'],
'HKD': [],
'IDR': ['Jakarta'],
'INR': ['Delhi'],
'MXN': ['Mexico City'],
'MYR': ['Kuala Lumpur'],
'NOK': ['Oslo'],
'NZD': ['Wellington','Auckland'],
'SEK': ['Stockholm'],
'THB': ['Bangkok','Phuket'],
'ZAR': ['Cape Town','Johannesburg']
}
leaders = {
'USD': ['Donald Trump','Trump','Pence','US President','U.S. President','American President','U.S. President Donald Trump'],
'EUR': ['Donald Tusk',
        'Macron',
        'Merkel','Angela Merkel','German Chancellor Angela Merkel','German Chancellor','Chancellor Merkel','Chancellor Angela Merkel',
        'Pope'],
'JPY': ['Abe'],
'GBP': ['PM May','Theresa May','Prime Minister May','British Prime Minister'],
'AUD': ['Scott Morrison'],
'CAD': ['Trudeau','Justin Trudeau'],
'CNY': ['Xi Jinping','Xi'],
'SGD': ['Lee Hsien Loong'],
'KRW': ['Moon Jae-in','President Moon'],
'CHF': [],
'HKD': [],
'IDR': [],
'INR': ['Modi'],
'MXN': ['Nieto'],
'MYR': [],
'NOK': [],
'NZD': [],
'SEK': [],
'THB': [],
'ZAR': []
}
other = {
'USD': ['USDX','DXY','UST','US Treasury','U.S. Treasury','U.S. Treasury bond','U.S. Treasury bond yields','T Bills','USDA','Capitol Hill',
            'Nonfarm payroll','Non Farm Payroll','NASDAQ','Dow','Wall Street','US Manufacturing',
            'Federal Reserve','FOMC','Fed','POTUS','SCOTUS','Jackson Hole', 'Wall St',
            'u . s .'],
'EUR': ['European Central Bank','ECB',
        'Deutsche Bundesbank','DAX','DAX Index',
        'e . u .'],
'JPY': ['BOJ','Bank of Japan','Nikkei','N225','N 225'],
'GBP': ['BoE','Bank of England','FTSE',"Britain's FTSE",
        'u . k .'],
'AUD': ['RBA','FIRB','Reserve Bank of Australia'],
'CAD': [],
'CNY': ['PBOC','Bank of China'],
'SGD': [],
'KRW': ['Kospi','Kospi Index',"South Korea's Kospi Index","Korea's Kospi"],
'CHF': [],
'HKD': ['HSI',"Hong Kong's Seng Index",'Seng','Seng Index',"Hong Kong's Seng","Hong Kong's HSI"],
'IDR': [],
'INR': [],
'MXN': [],
'MYR': [],
'NOK': [],
'NZD': [],
'SEK': [],
'THB': [],
'ZAR': []
}


dic_lis = [country_name_variants,
            demonyms,
            currency_name_variants,
            important_cities,
            leaders,
            other]
# Combine all the dictionaries into one
combined_dic = {c:[] for c in curr_lis}
for dic in dic_lis:
    for curr in combined_dic.keys():
        combined_dic[curr] += dic[curr]

# Lower each entry in each list and add surrounding spaces
combined_dic = {curr:[' '+phrase.lower()+' ' for phrase in lis] for curr,lis in combined_dic.items()}

def dic_invert(dic):
    '''
    Inverts a dictionary of lists, e.g.: {a: [1, 2]} --> {1:a, 2:a}.
    Keys must of course be unique.
    '''
    out_dic = {}
    for key in dic.keys():
        lis = dic[key]
        for term in lis:
            out_dic[term] = key
    return out_dic

# Invert, so that keys are entries in lists and values are currencies
curr_dic = dic_invert(combined_dic)

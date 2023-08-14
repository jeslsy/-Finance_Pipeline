import pandas as pd
import requests

# - 주식거래대금,802Y001,0091000,D,
urls = 'https://ecos.bok.or.kr/api/StatisticSearch/EQYGCD4OHB16CGJTCC3K/JSON/kr/1/100000/802Y001/D/19700101/20230808/0091000/?/?/?'
res = requests.get(urls)
json_data = res.json()['StatisticSearch']['row']
df = pd.json_normalize(json_data)
df = df[['STAT_CODE','STAT_NAME','ITEM_CODE1','ITEM_NAME1','UNIT_NAME','TIME','DATA_VALUE']]
df.to_csv('../csv/코스닥_거래대금.csv',index=False)
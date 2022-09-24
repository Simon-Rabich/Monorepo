import pandas as pd
import sys

df1 = pd.read_csv("cost_1.csv")
df2 = pd.read_csv("revenue_1.csv")

date_from = '12/31/18 19:00' #sys.argv[0]
date_to = '1/1/19 22:00' #sys.argv[1]

df = df1.merge(df2, how='inner', on=['campaign_id', 'data_date']) # join on the key

newdf = df#.loc[(df['data_date'] >= date_from) & (df['data_date'] <= date_to)] # filter acorrding vaulse from CLI


newdf['uv'] = newdf['revenue'] / newdf['clicks']

newdf['cpc'] = newdf['cost'] / newdf['clicks']

newdf['profit'] = newdf['revenue'] - newdf['cost']

newdf['roi'] = newdf['uv'] / newdf['cpc']


agg_df = newdf.groupby(['campaign_id', 'data_date']).agg({'revenue':'sum','cost':'sum','profit':'sum', 'roi':'sum'})


newdf.to_csv("combined_csv.csv", index=False, encoding='utf-8-sig')


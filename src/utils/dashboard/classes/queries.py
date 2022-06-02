import pandas as pd
import calendar

class Queries:
    df=pd.read_csv('src/data/crypto_csv_formatted.csv', sep=',')
    df['month_name'] = df['month'].apply(lambda x: calendar.month_abbr[x])
    df['date'] = pd.to_datetime(df['date'])


    def __init__(self):
        pass


    def get_btc_price_by_years(self):
        res = self.df.loc[self.df['name'] == 'Bitcoin']

        return res


    def get_btc_rest_mcap(self, year):
        df_others_mcap = self.df.loc[self.df['name'] != 'Bitcoin']
        df_Bitcoin_mcap = self.df.loc[self.df['name'] == 'Bitcoin']

        df_others_mcap = df_others_mcap.groupby('year')['mcap'].sum().to_frame()
        df_others_mcap['name'] = 'Resto'
        df_others_mcap['meses'] = [7,12,12,12,12,12,12,12,12,5]
        df_others_mcap['mcap'] = df_others_mcap['mcap']/df_others_mcap['meses']

        df_Bitcoin_mcap = df_Bitcoin_mcap.groupby('year')['mcap'].sum().to_frame()
        df_Bitcoin_mcap['name'] = 'Bitcoin'
        df_Bitcoin_mcap['meses'] = [7,12,12,12,12,12,12,12,12,5]
        df_Bitcoin_mcap['mcap'] = df_Bitcoin_mcap['mcap']/df_Bitcoin_mcap['meses']

        df_all_mcap = pd.concat([df_Bitcoin_mcap,df_others_mcap]).reset_index()
        res = df_all_mcap.loc[df_all_mcap['year'] == year]

        return res


    def get_btc_price_by_year(self, year):
        res = self.df.loc[(self.df['name'] == 'Bitcoin') & (self.df['date'].dt.year == year)]

        return res


    def get_circulatingSupply_by_years(self):
        res = self.df.loc[self.df['name'] == 'Bitcoin', ['circulating_supply','date']]

        return res


    def get_crypto_price(self, name):
        res = self.df.loc[self.df['name'] == name]

        return res

    
    def get_top_crypto_by_year(self, year, amount):
        df = self.df.loc[self.df['date'].dt.year == year]
        res = df.groupby('name')['mcap'].mean().to_frame().reset_index().sort_values(by='mcap', ascending=False).iloc[:amount].reset_index(drop=True).sort_values(by='mcap', ascending=True)

        return res


    def get_count_by_years(self):
        df_anyo_mes = self.df.groupby(['year','month'])['name'].count().to_frame().reset_index().rename(columns = {'name':'count_crs'})

        df_aux = df_anyo_mes.loc[(df_anyo_mes['year'] == 2022) & (df_anyo_mes['month'] == 5)]

        df_anyo_mes = df_anyo_mes.loc[df_anyo_mes['month'] == 12]
        res = pd.concat([df_anyo_mes,df_aux])

        return res


    def get_months_mcap_by_year(self, year):
        res = self.df.loc[self.df['year'] == year].groupby('month_name')['mcap'].sum().reset_index().sort_values(by='mcap', ascending=True)

        return res

    
    def get_months_mcap_by_years(self):
        res = self.df.groupby('month_name')['mcap'].mean().to_frame()

        return res
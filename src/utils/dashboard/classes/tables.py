import plotly.graph_objects as go

# Tables class
class Tables:

    def __init__(self):
        pass

    
    def get_btc_price_by_years(self, df):
        res = go.Figure(data=[go.Table(header=dict(values=['date', 'price']),
                    cells=dict(values=[df['date'], df['price']]))
                ])
        res.update_layout(height=140, margin=dict(r=5, l=5, t=5, b=5))

        return res

    
    def get_btc_rest_mcap(self, df):
        res = go.Figure(data=[go.Table(header=dict(values=['year', 'name', 'mcap']),
                    cells=dict(values=[df['year'], df['name'], df['mcap']]))
                ])
        res.update_layout(height=140, margin=dict(r=5, l=5, t=5, b=5))

        return res

    
    def get_btc_price_by_year(self, df):
        res = go.Figure(data=[go.Table(header=dict(values=['month name', 'price']),
                    cells=dict(values=[df['month_name'], df['price']]))
                ])
        res.update_layout(height=140, margin=dict(r=5, l=5, t=5, b=5))

        return res

    
    def get_circulatingSupply_by_years(self, df):
        res = go.Figure(data=[go.Table(header=dict(values=['circulating supply', 'date']),
                    cells=dict(values=[df['circulating_supply'], df['date']]))
                ])
        res.update_layout(height=140, margin=dict(r=5, l=5, t=5, b=5))

        return res
    

    def get_crypto_price(self, df):
        res = go.Figure(data=[go.Table(header=dict(values=['name', 'price','date']),
                    cells=dict(values=[df['name'], df['price'], df['date']]))
                ])
        res.update_layout(height=140, margin=dict(r=5, l=5, t=5, b=5))

        return res

    
    def get_top_crypto_by_year(self, df):
        df = df.sort_values(by='mcap', ascending=False)
            
        res = go.Figure(data=[go.Table(header=dict(values=['name', 'market capital']),
                cells=dict(values=[df['name'], df['mcap']]))
            ])
        res.update_layout(height=140, margin=dict(r=5, l=5, t=5, b=5))

        return res


    def get_count_by_years(self, df):
        res = go.Figure(data=[go.Table(header=dict(values=['year', 'number of cryptos']),
                    cells=dict(values=[df['year'], df['count_crs']]))
            ])
        res.update_layout(height=140, margin=dict(r=5, l=5, t=5, b=5))

        return res


    def get_months_mcap_by_year(self, df):
        res = go.Figure(data=[go.Table(header=dict(values=['month', 'market capital']),
                    cells=dict(values=[df['month_name'], df['mcap']]))
                ])
        res.update_layout(height=140, margin=dict(r=5, l=5, t=5, b=5))

        return res

    
    def get_months_mcap_by_years(self, df):
        res = go.Figure(data=[go.Table(header=dict(values=['month', 'market capital']),
                    cells=dict(values=[df.index, df['mcap']]))
                ])
        res.update_layout(height=140, margin=dict(r=5, l=5, t=5, b=5))

        return res
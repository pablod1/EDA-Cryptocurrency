import plotly.graph_objects as go

# Graphs class
class Graphs:

    def __init__(self):
        pass


    def get_btc_price_by_years(self, df):
        trace = go.Scatter(
            x = df['date'],
            y = df['price'],
            mode = 'lines',
            marker = dict(color = 'rgba(16, 112, 2, 0.8)'),
            text = df['date']
        )

        layout = dict(
            title = '1. Bitcoin price by all years', 
            font=dict(
                family="Courier New, monospace",
                size=18,
                color="RebeccaPurple"
        ))

        res = go.Figure(data = trace, layout = layout)

        return res

    
    def get_btc_rest_mcap(self, df, year):
        title = "2. Global mcap for "+str(year)

        trace = go.Pie(
            labels = df['name'],
            values = df['mcap']
        )

        layout = dict(
            title = title, 
            font=dict(
                family="Courier New, monospace",
                size=18,
                color="RebeccaPurple"
        ))

        res = go.Figure(data = trace, layout = layout)

        return res


    def get_btc_price_by_year(self, df, year):
        trace = go.Scatter(
            x = df['month_name'],
            y = df['price'],
            mode = 'lines+markers',
            marker = dict(color = 'rgba(16, 112, 2, 0.8)'),
            text = df['price']
        )

        title = "3. Bitcoin price for "+str(year)

        layout = dict(
            title = title,
            font=dict(
                family="Courier New, monospace",
                size=18,
                color="RebeccaPurple"
        ))

        res = go.Figure(data = trace, layout = layout)

        return res


    def get_circulatingSupply_by_years(self, df):
        trace = go.Bar(
            x = df['date'],
            y = df['circulating_supply'],
            marker = dict(color = 'green'),
            text = df['circulating_supply']
        )

        layout = dict(
            title = '2. Circulating supply by all years',
            font=dict(
                family="Courier New, monospace",
                size=18,
                color="RebeccaPurple"
        ))

        res = go.Figure(data = trace, layout = layout)

        return res


    def get_crypto_price(self, df, name):
        trace = go.Scatter(
            x = df['date'],
            y = df['price'],
            mode = 'lines',
            marker = dict(color = 'rgba(170, 112, 2, 0.8)'),
            text = df['date']
        )

        title = "1. "+str(name)+" price evolution"

        layout = dict(
            title = title, 
            font=dict(
                family="Courier New, monospace",
                size=18,
                color="RebeccaPurple"
        ))

        res = go.Figure(data = trace, layout = layout)

        return res


    def get_top_crypto_by_year(self, df, year):
        trace = go.Bar(
            x = df['mcap'],
            y = df['name'],
            orientation='h',
            marker = dict(color = 'DarkSlateGrey'),
            text = round(df['mcap']/1000000000, 2)
        )

        layout = dict(
            title = '2. Top currencies marketcap in '+str(year),
            font=dict(
                family="Courier New, monospace",
                size=18,
                color="RebeccaPurple"
        ))

        res = go.Figure(data = trace, layout = layout)

        return res

    
    def get_count_by_years(self, df):
        trace = go.Bar(
            x = df['year'],
            y = df['count_crs'],
            marker = dict(color = 'rgba(255, 174, 255, 0.5)'),
            text = df['count_crs']
        )

        layout = dict(
            title = '3. Count of currencies by years',
            font=dict(
                family="Courier New, monospace",
                size=18,
                color="RebeccaPurple"
        ))

        res = go.Figure(data = trace, layout = layout)

        return res

    
    def get_months_mcap_by_year(self, df, year):
        trace1 = go.Bar(
            x = df['mcap'],
            y = df['month_name'],
            orientation='h',
            marker = dict(color = 'LightSkyBlue'),
            text = round(df['mcap']/1000000000, 2)
        )

        layout = dict(
            title = '4. Months marketcap in '+str(year),
            font=dict(
                family="Courier New, monospace",
                size=18,
                color="RebeccaPurple"
        ))

        res = go.Figure(data = trace1, layout = layout)

        return res

    
    def get_months_mcap_by_years(self, df):
        title = "4. Mean of marketcap by months"

        trace = go.Pie(
            labels = df.index,
            values = df['mcap']
        )

        layout = dict(
            title = title, 
            font=dict(
                family="Courier New, monospace",
                size=18,
                color="RebeccaPurple"
        ))

        res = go.Figure(data = trace, layout = layout)

        return res

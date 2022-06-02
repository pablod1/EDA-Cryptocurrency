import pandas as pd
import streamlit as st
import constants as cns
import classes.queries as gq
import classes.graphs as g
import classes.tables as tb

df=pd.read_csv('../../data/crypto_csv_formatted.csv', sep=',')

query = gq.Queries()
graph = g.Graphs()
table = tb.Tables()

def home():
    st.title('EDA Cryptocurrency')

    st.subheader('Short description')
    st.markdown('##### The main purpose of this presentation is know how the global cryptocurrency market has moved throught the years, in order to respond some important questions like: <i>¿Is it safe now to invest in cryptocurrencies?</i>, <i>¿How important is the Bitcoin for the cryptomarket?</i> or <i>¿Where and when should i invest?. Those answers are going to help us understand the market and make better investments.', unsafe_allow_html=True)

    st.subheader('Data used (From 2013 May. to 2022 May)')
    st.markdown('###### Data dimension: '+str(df.shape[0])+' rows and '+str(df.shape[1])+' columns')

    st.dataframe(df)
    
    csv = convert_df(df)

    st.download_button(
        label='Download CSV file',
        data=csv,
        file_name='crypto_data.csv',
        mime='text/csv',
    )

    st.subheader('About')

    st.markdown("""
    * **Python libraries:** pandas, plotly, beautifulSoup, selenium, calendar, math, time, csv
    * **Data source:** [CoinMarketCap](https://coinmarketcap.com/es/historical/).
    * **Created by:** [Pablo Díaz González](https://www.linkedin.com/in/pablo-d%C3%ADaz-gonz%C3%A1lez-574b42173/)
    """)
        
        

def BTC():
    # Sliders
    st.sidebar.markdown('##### Figure 2')
    mcap_year = st.sidebar.slider('Select year.: ', 2013, 2022)

    st.sidebar.markdown('##### Figure 3')
    btc_price_year = st.sidebar.slider('Select year: ', 2013, 2022)


    col1, col2 = st.columns(2)

    # Figure 1
    with col1:
        df = query.get_btc_price_by_years()
        fig = graph.get_btc_price_by_years(df)
        st.plotly_chart(fig)

        with st.expander('Detail fig 1'):
            fig = table.get_btc_price_by_years(df)
            st.plotly_chart(fig)
            st.markdown(cns.graph_description.get('text1'))

    
    #Figure 2
    with col2:
        df = query.get_btc_rest_mcap(mcap_year)
        fig = graph.get_btc_rest_mcap(df, mcap_year)
        st.plotly_chart(fig)

        with st.expander('Detail fig 2'):
            for i,row in df.iterrows():
                nombre = str(row['name'])
                cap = str(round(row['mcap']/1000000000, 2))
                st.info(nombre+" capital "+cap+" b. ($)")

            fig = table.get_btc_rest_mcap(df)
            st.plotly_chart(fig)
            st.markdown(cns.graph_description.get('text2'))


    # Figure 3
    with col1:
        df = query.get_btc_price_by_year(btc_price_year)
        fig = graph.get_btc_price_by_year(df, btc_price_year)
        st.plotly_chart(fig)

        with st.expander('Detail fig 3'):
            fig = table.get_btc_price_by_year(df)
            st.plotly_chart(fig)
            st.markdown(cns.graph_description.get('text3'))


    with col2:
        st.info('TO BE decided')


def market():
    # Sliders
    st.sidebar.markdown('##### Figure 1')
    selected_crypto = st.sidebar.selectbox('Select cryptocurrency: ', df['name'].unique())

    min_year = int(df['year'].min())
    max_year = int(df['year'].max())

    st.sidebar.markdown('##### Figure 2')
    top_year = st.sidebar.slider('Select year: ', min_year,max_year)
    top_amount = st.sidebar.slider('Select amount of cryptos: ', 5,20)

    st.sidebar.markdown('##### Figure 4')
    month_year = st.sidebar.slider('Select year:  ', min_year,max_year)
    month_year_all = st.sidebar.checkbox('All')
    
    col1, col2 = st.columns(2)

    # Figure 1
    with col1:
        df_select_crypto = query.get_crypto_price(selected_crypto)
        fig = graph.get_crypto_price(df_select_crypto, selected_crypto)

        st.plotly_chart(fig)

        with st.expander('Detail fig 1:'):
            fig = table.get_crypto_price(df_select_crypto)
            st.plotly_chart(fig)
            st.markdown(cns.graph_description.get('text4'))


    # Figure 2
    with col2:
        df_s = query.get_top_crypto_by_year(top_year, top_amount)
        fig = graph.get_top_crypto_by_year(df_s, top_year)
        
        st.plotly_chart(fig)

        with st.expander('Detail fig 2:'):
            fig = table.get_top_crypto_by_year(df_s)
            st.plotly_chart(fig)
            st.markdown(cns.graph_description.get('text5'))


    # Figure 3
    with col1:
        df_anyo_mes = query.get_count_by_years()
        fig = graph.get_count_by_years(df_anyo_mes)

        st.plotly_chart(fig)

        with st.expander('Detail fig 3:'):
            fig = table.get_count_by_years(df_anyo_mes)
            st.plotly_chart(fig)
            st.markdown(cns.graph_description.get('text6'))


    # Figure 4
    with col2:
        if month_year_all:
            df_month_mcap = query.get_months_mcap_by_years()
            fig = graph.get_months_mcap_by_years(df_month_mcap)

            st.plotly_chart(fig)

            with st.expander('Detail fig 4:'):
                fig = table.get_months_mcap_by_years(df_month_mcap)
                st.plotly_chart(fig)
                st.markdown(cns.graph_description.get('text7'))
        else:
            df_month_mcap = query.get_months_mcap_by_year(month_year)
            fig = graph.get_months_mcap_by_year(df_month_mcap, month_year)

            st.plotly_chart(fig)

            with st.expander('Detail fig 4:'):
                fig = table.get_months_mcap_by_year(df_month_mcap)
                st.plotly_chart(fig)
                st.markdown(cns.graph_description.get('text8'))


#@st.cache
def convert_df(df):
    return df.to_csv(index=False).encode('utf-8')
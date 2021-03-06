import streamlit as st
import functions as ft

st.set_page_config(page_title='Criptomonedas', layout='wide')

# Open css file
with open('src/utils/dashboard/css/styles.css') as f:
   st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

pagina = st.sidebar.selectbox('Select a page', ('Home', 'BTC', 'Market'))

# Depending on the selected option
if pagina == 'Home':
    ft.home()
elif pagina == 'BTC':
    ft.BTC()
elif pagina == 'Market':
    ft.market()
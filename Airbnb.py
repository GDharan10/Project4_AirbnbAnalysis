import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="Airbnb Analysis",
    page_icon="https://static-00.iconduck.com/assets.00/airbnb-icon-512x512-d9grja5t.png",
    layout="wide",
    initial_sidebar_state="collapsed"
)

row1 = st.columns(2)
with row1[0]:
    sub_columns = st.columns(3)

    with sub_columns[0]:
        menu = option_menu("Menu", ["Home","Analysis"], 
                icons=["house", "graph-up"],
                menu_icon="cast",
                default_index=0,
                styles={"icon": {"color": "orange", "font-size": "20px"}}
                )


if menu == 'Home':

    st.markdown(f""" <style>.stApp {{
                    background: url('https://www.spinxdigital.com/app/uploads/2022/11/image-airbnb.jpg');   
                    background-size: cover}}
                 </style>""",unsafe_allow_html=True)
    

if menu == 'Analysis':
    with row1[1]:
        st.image('https://www.stocksbnb.com/wp-content/uploads/2021/08/airbnb-678x381-1.png', use_column_width=True)
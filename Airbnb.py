import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from streamlit_option_menu import option_menu

df = pd.read_csv("C:\\GD\\Notes\\DS Class\\DTM15\\Project\\Guvi project\\4 Airbnb\\AirbnbDataset.csv")

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

    st.markdown(f""" <style>.stApp {{
                    background: url('https://blog.artonemfg.com/hubfs/airbnb-3399753_1920.jpg');   
                    background-size: cover}}
                    </style>""",unsafe_allow_html=True)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.hist(df['review_scores_rating'], bins=20, color='skyblue')
    ax.set_xlabel('Review Scores Rating')
    ax.set_ylabel('Frequency')
    ax.set_title('Review Scores Rating Distribution')

    # Display the Matplotlib plot using st.pyplot(), passing the figure explicitly
    st.pyplot(fig)
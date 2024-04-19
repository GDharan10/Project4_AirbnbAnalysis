import pandas as pd

import plotly.express as px

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
        menu = option_menu("Menu", ["Home","Analysis", "About"], 
                            icons=["house", "graph-up", "exclamation-triangle"],
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
                background: url('https://media.cntraveller.com/photos/63bd91b73c7bca633cbfe0fb/4:3/w_2400,h_1800,c_limit/airbnb.jpg');   
                background-size: cover}}
                </style>""",unsafe_allow_html=True)

    with row1[1]:
        analysis = st.selectbox("", ["1. Country Distribution",
                                    "2. ",
                                    "3. ",
                                    "4. ",
                                    "5. ",
                                    "6. ",
                                    "7. ",
                                    "8. ",
                                    "9. ",
                                    "10. "
                                    ])
    
    if analysis == "1. Country Distribution":

        sub_columns = st.columns(2)

        with sub_columns[0]:

            # Assuming df is your DataFrame containing the 'country' column
            country_counts = df['country'].value_counts().reset_index()
            country_counts.columns = ['country', 'count']

            # Create a pie chart using Plotly Express
            fig = px.pie(country_counts, values='count', names='country', title='Country Distribution')
            fig.update_layout(title_x=0.3)
            st.plotly_chart(fig)
    

    if analysis == "2. ":

        sub_columns = st.columns(2)

        with sub_columns[1]:
                    sub_columns_1 = st.columns(2)

                    with sub_columns_1[1]:
                        yaxis = st.selectbox("", ['price',
                                                  "review_scores_rating",
                                                  "extra_people_fee",                                                  
                                                ])

        with sub_columns[0]:
            fig = px.box(df, x='country', y = yaxis, title=f"{yaxis} by Country")
            fig.update_layout(xaxis_title='Country', yaxis_title = yaxis , xaxis_tickangle=-45)
            fig.update_layout(title_x=0.35)
            st.plotly_chart(fig)







if menu == "About":

    st.markdown(f""" <style>.stApp {{
                    background: url('https://blog.artonemfg.com/hubfs/airbnb-3399753_1920.jpg');   
                    background-size: cover}}
                    </style>""",unsafe_allow_html=True)
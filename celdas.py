import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

#Importamos DATA
df=pd.read_csv ("employee_data.csv")

#page config
st.set_page_config(page_tittle="Socialize your knowledge",page_icon=": busts_in_silhouette:")

st.tittle("Socializa your knowledge")
st.markdown("_Site that would help and make easier for us to analyze ther performance of socialize your knowledge employees_")

#LOGOS 
st.sidebar.image("a.png")
st.sidebar.markdown
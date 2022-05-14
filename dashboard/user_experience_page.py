import sys
import os
import sys
import pandas as pd
import streamlit as st
import plotly.io as pio
import plotly.express as px
from sklearn.cluster import KMeans

sys.path.append(os.path.abspath(os.path.join('../scripts'))) 
import plots

@st.cache
def loadCleanData():
    df = pd.read_csv("../data/user_experiance.csv")
    return df

@st.cache
def getExperienceDataFrame():
    df = loadCleanData().copy()
    user_experience_df = df[[\
        "MSISDN_Number", "Total_Avg_RTT", "Total_Avg_Bearer_TP", "Total_Avg_TCP"]].copy() 

    return user_experience_df

@st.cache
def getExperienceData():
    df = getExperienceDataFrame().copy()
    user_experience = df.groupby('MSISDN_Number').agg({
        'Total_Avg_RTT': 'sum',
        'Total_Avg_Bearer_TP': 'sum',
        'Total_Avg_TCP': 'sum'})
    return user_experience


def hist(sr, interactive=False):
    x = ["Id: " + str(i) for i in sr.index]
    fig = px.histogram(x=x, y=sr.values)
    if(interactive):
        st.plotly_chart(fig)
    else:
        st.image(pio.to_image(fig, format='png', width=1200))

def plot10(df):
    col = st.selectbox("Compute & list 10 of the top, bottom and most frequent: from", (
        [
            "TCP values",
            "Duration", 
            "Throughput values"
        ]))
    if col == "TCP values":
        sorted_by_tcp = df.sort_values('Total_Avg_TCP', ascending=False)
        return plot10Sorted(sorted_by_tcp, 'Total_Avg_TCP')

    elif col == "RTT values":
        sorted_by_rtt = df.sort_values('Total_Avg_RTT', ascending=False)
        return plot10Sorted(sorted_by_rtt, 'Total_Avg_RTT')  

    else:
        sorted_by_tp = df.sort_values('Total_Avg_Bearer_TP', ascending=False)
        return plot10Sorted(sorted_by_tp, 'Total_Avg_Bearer_TP')


def plot10Sorted(df, col_name):
    col = st.selectbox("Select from: from", (
        [
            "Top 10",
            "Last 10",
        ]))
    
    if col == "Top 10":
        sat_top_10 = df.head(10)[col_name]
        return hist(sat_top_10)
    else:
        sat_last_10 = df.tail(10)[col_name]
        return hist(sat_last_10)


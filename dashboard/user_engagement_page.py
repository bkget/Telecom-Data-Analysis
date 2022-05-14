import sys
import os
import sys
import pandas as pd
import streamlit as st
from sklearn.cluster import KMeans

sys.path.append(os.path.abspath(os.path.join('../scripts'))) 
import plots

@st.cache
def loadCleanData():
    df = pd.read_csv("../data/user_engagement.csv")
    return df

@st.cache
def getEngagemetData():
    df = loadCleanData().copy()
    user_engagement_df = df[['Customer_Id', 'Session_Frequency', 'Duration', 'Total_Data_Volume']].copy()
    user_engagement = df.groupby(
        'Customer_Id').agg({'Session_Frequency': 'count', 'Duration': 'sum', 'Total_Data_Volume': 'sum'}) 
    return user_engagement


def plotTop10(df): 
    col = st.sidebar.selectbox(
        "Select top 10 from", (["Session_Frequency", "Duration", "Total_Data_Volume"]))
    if col == "Sessions_Frequency":
        sessions = df.nlargest(10, "Session_Frequency")['Sessions_Frequency']
        return hist(sessions)
    elif col == "Duration":
        duration = df.nlargest(10, "Duration")['Duration']

        return plots.mult_hist([duration], 1, 1, "User Engagement Duration", ['Duration (sec)'])

    else:
        total_data_volume = df.nlargest(
            10, "Total_Data_Volume")['Total_Data_Volume']
        
        return plots.mult_hist([total_data_volume], 1, 1, "User Engagement Total Data Volume", ['Total Data Volume (kbps)'])


import sys
import os
import sys 
import pickle
import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px

sys.path.append(os.path.abspath(os.path.join('../scripts')))
import plots

@st.cache
def getEngagemetData():
    df = pd.read_csv("../data/user_engagement.csv")
    return df


@st.cache
def getExperienceData():
    df = pd.read_csv("../data/user_experiance.csv")
    df.rename(columns = {'MSISDN_Number':'Customer_Id'}, inplace=True)
    return df


def getEngagemetModel():
    with open("../models/user_engagement.pkl", "rb") as f:
        kmeans = pickle.load(f)
    return kmeans

def getExperienceModel():
    with open("../models/user_experiance.pkl", "rb") as f:
        kmeans = pickle.load(f)
    return kmeans

def getUserEngagement(less_engagement):
    eng_df = getEngagemetData().copy()
    eng_model = getEngagemetModel() 
    eng_df = eng_df.set_index('Customer_Id')[
        ['Session_Frequency', 'Duration', 'Total_Data_Volume']]
        
    distance = eng_model.fit_transform(eng_df)
    distance_from_less_engagement = list(
        map(lambda x: x[less_engagement], distance))
    eng_df['Engagement_Score'] = distance_from_less_engagement
    return eng_df

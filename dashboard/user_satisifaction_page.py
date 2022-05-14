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


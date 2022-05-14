import sys
import os
import sys
import numpy as np
import pandas as pd
import streamlit as st


def loadDescription():
    df = pd.read_csv("../data/Field_Descriptions.csv")
    return df


def loadOriginalData():
    df = pd.read_csv("../data/Week1_challenge_data_source(CSV).csv")
    return df


def loadPreprocessedData():
    df = pd.read_csv("../data/cleaned_Telecom_data.csv")
    return df


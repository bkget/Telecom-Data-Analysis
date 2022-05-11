import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd

def hist(df:pd.DataFrame, column:str, color:str)->None:
    plt.figure(figsize=(9, 7))
    sns.displot(data=df, x=column, color=color, kde=True, height=7, aspect=2)
    plt.title(f'Distribution of {column}', size=20, fontweight='bold')
    plt.show()


def box_plot(df: pd.DataFrame, x_col: str, title: str)->None:
    plt.figure(figsize=(12, 7))
    sns.boxplot(data=df, x=x_col)
    plt.title(title, size=20)
    plt.xticks(rotation=90, fontsize=14)
    plt.show()
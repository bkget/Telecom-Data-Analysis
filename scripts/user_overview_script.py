import pandas as pd

class UserOverviewScript():
    def __init__(self, df) -> None:
        self.df = df.copy()

    def get_top_handsets(self,  num):
        top_handset = self.df['Handset Type'].value_counts().head(num)
        return top_handset

    def get_top_manufacturers(self,  num):
        top_handset = self.df['Handset Manufacturer'].value_counts().head(num)
        return top_handset

    
    

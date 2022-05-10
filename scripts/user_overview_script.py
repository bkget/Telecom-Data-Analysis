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

    
    def get_handset_group(self):
        top_3_manufacturers = self.get_top_manufacturers(3)

        manufacturers = self.df.groupby("Handset Manufacturer")

        for column in top_3_manufacturers.index:
            result = manufacturers.get_group(column).groupby("Handset Type")['MSISDN/Number'].nunique().nlargest(5)
            print(f">>>> { column } <<<<")
            print(result)
            print() 
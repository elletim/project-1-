import pandas as pd
import requests as req
from io import StringIO
import matplotlib.pyplot as plt 

#loop through La, Sd, Nyc, Nd data

urls = ["http://berkeleyearth.lbl.gov/air-quality/maps/cities/United_States/California/Los_Angeles.txt", 
        "http://berkeleyearth.lbl.gov/air-quality/maps/cities/United_States/California/San_Diego.txt",
       "http://berkeleyearth.lbl.gov/air-quality/maps/cities/United_States/New_York/New_York.txt",
       "http://berkeleyearth.lbl.gov/air-quality/maps/cities/India/NCT/New_Delhi.txt"]

#function to take in url and display dataframe
def get_url(url):
    page = req.get(url) 
    page_df= pd.read_csv(StringIO(page.text),skiprows=10,sep='\t')
    page_df.columns= ['Year','Month','Day', 'UTC Hour','PM2.5','PM10_mask','Retrospective']     
    page_df = page_df[["Year","Month","PM2.5"]]
    page_df = page_df[(page_df["Year"].isin([2018,2019,2020,2021,2022])) & (page_df["Month"].isin([3,4,5]))]
    page_df = page_df.groupby(["Year","Month"])
    page_df = page_df["PM2.5"].mean()
    global df
    df = pd.DataFrame(data=page_df)
    pivot = df.pivot_table(columns="Year",index="Month",values="PM2.5")
    print (get_label(url),"PM2.5 Average")
    print (pivot)
    print (" ")

#function to plot dataframe
def plot_table (table,title, subtitle):
    x = table.plot()
    plt.title(title)
    plt.suptitle(subtitle)
    x.set_xticks(range(len(table)))
    x.set_xticklabels(["%s-%d" % item for item in table.index.tolist()], rotation=90)
    plt.show()

#function to get url label
def get_label(urlname):
    return urlname.split('.txt')[0].split('/')[-1].replace('_'," ")
    

#Main
for url in urls: 
    get_url(url)
    plot_table(df, "Ave PM2.5 Levels for Year/Month", get_label(url))

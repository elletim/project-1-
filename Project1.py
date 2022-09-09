#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


@author: elletimmer
"""


import pandas as pd
import requests as req
import matplotlib.pyplot as plt
import io
import csv
from io import StringIO

"Las Angeles Data"
la = req.get("http://berkeleyearth.lbl.gov/air-quality/maps/cities/United_States/California/Los_Angeles.txt")
with open('/tmp/la.txt','w') as fp:
    fp.write(la.text)
la_df= pd.read_csv('/tmp/la.txt',skiprows=9,header='infer',sep='\t')
la_df.columns = ["Year", "Month", "Day", "UTC Hour", "PM2.5", "PM10_mask", "Retrospective"]
print (la_df)
print(la_df.head())



"San Diego Data"
sd = req.get("http://berkeleyearth.lbl.gov/air-quality/maps/cities/United_States/California/San_Diego.txt")
print(la.status_code)
sd_df = pd.read_csv(sd.text)







"New York City Data"
nyc = req.get("http://berkeleyearth.lbl.gov/air-quality/maps/cities/United_States/New_York/New_York_City.txt")
print(la.status_code)
nyc_df = pd.read_csv(nyc.text)




"New Dehli Data"
nd= req.get("http://berkeleyearth.lbl.gov/air-quality/maps/cities/India/NCT/New_Delhi.txt")
print(nd.status_code)
nd_df = pd.read_csv(nd.text)


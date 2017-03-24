# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 12:45:44 2017

@author: Ronak
"""

import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt
calinmen1=[random.randrange(2500, 3300) for _ in range(0, 3000)]

calinmen2=[random.randrange(3301, 4100) for _ in range(0, 1000)]

calinmen3=[random.randrange(4101, 6000) for _ in range(0, 500)]

calinmen4=[random.randrange(6000, 13000) for _ in range(0, 500)]

           

calbur=[]
calintake= calinmen1+calinmen2+calinmen3+calinmen4
for i in range(len(calintake)):
    if calintake[i]> 2500 and calintake[i]<3300:
        calbur.append(random.randrange(2300,3100))
    elif calintake[i]> 3300 and calintake[i]<4100:
        calbur.append(random.randrange(3100,3600))
    elif calintake[i]> 4100 and calintake[i]<6000:
        calbur.append(random.randrange(3600,4400))
    else:
        calbur.append(random.randrange(3000,5000))
        
netcal= [x - y for x, y in zip(calintake, calbur)]

        
df= pd.DataFrame({'CalIntake': calintake, 'CalBurnt': calbur, 'NetCal': netcal})
print df.head()
plt.scatter(df['CalIntake'], df['CalBurnt'])
plt.show()
'''
labels=[]
for i in range(len(df)):
    if df['NetCal'][i]>400:
        labels.append('Obese')
    elif (df['Netcal'][i]>-300 or df['NetCal'][i]<399):
        labels.append('Stable')
    else:
        labels.append('Malnourished')
df['Labels']= pd.Series(labels)
'''
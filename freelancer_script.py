# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 14:10:28 2018

@author: Terry
"""

import pandas as pd
from matplotlib import rcParams
rcParams['font.family'] = 'serif'
rcParams['image.cmap'] = 'grey'
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('C:/Users/Terry/Desktop/freelancer_data.csv') # loads CSV
data = data.sort_values(by='CropLost') #sorts by croplost
top_num=15 #the number of countries you would like to have annotated
data['Annotate'] = data['CropLost']>data['CropLost'].iloc[-top_num-1] # creates another column that tells the plotter to annotate a country or not

groups = data.groupby('Region') # groups countries by region for plotting

# Plot
fig, ax = plt.subplots(figsize=(30,20)) # creates figure
ax.set_prop_cycle(color=[plt.cm.Set2(i) for i in np.linspace(0, 1, 8)]) #change color cycler to Set2
ax.margins(0.05) # Optional, just adds 5% padding to the autoscaling
for region, group in groups:
    ax.plot(group.CropGDP, group.CropLost, marker='o', linestyle='', ms=20, label=region) #plots points at CropGDP and CropLost values and colors them the same for each region


ann_data = data[data['Annotate']] #creates dataframe with just the annotated countries

for i,name in enumerate(ann_data['Country']): #loops over them
    ax.annotate(name, xy=(ann_data['CropGDP'].iloc[i], ann_data['CropLost'].iloc[i]), #annotates them
                xytext=(ann_data['CropGDP'].iloc[i]-.75*((i)%2)+.6, ann_data['CropLost'].iloc[i]+1.75*((i)%2)), #shifts every other up and to the left so there is no overlap
                 label=ann_data['Region'].iloc[i],size=30 ) #keeps the formatting the same as the rest
    
lgd=ax.legend( bbox_to_anchor=(1.02, .75), bbox_transform=ax.transAxes, fontsize=30, numpoints=1) #creates the legned and moves it outside of the graph
plt.xlabel('Crop GDP',size=40) #x label
plt.xticks(fontsize=30) # tick size
plt.ylabel('Crop Lost',size=40) # y label
plt.yticks(fontsize=30) # tick size
plt.grid() # adds gridlines

#Lesser GDP Arrow
bbox_props = dict(boxstyle="larrow", fc=(0.8, 0.9, 0.9), ec="b", lw=2)
t = ax.text(5, -5.5, "Lesser GDP", ha="center", va="center", rotation=0,
            size=15,
            bbox=bbox_props)
bb = t.get_bbox_patch()
bb.set_boxstyle("larrow", pad=0.6)

#Greater GDP Arrow
bbox_props = dict(boxstyle="rarrow", fc=(0.8, 0.9, 0.9), ec="b", lw=2)
t = ax.text(77, -5.5, "Greater GDP", ha="center", va="center", rotation=0,
            size=15,
            bbox=bbox_props)
bb = t.get_bbox_patch()
bb.set_boxstyle("rarrow", pad=0.6)

#More Crops Lost Arrow
bbox_props = dict(boxstyle="rarrow", fc=(0.8, 0.9, 0.9), ec="b", lw=2)
t = ax.text(0.5, 67, "More Crops Lost", ha="center", va="center", rotation=90,
            size=15,
            bbox=bbox_props)
bb = t.get_bbox_patch()
bb.set_boxstyle("rarrow", pad=0.6)

#Less Crops lost Arrow
bbox_props = dict(boxstyle="larrow", fc=(0.8, 0.9, 0.9), ec="b", lw=2)
t = ax.text(0.5, 3, "Less Crops Lost", ha="center", va="center", rotation=90,
            size=15,
            bbox=bbox_props)
bb = t.get_bbox_patch()
bb.set_boxstyle("larrow", pad=0.6)


plt.savefig('plot.png', bbox_extra_artists=(lgd,), bbox_inches='tight') #saves the figure
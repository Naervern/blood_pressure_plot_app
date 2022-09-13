###################################
# This is just a proof of concept #
# Doing some simple plotting with #
# A small mock dataset            #
###################################

import pandas as pd
import numpy as np
import pylab
from datetime import datetime as dt
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.ticker import (AutoMinorLocator, MultipleLocator)
from matplotlib.dates import HourLocator, MonthLocator, YearLocator

matplotlib.rcParams["figure.dpi"] = 400
matplotlib.rcParams["figure.figsize"] = (15,3)

table = pd.DataFrame(columns=['Hora', 'Sist', 'Dias', 'Puls'])


datestr =  ["07/09/2022 ", "08/09/2022 ", "09/09/2022 ", "10/09/2022 ", "11/09/2022 "]

times= [["500","520","625","720","820","940","1040","1140","1255","1330","1530","1730","1830","1950","2055","2325"], ["0415","0525","0615","0720","0850","0910","1000","1105","1155","1250","1410","1550","1700","1800","1900","2000","2100","2200"], ["0300","0430","0620","0710","0815","0910","0945","1010","1115","1210","1300","1450","1850","2150"], ["0505","0610","0850","1015","1120","1510","1725","1815","2110","2230","2315"], ["0405","0515","0850","1135","1205","1240","1600","1845","2005","2130"]]

col0 = []

col1 = [122,105,113,124,123,124,125,121,112,113,112,123,123,119,120,110,114,107,109,120,132,126,126,125,117,113,122,109,110,105,111,113,107,100,108,102,113,121,130,129,123,135,124,120,122,112,117,98,111,115,128,116,123,121,119,123,112,126,131,113,110,127,131,130,116,125,121,116,121]

col2 = [75,73,77,78,77,83,82,77,71,75,73,77,77,78,80,71,76,73,70,73,85,75,78,73,72,76,76,68,71,62,75,74,65,66,73,70,72,77,79,81,79,83,78,78,73,72,75,59,70,75,81,76,82,75,75,76,70,76,77,73,70,78,85,83,78,76,81,76,78]

col3 = [64,63,59,68,68,62,70,66,67,77,72,68,67,68,68,68,68,61,58,66,73,70,68,60,62,73,80,70,64,63,68,71,67,61,65,58,60,64,77,75,76,80,84,78,87,84,71,80,79,68,76,70,72,83,77,73,79,77,84,65,66,72,80,80,76,81,70,71,76]


for i in range(len(times)):
    for j in range(len(times[i])):
        #times[i][j] = datestr[i] + times[i][j]
        col0.append(dt.strptime((datestr[i] + times[i][j]), "%d/%m/%Y %H%M"))
    
print(col0, '\n')
print(col1, '\n')
print(col2, '\n')


# appending
table['Hora'] = col0
table['Sist'] = col1
table['Dias'] = col2
table['Puls'] = col3


# Time to plot

plt.clf()
fig, ax1 = plt.subplots()
ax1.plot(table['Hora'], table['Sist'], '.', table['Hora'],table['Dias'], '.')
plt.ylim([50, 140])
plt.xlim([dt.strptime("07092022 0000", "%d%m%Y %H%M"), dt.strptime("12092022 0000", "%d%m%Y %H%M")])

ax1.xaxis.set_minor_locator(AutoMinorLocator(4))
#ax1.xaxis.set_major_locator(HourLocator(byhour=None, interval=6, tz=None))

ax1.yaxis.set_major_locator(MultipleLocator(20))
ax1.yaxis.set_minor_locator(AutoMinorLocator(4))

#ax1.xaxis.set_major_locator(ticker.AutoLocator())

ax1.grid(which='major', color='#7F7F7F', linewidth=0.5)
ax1.grid(which='minor', color='#DDDDDD', linewidth=0.5)

#plt.xlabel("Data")
#plt.ylabel("Pressão(mmHg)")

plt.show()


plt.clf()
fig, ax2 = plt.subplots()
ax2.plot(table['Hora'], table['Puls'], '.')
plt.ylim([50, 100])

plt.xlim([dt.strptime("07092022 0000", "%d%m%Y %H%M"), dt.strptime("12092022 0000", "%d%m%Y %H%M")])

ax2.xaxis.set_minor_locator(AutoMinorLocator(4))

ax2.yaxis.set_major_locator(MultipleLocator(10))
ax2.yaxis.set_minor_locator(AutoMinorLocator(4))
ax2.grid(which='major', color='#7F7F7F', linewidth=0.5)
ax2.grid(which='minor', color='#DDDDDD', linewidth=0.5)

plt.show()

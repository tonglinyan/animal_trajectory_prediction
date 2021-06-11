import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
import pre_processing as pp
import correlation as cor
from matplotlib import gridspec
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

#whale_data = pp.import_data(
#    "../dataset/large marine fauna/blue whales/Blue whales Eastern North Pacific 1993-2008 - Argos Data.csv")


## zebra
#zebra_data = pp.import_data(
#    "../dataset/land predator/zebra/Migratory Burchell's zebra (Equus burchellii) in northern Botswana.csv")
#data = zebra_data[zebra_data['visible']][['timestamp', 'location-long', 'location-lat', 'tag-local-identifier']]


## gulls
#gull_data = pp.import_data(
#    '../dataset/bird/herring gulls/Herring Gulls (Larus Argentatus); Clark; Massachussets United States-argos.csv')
#gull_data2 = pp.import_data(
#    '../dataset/bird/herring gulls/Herring Gulls (Larus Argentatus); Clark; Massachussets United States-gps.csv')
#data = pd.concat([gull_data[['timestamp', 'location-long', 'location-lat', 'tag-local-identifier']], 
#    gull_data2[['timestamp', 'location-long', 'location-lat', 'tag-local-identifier']]], axis = 0)


## elephant
#elephant_data = pp.import_data(
#    '../dataset/land predator/elephant/African elephants in Etosha National Park (data from Tsalyuk et al. 2018).csv')
#data = elephant_data[['timestamp', 'location-long', 'location-lat', 'tag-local-identifier']]


#data = pp.missing_data(data)
#n, p = data.shape
#data, labels = pp.pre_processing(data, n)

#data.to_csv(r'../dataset/land predator/zebra/after_processing.csv', index = False)

#data.to_csv(r'../dataset/bird/herring gulls/after_processing.csv', index = False)

#data.to_csv(r'../dataset/land predator/elephant/after_processing.csv', index = False)

## zebra
#data = pd.read_csv('../dataset/land predator/zebra/after_processing.csv')
#pp.point_zebra(data) 


## gull
data = pd.read_csv('../dataset/bird/herring gulls/after_processing.csv')
pp.point_gull(data) 


## elephant
data = pd.read_csv('../dataset/land predator/elephant/after_processing.csv')
pp.point_elephant(data) 


#col = pp.labels(data)

## zebra
#date_list = pp.get_date_list('2007-10-25', '2009-06-01')

## gull
#date_list = pp.get_date_list('2007-10-25', '2009-06-01')

## elephant
#date_list = pp.get_date_list('2007-10-25', '2009-06-01')

#n1 = len(col)
#n2, p2 = date_list.shape
#arr = np.zeros((n2, n1))
#arr = pd.DataFrame(arr, columns = col)
#date_list = pd.concat([date_list, arr], axis = 1)

#n, p = data.shape

#for i in range(1, len(col)+1):
#    date_list = pp.box_time_series(data[data['label'] == col[i-1]], date_list, i)

## zebra
#date_list.to_csv(r'../dataset/land predator/zebra/date_list.csv', index = False)
#date_list = pd.read_csv('../dataset/land predator/zebra/date_list.csv', index_col = 0)

## gull
#date_list.to_csv(r'../dataset/bird/herring gulls/date_list.csv', index = False)
#date_list = pd.read_csv('../dataset/bird/herring gulls/date_list.csv', index_col = 0)

## elk
#date_list.to_csv(r'../dataset/land predator/elk/date_list.csv', index = False)
#date_list = pd.read_csv('../dataset/land predator/elk/date_list.csv', index_col = 0)


#for i in range(len(col)):
#    cor.ts_plot(date_list.iloc[:,i], col[i])

#cor.correlation(date_list)
#for i in range(len(col)):
    ##cor.lag_plot(date_list.iloc[:, i])
    #cor.autocorrelation(date_list.iloc[:, i], col[i])
   
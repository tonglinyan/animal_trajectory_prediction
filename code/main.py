import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
import pre_processing as pp
import correlation as cor
from matplotlib import gridspec
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

#whale_data, whale_ref = pp.import_data(
#    "../dataset/large marine fauna/blue whales/Blue whales Eastern North Pacific 1993-2008 - Argos Data.csv", 
#    "../dataset/large marine fauna/blue whales/Blue whales Eastern North Pacific 1993-2008 - Argos Data-reference-data.csv")

#zebra_data, zebra_ref= pp.import_data(
#    "../dataset/land predator/zebra/Migratory Burchell's zebra (Equus burchellii) in northern Botswana.csv",
#    "../dataset/land predator/zebra/Migratory Burchell's zebra (Equus burchellii) in northern Botswana-reference data.csv")

#zebra = zebra_data[zebra_data['visible']][['timestamp', 'location-long', 'location-lat', 'tag-local-identifier']]
#zebra = pp.missing_data(zebra)
#zebra_n, p = zebra.shape
#zebra, labels = pp.pre_processing(zebra, zebra_n)
#pp.point_plot(zebra)
#zebra.to_csv(r'../dataset/land predator/zebra/after_processing.csv', index = False)

zebra = pd.read_csv('../dataset/land predator/zebra/after_processing.csv')
pp.plot_colored(zebra) 

col = pp.labels(zebra)
#date_list = pp.get_date_list('2007-10-25', '2009-06-01')
#n1 = len(col)
#n2, p2 = date_list.shape
#arr = np.zeros((n2, n1))
#arr = pd.DataFrame(arr, columns = col)
#date_list = pd.concat([date_list, arr], axis = 1)

#zebra_n, p = zebra.shape
#print(zebra)

#for i in range(1, len(col)+1):
#    date_list = pp.box_time_series(zebra[zebra['label'] == col[i-1]], date_list, i)

#date_list.to_csv(r'../dataset/land predator/zebra/date_list.csv', index = False)
date_list = pd.read_csv('../dataset/land predator/zebra/date_list.csv', index_col = 0)

#for i in range(len(col)):
#    cor.ts_plot(date_list.iloc[:,i], col[i])

cor.correlation(date_list)
   
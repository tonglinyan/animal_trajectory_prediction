import numpy as np
import pandas as pd
import math
import box


def import_data(name_file, name_ref):
    x = pd.read_csv(name_file)
    ref = pd.read_csv(name_ref)
    x = pd.DataFrame(x)
    #print(x.info())
    ref = pd.DataFrame(ref)
    x = x.drop(x[x['visible'] == 'FALSE'].index)
    n, p = x.shape
    return x, ref, n


def missing_data(data):
    data = data.dropna(subset = ['location-long'], axis=0, how='any')
    data = data.dropna(subset = ['location-lat'], axis=0, how='any')
    return data


def pre_processing(data, n):

    col = pd.DataFrame(columns=['label'], index=[range (n)])
    data = pd.concat((data, col), axis = 1)
    for i in range(n):
        # longitude
        x = int(data.iloc[i, 1])
        # latitude
        y = math.ceil(data.iloc[i, 2]) 
        data.iloc[i, 4] = label(x, y)
        data.iloc[i, 0] = data.iloc[i, 0][0:10]
        print(i)
    data = data.drop_duplicates(['timestamp', 'tag-local-identifier'], 'first')
    print(data)
    return data


def label(x, y):
    return (90 - y)*360 + (x-180)


whale_data, whale_ref, whale_n = import_data(
    "../dataset/large marine fauna/blue whales/Blue whales Eastern North Pacific 1993-2008 - Argos Data.csv", 
    "../dataset/large marine fauna/blue whales/Blue whales Eastern North Pacific 1993-2008 - Argos Data-reference-data.csv")

zebra_data, zebra_ref, zebra_n = import_data(
    "../dataset/land predator/zebra/Migratory Burchell's zebra (Equus burchellii) in northern Botswana.csv",
    "../dataset/land predator/zebra/Migratory Burchell's zebra (Equus burchellii) in northern Botswana-reference data.csv")


zebra = zebra_data.iloc[:,2:5]
zebra = pd.concat([zebra, zebra_data.iloc[:,8]], axis=1)
zebra = missing_data(zebra)

"""
zebra_long_min = int(min(zebra.iloc[:,1]))
zebra_long_max = math.ceil(max(zebra.iloc[:,1]))
zebra_lat_min = int(min(zebra.iloc[:,2]))
zebra_lat_max = math.ceil(max(zebra.iloc[:,2]))


zebra_h = 0.1
nb_long_interval = (zebra_long_max - zebra_long_min)/zebra_h
nb_lat_interval = (zebra_lat_max - zebra_lat_min)/zebra_h

for i in range(int(nb_long_interval)-1):
    for j in range(int(nb_lat_interval)-1):
        df2 = zebra[(zebra['location-long'] >= zebra_long_min + i * zebra_h) 
        & (zebra['location-long'] < zebra_long_min + (i+1) * zebra_h)
        & (zebra['location-lat'] >= zebra_lat_min + i * zebra_h) 
        & (zebra['location-lat'] < zebra_lat_min + (i+1) * zebra_h)][['timestamp','tag-local-identifier']]
        list[i, j] = box.Box(zebra_long_min + i * zebra_h, zebra_lat_min + i * zebra_h, df2)
"""

#zebra.info()
#print(zebra.isnull())
pre_processing(zebra, zebra_n)
        
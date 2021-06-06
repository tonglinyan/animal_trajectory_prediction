import box
import numpy as np
import pandas as pd
import math

def import_data(name_file, name_ref):
    x = pd.read_csv(name_file)
    ref = pd.read_csv(name_ref)
    x = pd.DataFrame(x)
    ref = pd.DataFrame(ref)
    n, p = x.shape
    return x, ref, n


whale_data, whale_ref, whale_n = import_data(
    "../dataset/large marine fauna/blue whales/Blue whales Eastern North Pacific 1993-2008 - Argos Data.csv", 
    "../dataset/large marine fauna/blue whales/Blue whales Eastern North Pacific 1993-2008 - Argos Data-reference-data.csv")

zebra_data, zebra_ref, zebra_n = import_data(
    "../dataset/land predator/zebra/Migratory Burchell's zebra (Equus burchellii) in northern Botswana.csv",
    "../dataset/land predator/zebra/Migratory Burchell's zebra (Equus burchellii) in northern Botswana-reference data.csv")


zebra = zebra_data.iloc[:,2:5]
zebra = pd.concat([zebra, zebra_data.iloc[:,8]], axis=1)

zebra_long_min = int(min(zebra.iloc[:,1]))
zebra_long_max = math.ceil(max(zebra.iloc[:,1]))
zebra_lat_min = int(min(zebra.iloc[:,2]))
zebra_lat_max = math.ceil(max(zebra.iloc[:,2]))


zebra_h = 0.1
nb_long_interval = (zebra_long_max - zebra_long_min)/zebra_h
nb_lat_interval = (zebra_lat_max - zebra_lat_min)/zebra_h


df2 = zebra[(zebra['location-long'] >= 23.5) & (zebra['location-long'] < 23.6) 
& (zebra['location-lat'] >= -19.4) & (zebra['location-lat'] < -19.3)]
box1 = box.Box(df2, 23.5, -19.4)
box1.training_data
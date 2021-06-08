import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
import box

# def import_data(name_file, name_ref):
#    x = pd.read_csv(name_file)
#    ref = pd.read_csv(name_ref)
#    x = pd.DataFrame(x)
#    #print(x.info())
#    ref = pd.DataFrame(ref)
#    return x, ref


# def missing_data(data):
#    data = data.dropna(subset = ['location-long'], axis=0, how='any')
#    data = data.dropna(subset = ['location-lat'], axis=0, how='any')
#    return data


# def pre_processing(data, n):
#    lab = np.zeros((n, 1))
    
#    for i in range(n):
#        # longitude
#        x = int(data.iloc[i, 1])
#        # latitude
#        y = math.ceil(data.iloc[i, 2]) 
#        lab[i, 0] = label(x, y)
#        data.iloc[i, 0] = data.iloc[i, 0][0:10]
    
#    col = pd.DataFrame(lab, columns=['label'])
#    print(col.shape)
#    data = pd.concat((data, col), axis = 1)

#    data = data.drop_duplicates(['timestamp', 'tag-local-identifier'], 'first')
#    data.info()
#    print(data)
#    return data


#def label(x, y):
#    return int((90 - y)*360 + (x-180))


#whale_data, whale_ref = import_data(
#   "../dataset/large marine fauna/blue whales/Blue whales Eastern North Pacific 1993-2008 - Argos Data.csv", 
#    "../dataset/large marine fauna/blue whales/Blue whales Eastern North Pacific 1993-2008 - Argos Data-reference-data.csv")

#zebra_data, zebra_ref= import_data(
#    "../dataset/land predator/zebra/Migratory Burchell's zebra (Equus burchellii) in northern Botswana.csv",
#    "../dataset/land predator/zebra/Migratory Burchell's zebra (Equus burchellii) in northern Botswana-reference data.csv")


#zebra = zebra_data[zebra_data['visible']][['timestamp', 'location-long', 'location-lat', 'tag-local-identifier']]
#zebra = missing_data(zebra)
#zebra_n, p = zebra.shape

#zebra = pre_processing(zebra, zebra_n)
#zebra.to_csv(r'../dataset/land predator/zebra/after_processing.csv', index = False)

zebra = pd.read_csv('../dataset/land predator/zebra/after_processing.csv') 
fig = plt.figure(dpi=128, figsize=(10,6))
plt.axhline(y=-20,ls="-",c="green")
plt.axhline(y=-19,ls="-",c="green")
plt.axhline(y=-21,ls="-",c="green")
plt.axvline(x=23,ls="-",c="green")
plt.axvline(x=24,ls="-",c="green")
plt.axvline(x=25,ls="-",c="green")
plt.axvline(x=26,ls="-",c="green")
plt.scatter(zebra['location-long'], zebra['location-lat'], c='red')
plt.title("location", fontsize=24)
plt.xlabel('longtitude',fontsize=16)
plt.ylabel("latitude", fontsize=16)
plt.tick_params(axis='both', which="major", labelsize=16)
 
plt.show()
   
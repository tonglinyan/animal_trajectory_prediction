import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

def import_data(name_file, name_ref):
    x = pd.read_csv(name_file)
    ref = pd.read_csv(name_ref)
    x = pd.DataFrame(x)
    #print(x.info())
    ref = pd.DataFrame(ref)
    return x, ref


def missing_data(data):
    data = data.dropna()
    data = data.reset_index(drop=True)
    return data


def pre_processing(data, n):
    lab = np.zeros((n, 1))
    
    for i in range(n):
        # longitude
        x = math.floor(data.iloc[i, 1])
        # latitude
        y = math.ceil(data.iloc[i, 2]) 
        lab[i, 0] = label(x, y)
        print(label(x, y))
        data.iloc[i, 0] = data.iloc[i, 0][0:10]
    
    col = pd.DataFrame(lab, columns=['label'])
    data = pd.concat((data, col), axis = 1)
    data = data.drop_duplicates(['timestamp', 'tag-local-identifier'], 'first')
    data = data.reset_index(drop = True)
    labels = []
    for i in data['label']:
        if i not in labels:
            labels.append(i)
    return data, labels


def label(x, y):
    return int((90 - y) * 360 + (x + 180))


def point_plot(data):
    fig = plt.figure(dpi=128, figsize=(10,6))
    plt.axhline(y=-20,ls="-",c="green")
    plt.axhline(y=-19,ls="-",c="green")
    plt.axhline(y=-21,ls="-",c="green")
    plt.axvline(x=23,ls="-",c="green")
    plt.axvline(x=24,ls="-",c="green")
    plt.axvline(x=25,ls="-",c="green")
    plt.axvline(x=26,ls="-",c="green")
    plt.scatter(data['location-long'], data['location-lat'], c='red')
    plt.title("location", fontsize=24)
    plt.xlabel('longtitude',fontsize=16)
    plt.ylabel("latitude", fontsize=16)
    plt.tick_params(axis='both', which="major", labelsize=16)    
    plt.show()

def get_date_list(begin_date, end_date):
    date_list = [x.strftime('%Y-%m-%d') for x in list(pd.date_range(start=begin_date, end=end_date))]
    date_list = {'date': date_list}
    date_list = pd.DataFrame(date_list)
    return date_list


def labels(data):
    col = []
    for i in data['label']:
        if i not in col:
            col.append(i)
    #for i in range(len(col)):
    #    col[i] = '%i' % col[i]
    return col


def box_time_series(data, date, ind):

    for i in data['timestamp']:
        #print(date.iloc[date[(date['date'] == i)].index, ind+1])
        date.iloc[date[(date['date'] == i)].index, ind] += 1
    #print(date)
    return date


def plot_colored(df):
    zebra1 = df.iloc[1:203] #id=3864
    zebra2 = df.iloc[204:478] #id=3743
    zebra3 = df.iloc[479:749] #id=3866
    zebra4 = df.iloc[750:1070] #id=6402
    zebra5 = df.iloc[1071:1287] #id=6405
    zebra6 = df.iloc[1288:1551] #id=6407
    zebra7 = df.iloc[1552:1793] #id=6399

    fig = plt.figure(dpi=300, figsize=(10,6))

    plt.axhline(y=-20,ls="-",c="black")
    plt.axhline(y=-19,ls="-",c="black")
    plt.axhline(y=-21,ls="-",c="black")
    plt.axvline(x=23,ls="-",c="black")
    plt.axvline(x=24,ls="-",c="black")
    plt.axvline(x=25,ls="-",c="black")
    plt.axvline(x=26,ls="-",c="black")
    plt.plot(zebra1['location-long'], zebra1['location-lat'], 'o', markersize = 3, c='firebrick')
    plt.plot(zebra2['location-long'], zebra2['location-lat'], 'o', markersize = 3, c='gold')
    plt.plot(zebra3['location-long'], zebra3['location-lat'], 'o', markersize = 3, c='greenyellow')
    plt.plot(zebra4['location-long'], zebra4['location-lat'], 'o', markersize = 3, c='dodgerblue')
    plt.plot(zebra5['location-long'], zebra5['location-lat'], 'o', markersize = 3, c='royalblue')
    plt.plot(zebra6['location-long'], zebra6['location-lat'], 'o', markersize = 3, c='gray')
    plt.plot(zebra7['location-long'], zebra7['location-lat'], 'o', markersize = 3, c='orange')

    plt.title('location', fontsize=24)
    plt.xlabel('longtitude',fontsize=16)
    plt.ylabel('latitude', fontsize=16)
    plt.tick_params(axis='both', which="major", labelsize=16)
    
    plt.savefig('../figures/zebra/point.png')
    plt.show()
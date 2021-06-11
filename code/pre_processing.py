import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
import brewer2mpl

def import_data(name_file):
    x = pd.read_csv(name_file)
    x = pd.DataFrame(x)
    return x


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


def scatter_plot(data, path):
    
    id = np.unique(data['tag-local-identifier'])
    nb = len(id)
    
    max = data[['location-long','location-lat']].max(axis=0)
    min = data[['location-long','location-lat']].min(axis=0)
    
    max_long = math.ceil(max[0])
    max_lat = math.ceil(max[1])
    min_long = math.floor(min[0])
    min_lat = math.floor(min[1])
    
    #print(max_long, max_lat, min_long, min_lat)
    color = ['firebrick', 'black', 'blue', 'greenyellow', 'gold', 'grey', 'orange', 'violet', 'green', 'pink', 'dodgerblue', 'blueviolet', 'red', 'yellow', 'slategrey']
    
    #color = brewer2mpl.get_map('RdYlGn', 'diverging', nb).mpl_colors
    fig = plt.figure(dpi=128, figsize=(10,6))
    
    for i in range (nb):
        animal = data[data['tag-local-identifier'] == id[i]]
        plt.plot(animal['location-long'], animal['location-lat'], 'o', markersize = 3, color = color[i], label = id[i])

    for j in range (min_lat,max_lat+1) :
        plt.axhline(y = j, ls = "--", c = "black", lw = 0.3)
                            
    for k in range (min_long, max_long+1) :
        plt.axvline(x = k, ls = "--", c = "black", lw = 0.3)
        
    plt.title('location', fontsize=24)
    plt.xlabel('longtitude',fontsize=16)
    plt.ylabel('latitude', fontsize=16)
    plt.tick_params(axis='both', which="major", labelsize=16)
    plt.legend(loc='best')
    plt.savefig(path)
    plt.show()
import os
from matplotlib.pyplot import switch_backend
import pandas as pd
import numpy as np
import math

def import_data(num_colony):
    path = "../dataset/insect/ant/tracking data/ant tracking data/Colony %i/Colony_%i_low_density_locations" % (num_colony, num_colony) #文件夹目录
    files= os.listdir(path) # get all the files in the folder
    
    if ('.DS_Store' in files):
        files.remove('.DS_Store')

    index = 0
    return_matrix = []

    #print(files)

    for file in files: # iterator for traversing all the files
        if not os.path.isdir(file): # check if it is a file  
            f = open(path+"/"+file) # open the file
            #print(f)
            df = pd.read_table(f, sep = ',') 
            data = df.values
            data = pd.DataFrame(data)

            data.columns = ['time', 'location_x', 'location_y', 'chamber']
            ant_id = np.ones((data.shape[0],1))*index
            colony_id = np.ones((data.shape[0],1))*num_colony
            ant_id = pd.DataFrame(ant_id, columns = ['ant_id'])
            colony_id = pd.DataFrame(colony_id, columns = ['colony_id'])
            data = pd.concat([data, ant_id], axis = 1)
            data = pd.concat([data, colony_id], axis = 1)

            if (index == 0):
                return_matrix = data
            else:
                return_matrix = pd.concat([return_matrix, data], axis = 0)
            index += 1
     
    return return_matrix


def minmax(data):    
    id = np.unique(data['chamber'])
    min = [[0]*(len(id)-1)for _ in range (2)]
    max = [[0]*(len(id)-1)for _ in range (2)]

    ant = data[(data['chamber']!=0)]
    for j in range (len(id)-1):
        a = ant[ant['chamber'] == j+1]
        max[0][j] = a['location_x'].max(axis=0)
        max[1][j] = a['location_y'].max(axis=0)
        min[0][j] = a['location_x'].min(axis=0)
        min[1][j] = a['location_y'].min(axis=0)
     
    return min, max


def discretization_time(data):

    data = data[(data.time == 1) | (data.time % 5 == 1)]
    data = data.reset_index(drop=True)

    return data


def location_in_mm(data):

    df = data
    return_matrix = []
    min, max = minmax(data)

    for i in range(5):

        if (i == 0):
            return_matrix = df[df.chamber == i]

        else: 
            data = df[df.chamber == i]

            h_x = (max[0][i-1] - min[0][i-1])/60
            h_y = (max[1][i-1] - min[1][i-1])/40

            x = data['location_x']
            x = np.array(x)
            y = data['location_y']
            y = np.array(y)

            min_x = np.ones((len(x),))*min[0][i-1]
            min_y = np.ones((len(x),))*min[1][i-1]
            
            dif_y = np.ones((len(x),))*(i-1)*(40+6)

            x = np.round((x - min_x)/h_x, 2)
            y = np.round((y - min_y)/h_y+dif_y, 2)
            
            data['location_x'] = x
            data['location_y'] = y
    
            return_matrix = pd.concat([return_matrix, data], axis = 0)
    
    return_matrix = return_matrix.sort_index(axis = 0)
    return_matrix = tunnel(return_matrix)

    return return_matrix



def tunnel(data):

    zero_list = np.where(data['chamber'] == 0)

    while (len(zero_list[0])):

        a = zero_list[0][0]
        b = a + 1
        a = a - 1

        while (data.iloc[b, 3] == 0):
            b += 1

        if (data.iloc[a, 4] == data.iloc[b, 4]):

            if (data.iloc[a, 3] != data.iloc[b, 3]):

                m = math.floor((data.iloc[a, 3] + data.iloc[b, 3])/2)

                for i in range(a+1, b):
                    data.iloc[i, 1] = 1
                    data.iloc[i, 2] = (40 + 6) * m - 3
            
            else:
                if ((data.iloc[a, 2] - 46 * (data.iloc[a, 3]-1) < 20) 
                & (data.iloc[b, 2] - 46 * (data.iloc[a, 3]-1) < 20) 
                & (data.iloc[a, 3] != 1)):
                    m = data.iloc[a, 3] - 1
                    for i in range(a+1, b):
                        data.iloc[i, 1] = 1
                        data.iloc[i, 2] = (40 + 6) * m - 3

                if ((data.iloc[a, 2] - 46 * (data.iloc[a, 3]-1) > 20) 
                & (data.iloc[b, 2] - 46 * (data.iloc[a, 3]-1) > 20) 
                & (data.iloc[a, 3] != 4)):
                    m = data.iloc[a, 3]
                    for i in range(a+1, b):
                        data.iloc[i, 1] = 1
                        data.iloc[i, 2] = (40 + 6) * m - 3
            
        for i in range(a+1, b):
            data.iloc[i, 3] = 5

        zero_list = np.where(data['chamber'] == 0)

    return data


def discretization_location(data):

    labels = np.zeros((len(data), 1))
    for i in range(len(data)):
        x = data.iloc[i, 1]
        y = data.iloc[i, 2]

        if (y <= 40):
            label = math.ceil(y/5) * math.ceil(x/5)
        else:
            if (y <= 46):
                label = 97
            else:
                if (y <= 86):
                    label = math.ceil((y-6)/5) * math.ceil(x/5) + 1
                else:
                    if (y <= 92):
                        label = 194
                    else: 
                        if (y <= 132):
                            label = math.ceil((y-12)/5) * math.ceil(x/5) + 2
                        else:
                            if (y <= 138):
                                label = 291
                            else:
                                #print(i, x, y)
                                label = math.ceil((y-18)/5) * math.ceil(x/5) + 3

        labels[i, 0] = label

    labels = pd.DataFrame(labels, columns = ['label'])
    data = pd.concat([data, labels], axis = 1)
    return data


def time_series(data):

    time_list = pd.DataFrame(np.unique(data.time), columns = ['time'])
    index = np.arange(388)
    lab = np.zeros((len(time_list), 388))
    lab = pd.DataFrame(lab, columns = index)
    time_list = pd.concat([time_list, lab], axis = 1)
    #print(time_list.shape)
    
    for i in range(len(time_list)):
        for j in index:
            print(data[(data['time'] == time_list.time[i]) & (data['label'] == j)].index.tolist())
            num = len(data[(data['time'] == time_list.time[i]) & (data['label'] == j)].index.tolist())
            
            time_list.iloc[i, j+1] = num
    '''
    for i in range(len(data)):
        ind = np.where(time_list['time'] == data.iloc[i, 0])       
        tmp = data.iloc[i, 6] + 1
        print(ind[0][0], tmp)
        time_list.iloc[int(ind[0][0]), int(tmp)] += 1
    '''
    return data, time_list

#data = import_data(1)
#data = pd.concat([data, import_data(2)], axis = 0)
#data = pd.concat([data, import_data(3)], axis = 0)
#data.to_csv('../dataset/insect/ant/after_processing.csv', index = False)


#data = pd.read_csv('../dataset/insect/ant/after_processing.csv')
#data = discretization_time(data)
#data.to_csv('../dataset/insect/ant/time_discretized.csv', index = False)

"""
data = pd.read_csv('../dataset/insect/ant/time_discretized.csv')
data1 = []
for i in range(1, 4):
    df = location_in_mm(data[data.colony_id == i])
    if (i == 1):
        data1 = df
    else:
        data1 = pd.concat([data1, df], axis = 0)

data = data1
print(data)
data.to_csv('../dataset/insect/ant/location_in_mm.csv', index = False)

data = pd.read_csv('../dataset/insect/ant/location_in_mm.csv')
data = discretization_location(data)
print(data)
data.to_csv('../dataset/insect/ant/data_labelled.csv', index = False)
"""
data = pd.read_csv('../dataset/insect/ant/data_labelled.csv')
data, time_list = time_series(data)
time_list.to_csv('../dataset/insect/ant/time_series.csv', index = False)
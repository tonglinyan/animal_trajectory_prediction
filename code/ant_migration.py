import os
import pandas as pd
import numpy as np

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

    for i in range(4):
        h_x = (max[0][i] - min[0][i])/60
        h_y = (max[1][i] - min[1][i])/40

        data = df[df.chamber == i+1]

        x = data['location_x']
        x = np.array(x)
        y = data['location_y']
        y = np.array(y)

        min_x = np.ones((len(x),))*min[0][i]
        min_y = np.ones((len(x),))*min[1][i]
        
        dif_y = np.ones((len(x),))*i*(40+6)

        x = (x - min_x)/h_x
        y = (y - min_y)/h_y+dif_y
        
        data['location_x'] = x
        data['location_y'] = y
        
        if (i == 0):
            return_matrix = data
        else:
            return_matrix = pd.concat([return_matrix, data], axis = 0)

    return return_matrix



def tunnel(data):
    return data


def discretization_location(data):
    return data


#data = import_data(1)
#data = pd.concat([data, import_data(2)], axis = 0)
#data = pd.concat([data, import_data(3)], axis = 0)
#data.to_csv('../dataset/insect/ant/after_processing.csv', index = False)


#data = pd.read_csv('../dataset/insect/ant/after_processing.csv')
#data = discretization_time(data)
#data.to_csv('../dataset/insect/ant/time_discretized.csv', index = False)


data = pd.read_csv('../dataset/insect/ant/time_discretized.csv')
data1 = []
for i in range(1, 4):
    df = location_in_mm(data[data.colony_id == i])
    if (i == 1):
        data1 = df
    else:
        data1 = pd.concat([data1, df], axis = 0)

data = data1.sort_index(axis = 0)
print(data)
data.to_csv('../dataset/insect/ant/location_in_mm.csv', index = False)

data = pd.read_csv('../dataset/insect/ant/location_in_mm.csv')

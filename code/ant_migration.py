import os
import pandas as pd
import numpy as np

def import_data(num_colony):
    path = "../dataset/insect/ant/tracking data/ant tracking data/Colony %i/Colony_%i_low_density_locations" % (num_colony, num_colony) #文件夹目录
    files= os.listdir(path) # get all the files in the folder
    index = 0
    return_matrix = []
    for file in files: # iterator for traversing all the files
        if not os.path.isdir(file): # check if it is a file  
            f = open(path+"/"+file) # open the file
            df = pd.read_table(f, sep = ',') # 
            data = df.values #
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
            """
            iter_f = iter(f); # iterator for reading
            for line in iter_f:
                line = line.strip('\n')
                list_from_line = line.split(',')
                s = s.append(list_from_line axis = 0)
                index += 1
            """
    # print(return_matrix)
    #arr = np.ones((return_matrix.shape[0],1))*num_colony
    #arr = pd.DataFrame(arr, columns = ['colony_id'])
    #return_matrix = pd.concat([return_matrix, arr], axis = 1)
    return return_matrix

data = import_data(1)
data = pd.concat([data, import_data(2)], axis = 0)
data = pd.concat([data, import_data(3)], axis = 0)
print(data)

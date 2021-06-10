import pandas as pd
import math

class Box:

    def __init__(self, data, date, label):
        self.label = label
        self.data = data
        self.date = date
        self.n, self.p = data.shape
        for i in self.data['timestamp']:
            self.date.iloc[self.date[self.date['date'] == i].index.tolist(), 1] += 1
        print(date)
        #self.n_training = math.ceil(self.n * 0.75)
        #self.training_data = self.time_series[0:self.n_training]
        #self.testing_data = self.time_series[self.n_training:self.n]
        #print(self.training_data)
        #print(self.testing_data)
        date.to_csv(r'../dataset/land predator/zebra/date_number_%s.csv'%label, index = False)
        data.to_csv(r'../dataset/land predator/zebra/box_%s.csv'%label, index = False)


    
    
    
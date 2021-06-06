import pandas as pd
import math

class Box:
    x = 0
    y = 0
    time_series = []
    training_data = []
    testing_data = []
    n = 0
    n_training = 0
    
    def __init__(self, x, y, time):
        self.x = x
        self.y = y
        self.time_series = time
        self.n, p = self.time_series.shape
        for i in range(self.n):
            self.time_series.iloc[i, 0] = self.time_series.iloc[i, 0][0:10]
        self.time_series = self.time_series.drop_duplicates(['timestamp', 'tag-local-identifier'], 'first')
        self.n, p = self.time_series.shape
        self.n_training = math.ceil(self.n * 0.75)
        self.training_data = self.time_series[0:self.n_training]
        self.testing_data = self.time_series[self.n_training:self.n]
        print(self.training_data)
        print(self.testing_data)


    def getX(self):
        return self.x

    def getY(self):
        return self.y
    
    
    
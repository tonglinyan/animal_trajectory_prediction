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
        self.n, p = time_series.shape
        for i in range(n):
            self.time_series[i, 1] = self.time_series[i, 1][0:10]
        self.time_series = self.time_series.drop_duplicates()
        self.n, p = self.time_series
        self.n_training = int(n * 0.75)
        self.training_data = self.time_series[0:n_training]
        self.testing_data = self.time_series[n_training:n]

    def getX(self):
        return self.x

    def getY(self):
        return self.y
    
    
    
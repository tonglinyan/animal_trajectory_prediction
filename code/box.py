class box:
    __x = 0
    __y = 0
    __time_series = []
    __training_data = []
    __testing_data = []
    __n = 0
    __n_training = 0
    
    def __init__(self, x, y, time):
        self.__x = x
        self.__y = y
        self.__n, p = time.shape
        self.__time = time

    def getX(self):
        return __x

    def getY(self):
        return __y
    
    def discretisation(self, date):

    
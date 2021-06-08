from statsmodels.tsa.ar_model import AutoReg 
from statsmodels.tsa.arima.model import ARIMA 
from statsmodels.tsa.statespace.sarimax import SARIMAX
from random import random

# AR example
def ar_model():
    # contrived dataset
    data = [x + random() for x in range(1, 100)] 
    # fit model
    model = AutoReg(data, lags=1)
    model_fit = model.fit()
    # make prediction
    yhat = model_fit.predict(len(data), len(data)) 
    print(yhat)


# MA example
def ma_model():
    # contrived dataset
    data = [x + random() for x in range(1, 100)]
    # fit model
    model = ARIMA(data, order=(0, 0, 1)) 
    model_fit = model.fit()
    # make prediction
    yhat = model_fit.predict(len(data), len(data)) 
    print(yhat)


# ARMA example
def arma_model():
    # contrived dataset
    data = [random() for x in range(1, 100)]
    # fit model
    model = ARIMA(data, order=(2, 0, 1)) 
    model_fit = model.fit()
    # make prediction
    yhat = model_fit.predict(len(data), len(data)) 
    print(yhat)


# ARIMA example
def arima_model():
    # contrived dataset
    data = [x + random() for x in range(1, 100)] 
    # fit model
    model = ARIMA(data, order=(1, 1, 1)) 
    model_fit = model.fit()
    # make prediction
    yhat = model_fit.predict(len(data), len(data), typ='levels') 
    print(yhat)


# SARIMA example
def sarima_model():
    # contrived dataset
    data = [x + random() for x in range(1, 100)]
    # fit model
    model = SARIMAX(data, order=(1, 1, 1), seasonal_order=(0, 0, 0, 0)) 
    model_fit = model.fit(disp=False)
    # make prediction
    yhat = model_fit.predict(len(data), len(data))
    print(yhat)

AR_model()
MA_model()
ARMA_model()
ARIMA_model()
SARIMA_model()
from methods.svm import SVM
from preparers import ticker_svm
from core.functions import forecast
from core.simulation import simulate_trades_continuous

from loaders.alphavantage import get_ticker_data
from utils.viz import plot_time_series, plot_balance, plot_balance_vs_price

import pandas as pd
import numpy as np
import ant_migration

def experiment(data):
    # Step 1: Data Loading
    #data = pd.read_csv('../dataset/insect/ant/location_in_mm.csv')
    #data_df = data[(data['colony_id'] == 1) & (data['ant_id']== 0)][['time', 'location_x', 'location_y', 'chamber']]
    #data_df.reset_index(drop = True, inplace = True)
    #n, p = data_df.shape
    data_df = data

    # Step 2: Data Preparation
    x_features, y_features = data_df[['time', 'location_x', 'location_y']], data_df['chamber']
    ground_truth, start_t = y_features.to_numpy(), 5
    print('x feature')
    print(x_features, y_features)
    print("ground_truth, start_t")
    print(ground_truth, start_t)
    # Step 3: Forecasting
    predictions = forecast(method=SVM(), data=(x_features, y_features), start_t=start_t, look_back=14)
    # Step 4: Simulation
    balances = simulate_trades_continuous(predictions=predictions, ground_truth=ground_truth, slowed=False, verbose=False)
    # Step 5: Visualization
    plot_time_series(ts_1=predictions, ts_label_1='SVM', ts_2=ground_truth, ts_label_2='Close', title='SVM predictions vs. ground truth')
    plot_balance(data=balances)
    plot_balance_vs_price(balances=balances, price=ground_truth[1:], title='balance vs. price')

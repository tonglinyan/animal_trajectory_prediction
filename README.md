# animal_migration_forcasting
In this repository, we try to forecasting the ants trajectory and birds spring migration with methods ARIMA(VARMA) and random forest regression.

# Ant

## Dataset





# Bird
## Dataset
You can download dataset "radar_narr_combine.csv.gz" and decompress it, then you will get a complete dataset in the forme of csv.

## Data processing
By executing the code "bird_data_processing", you will get all the time series for the modeling and forecasting part, including 
	"time_filled_AR.csv" time series of bird density with missing data filled by AR model
	"time_weather_filled.csv" time series of weather information without altitude filled by AR model
	"time_weather_filled_radar.csv"s time series of weather information for each radar with altitude filled by AR model
	"radar.csv" list of all the radar ids

## Modeling and Forecasting
### ARIMA
You need files "time_filled_AR.csv" to do the ARIMA forecasting. "bird_forecasting_arima"

### Random Forest
"bird_forecasting_RFR" tests with different features.
"bird_forecasting_RFR_hyperpar" is used to tune the hyperparameters "n_estimators" and "max_depth".
"config.json" has the parameters with best performance given by the hyperparameter tuning.
"bird_forecasting_RFR_best" gives the best performance by importing the "config.json".
In order to run the code, you need all the dataset mentioned before.

# animal_migration_forcasting
In this repository, we try to forecasting the ants trajectory and birds spring migration with methods ARIMA(VARMA) and random forest regression.

# Ant
The goal of this part is to predict the number of chamber where ants stay with ARIMA method.

## Dataset
To get the dataset of ant, download the compressed file "data_ant" and decompress. There's a further explaination of dataset in the "data_ant".

## Data processing

For the ants, there's no missing data. We can get a complete data by combining all the individual ones with "ang_processing.ipynb".

## Modeling and Forecasting

	"ant_forecasting_arima.ipynb" predicts the number of chamber directly.
	"ant_location_forecasting.ipynb" predicts the location of ant, and transfers the location to the number of chamber.
	"ant_evaluation.ipynb" calculates the accuracy, recall, precision and f1-score.


# Bird
The goal of this part is to predict the spring migration of bird (more specifically density of birds) with ARIMA method and random forest method.
## Dataset
You can download dataset "radar_narr_combine.csv.gz" and decompress it, then you will get a complete dataset in the forme of csv.

## Data processing
By executing the code "bird_data_processing.ipynb", you will get all the time series for the modeling and forecasting part, including 
	
	"time_filled_AR.csv" time series of bird density with missing data filled by AR model
	"time_weather_filled.csv" time series of weather information without altitude filled by AR model
	"time_weather_filled_radar.csv"s time series of weather information for each radar with altitude filled by AR model
	"radar.csv" list of all the radar ids

## Modeling and Forecasting
### ARIMA
You need files "time_filled_AR.csv" to do the ARIMA forecasting. "bird_forecasting_arima.ipynb"

### Random Forest
	"bird_forecasting_RFR.ipynb" tests with different features.
	"bird_forecasting_RFR_hyperpar.ipynb" is used to tune the hyperparameters "n_estimators" and "max_depth".
	"config.json.ipynb" has the parameters with best performance given by the hyperparameter tuning.
	"bird_forecasting_RFR_best.ipynb" gives the best performance by importing the "config.json".
In order to run the code, you need all the dataset mentioned before.

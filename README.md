# CAD-USD-Price-Forecast

This repo contains files showing the different stages of creating the CAD-USD Price Forcast model, the packaged model and the raw dataset.

# CAD-USD_Price_Part_1_Data_Analysis.ipynb
This file conains the following steps taken to clean & analyse the data (historical cad-usd exchange prices)

  1. Data Exploration: I explored the dataset to check the columns, no of data points, the distribution of the exchange prices and to check if there are any missing values in the dataset. 
  2. Data cleaning: After exploring the dataset, I removed irrelevant columns and missing values. I also transformed 'Date' column into a datetime object and set this column as the index with a business day frequency.
  3. Data Visualization: I used a line plot to observe how the CAD-USD price has changed over the past five years and a box plot to observe the distribution of the exchange price in each year. 
  I also generated Autocorrelation & Partial Auto Correlation plots as well as plots to show the Error, trends & seasonality component of the data.
  4. Additional Analysis: I analysed the data to check for Stationarity, trends & seasonality.
  
  # CAD-USD_PricePart_2_Implementing_Forecast_Models.ipynb
  After analysing the dataset, I used the dataset to predict future prices using the following forecast models:
    1. Holt-Winters Triple Exponential Smoothing
    2. Auto Regression Model
    3. AutoRegressive Integrated Moving Average (ARIMA)
    4. Recurrent Neural Network
    5. Facebook Prophet
  Each model's performance was evaluated based on:
  1. RMSE
  2. Ability of the model to forecat the future trends
  
# CAD-USD_Final_ML_Pipeline.ipynb: contains the final pipeline for forecasting the future price using FB Prophet model

# CADUSD_forecast_package
This package contains the pipeline (production code) of the ML model - forecast_model, the requirements, tests as well as other set up files. The model has also been uploaded
to the python package index, you can use this model by running this command "import forecast_model"


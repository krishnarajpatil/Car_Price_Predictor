<h1 align="center" style="margin-top: 0px;">END TO END MACHINE LEARNING PROJECT</h1>
<h1 align="center" style="margin-top: 0px;">CAR PRICE PREDICTOR</h1>
<p align="center" style="margin-bottom: 0px !important;">
  <img  src="https://github.com/krishnarajpatil/Car_Price_Predictor/blob/main/static/images/initial_page.PNG" alt="initial page" align="center">
</p>
<h2 align="center" style="margin-top: 0px;">Aim</h2>
This project aims to predict the Price of an used Car by taking it's Company name, it's Model name, Year of Purchase, and other parameters.
<p align="center" style="margin-bottom: 0px !important;">
  <img  src="https://github.com/krishnarajpatil/Car_Price_Predictor/blob/main/static/images/data_predicted.PNG" alt="data_predicted" align="center">
</p>
<h2 align="center" style="margin-top: 0px;">How to use?</h2>

1. Clone the repository
2. Install the required packages in "requirements.txt" file.

Some packages are:
 - numpy 
 - pandas 
 - scikit-learn

3. Run the "application.py" file
And you are good to go. 
<h2 align="center" style="margin-top: 0px;">What this project does?</h2>

1. This project takes the parameters of an used car like: Company name, Model name, Year of Purchase, Fuel Type and Number of Kilometers it has been driven.
2. It then predicts the possible price of the car. For example, the image below shows the predicted price of Chevrolet Enjoy 1.4. 
<p align="center" style="margin-bottom: 0px !important;">
  <img  src="https://github.com/krishnarajpatil/Car_Price_Predictor/blob/main/static/images/data_predicted.PNG" alt="data_predicted" align="center">
</p>
<h2 align="center" style="margin-top: 0px;">How this project does?</h2>

1. First of all the data was scraped from Quikr.com (https://quikr.com) 
Link for data: https://github.com/krishnarajpatil/Car_Price_Predictor/blob/main/notebook/data/quikr_car.csv

2. Then data cleaned (It was super uncleand.) and analysed.

3. Then a it data tested with different models like Linear Regression, Ridge & Lasso regression, K-Neighbors Regressor, Decision Tree, Random Forest Regressor, XGBRegressor, CatBoosting Regressor and AdaBoost Regressor. XGBoost Regressor model was built on top of it which had 0.91 R2_score.

Link for notebook: https://github.com/rajtilakls2510/car_price_predictor/blob/master/Quikr%20Analysis.ipynb

4. This project was given the form of an website built on Flask where we used the XGBoost Regressor model to perform predictions.

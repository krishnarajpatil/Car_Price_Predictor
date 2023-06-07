from flask import Flask, render_template, request
# from flask_cors import CORS, cross_origin
import pandas as pd
import numpy as np
import pickle

app = Flask(__name__)
car = pd.read_csv('notebook/data/cleaned_car_data.csv')
model = pickle.load(open('model/car_price_pred_Model.pkl', 'rb'))


@app.route('/', methods=['GET', 'POST'])
def index():
    companies = sorted(car['company'].unique())
    car_models = sorted(car['name'].unique())
    years = sorted(car['year'].unique(), reverse=True)
    fuel_type = car['fuel_type'].unique()

    companies.insert(0, 'Select Company')
    years.insert(0, 'Select Year')
    return render_template('index.html', companies=companies, car_models=car_models, years=years, fuel_types=fuel_type)


@app.route('/predict', methods=['POST'])
def predict():
    company = request.form.get('company')
    car_model = request.form.get('car_model')
    year = int(request.form.get('year'))
    fuel_type = request.form.get('fuel_type')
    kms_driven = int(request.form.get('kilo_driven'))
    # print(company, car_model, year, kms_driven, fuel_type)
    # print(type(company), type(car_model), type(year), type(kms_driven), type(fuel_type))

    prediction = model.predict(pd.DataFrame([[car_model, company, year, kms_driven, fuel_type]],
                                            columns=['name', 'company', 'year', 'kms_driven', 'fuel_type']))
    # print(prediction[0])

    return str(np.round(prediction[0], 2))


if __name__ == '__main__':
    app.run(debug=True)

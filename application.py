# import pickle

# from flask import Flask,request,jsonify,render_template
# import numpy as np
# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import StandardScaler
# from sklearn.decomposition import PCA
# from sklearn.linear_model import LinearRegression
# from sklearn.ensemble import RandomForestRegressor
# from xgboost import XGBRegressor
# from sklearn.metrics import r2_score
# import matplotlib.pyplot as plt
# import seaborn as sns


# application =Flask(__name__)
# app=application

# import joblib

# model = joblib.load("models/xgb_carbon_credit_model.pkl")
# scaler = joblib.load("models/scaler.pkl")
# pca = joblib.load("models/pca_transform.pkl")



# @app.route("/")
# def hellow_world():
#     return render_template('index.html')
# # if __name__ == "__main__":
# #     app.run(host="0.0.0.0")

# # Prediction route
# @app.route("/predict", methods=["GET", "POST"])
# def predict():
#     if request.method == "POST":
#         try:
#             # Extract input from form
#             BD = float(request.form["BD"])
#             soil_moisture = float(request.form["Soil_Moisture_%"])
#             pH = float(request.form["pH"])
#             CEC = float(request.form["CEC"])
#             SOC_stock = float(request.form["SOC_stock"])

#             # Preprocess
#             features = np.array([[BD, soil_moisture, pH, CEC, SOC_stock]])
#             scaled = scaler.transform(features)
#             pca_features = pca.transform(scaled)

#             # Predict
#             prediction = model.predict(pca_features)[0]
#             return render_template("index.html", prediction_text=f"🌱 Predicted Carbon Credits per Hectare: {prediction:.2f}")

#         except Exception as e:
#             return render_template("index.html", prediction_text=f"❌ Error: {str(e)}")
    
#     # If GET method, just show form
#     return render_template("index.html")


# # Run the app
# if __name__ == "__main__":
#     app.run(debug=True)





from flask import Flask, request, render_template
import numpy as np
import pickle

# Initialize Flask app
app = Flask(__name__)

# Load trained model and preprocessing objects
with open("models/xgb_carbon_credit_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("models/scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

with open("models/pca_transform.pkl", "rb") as f:
    pca = pickle.load(f)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        try:
            # Retrieve input values from form
            BD = float(request.form["BD"])
            soil_moisture = float(request.form["Soil_Moisture_%"])
            pH = float(request.form["pH"])
            CEC = float(request.form["CEC"])
            SOC_stock = float(request.form["SOC_stock"])

            # Format input for model
            input_data = np.array([[BD, soil_moisture, pH, CEC, SOC_stock]])
            scaled = scaler.transform(input_data)
            pca_input = pca.transform(scaled)
            prediction = model.predict(pca_input)[0]

            return render_template(
                "index.html",
                prediction_text=f"🌱 Predicted Carbon Credits per Hectare: {prediction:.2f}"
            )

        except Exception as e:
            return render_template("index.html", prediction_text=f"❌ Error: {str(e)}")

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

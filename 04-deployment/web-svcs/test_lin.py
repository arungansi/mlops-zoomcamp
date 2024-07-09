import requests

ride = {
    "PULocationID": 10,
    "DOLocationID": 50,
    "trip_distance": 40
}

# features =predict_lin.prepare_features(ride)
# print(features)
# pred = predict_lin.predict(features)
# print(pred)

url = 'http://localhost:5000/predict_lin'
response = requests.post(url, json=ride)
print(response.json())

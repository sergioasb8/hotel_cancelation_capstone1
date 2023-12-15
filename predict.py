from flask import Flask, request, jsonify
import pickle
import xgboost as xgb

# files path
model_file = './xgboost_model.pkl'
dv_file = './dv.pkl'

# read the model
with open(model_file, 'rb') as f_in:
    model = pickle.load(f_in)

# read the dv
with open(dv_file, 'rb') as f_in:
    dv = pickle.load(f_in)

app = Flask('hotel_cancelation')

@app.route('/hotel_cancelation', methods=['POST'])
def predict():

    data = request.get_json()
    # make predictions
    X = dv.fit_transform(data)
    features = dv.feature_names_
    dX = xgb.DMatrix(X, feature_names=features)
    y_pred = model.predict(dX)[0]

    result = {
        'hotel_cancelation_probability':float(y_pred),
        'hotel_cancelation':bool(y_pred >= 0.5)
    }

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug = True, host = '0.0.0.0', port = 9696)

    
# data = {
#     'lead_time':39,
#     'arrival_year':2019,
#     'avg_price_per_room':102.12,
#     'no_of_special_requests':2,
#     'market_segment_type':1,
# }


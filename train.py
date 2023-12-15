# import libraries
import pandas as pd
import xgboost as xgb
from sklearn.feature_extraction import DictVectorizer
import pickle


data = pd.read_csv('../data/Hotel_Cancelations.csv')
output_model = './xgboost_model.pkl'
output_vectorizer = './dv.pkl'

# prepara the data
most_meaningful_features = ['lead_time','arrival_year','avg_price_per_room','no_of_special_requests','market_segment_type']
df = data[most_meaningful_features + ['booking_status']].copy()

# set x and y data
y = df.booking_status.values
dv = DictVectorizer(sparse=False)
df_dict = df[most_meaningful_features].to_dict(orient='records')
X = dv.fit_transform(df_dict)
features = dv.feature_names_
d_data = xgb.DMatrix(X, label=y, feature_names=features)

# model
xgb_params = {
    'eta': 0.1, 
    'max_depth': 13,
    'min_child_weight': 1,
    
    'objective': 'binary:logistic',
    'nthread': 8,
    
    'seed': 1,
    'verbosity': 1,
}
model = xgb.train(xgb_params, d_data, num_boost_round=100)

# save model an vectorizer
with open(output_model, "wb") as f:
    pickle.dump(model, f)
    
with open(output_vectorizer, "wb") as f:
    pickle.dump(dv, f)
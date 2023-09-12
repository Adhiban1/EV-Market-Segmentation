import pickle

with open('model/car_model.pkl', 'rb') as f:
    car_model = pickle.load(f)

with open('model/scaler_x.pkl', 'rb') as f:
    scaler_x = pickle.load(f)

with open('model/scaler_y.pkl', 'rb') as f:
    scaler_y = pickle.load(f)

def car_price(AccelSec, TopSpeed_KmH, Range_Km, 
              Efficiency_WhKm, FastCharge_KmH, Seats):
    'This function gets AccelSec, TopSpeed_KmH, Range_Km, Efficiency_WhKm\
, FastCharge_KmH and Seats of car. It returns price of car in rupees'
    x = scaler_x.transform([[AccelSec, TopSpeed_KmH, Range_Km, 
                            Efficiency_WhKm, FastCharge_KmH, Seats]])
    y = car_model.predict(x)
    y = scaler_y.inverse_transform(y.reshape(1, -1))
    return y[0][0]*88.8
from flask import Flask, render_template, request
from CarPrice import car_price

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    sample_data = [4.6, 233.0, 450.0, 161.0, 940.0, 5.0]
    fields = ['AccelSec', 'TopSpeed_KmH', 'Range_Km', 
              'Efficiency_WhKm', 'FastCharge_KmH', 'Seats']
    zip_data = list(zip(fields, sample_data))
    price = '---'
    if request.method == 'POST':
        data = [request.form[i] for i in fields]
        zip_data = list(zip(fields, data))
        if data == ['']*len(fields):
            data = [0]*len(fields)
        else:
            data = list(map(float, data))
        price = f'{int(car_price(*data)):,}'
    return render_template('index.html', zip_data=zip_data, price=price)

if __name__ == '__main__':
    app.run()
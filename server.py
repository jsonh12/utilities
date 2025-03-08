from flask import Flask, render_template, request
from src.temp_converter import twoWayConverterV4

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('pages/index.html')

@app.route('/convert', methods=['POST'])
def convert():
    temp_value = float(request.form['temp_value'])
    temp_in_type = request.form['temp_in_type']
    temp_out_type = request.form['temp_out_type']
    result = twoWayConverterV4(temp_value, temp_in_type, temp_out_type)
    return render_template('pages/index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
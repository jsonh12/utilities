from flask import Flask, render_template
from src.temp_converter import twoWayConverterV2, AreaMeasurer


app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/temp')
def temp():
  result = twoWayConverterV2(21, 'C')
  print(result)
  return result

@app.route('/measure')
def measure():
  result = AreaMeasurer('Triangle', 8, 9,'CM')
  print(result)
  return result

if __name__ == '__main__':
  app.run(debug=True)

from flask_cors import *
import json
from flask import Flask,render_template,request,Response,redirect,url_for
app = Flask(__name__)
CORS(app, supports_credentials=True)
@app.route('/')
def index():
    return render_template('scatter-aqi-color.html')


@app.route('/')
def scatter_data():
    data = {}
    data1 = [
  [1, 'smartbox1', 56],[2, 'smartbox2', 21], [3, 'smartbox3', 63],[4, 'smartbox4', 29],[5, 'smartbox5', 44],[5, 'smartbox4', 44],[6, 'smartbox6', 90],
  [7, 'smartbox2', 77],[8, 'smartbox5', 80],[9, 'smartbox4', 280],[10,  'smartbox3', 216],[11,  'smartbox2', 38],[12,  'smartbox6', 40],[13,  'smartbox1', 74],[14,  'smartbox5', 120],[15, 'smartbox4', 116],
  [16,  'smartbox3', 29],[17, 'smartbox1', 110],[18,  'smartbox2', 192],[19,  'smartbox3', 54],[20,  'smartbox5', 17],[21, 'smartbox3', 36],[22,  'smartbox5', 114],
  [23, 'smartbox2', 110],[24, 'smartbox6', 30],[25,  'smartbox2', 43],[26,  'smartbox6', 157],[27, 'smartbox2', 230],[28, 'smartbox3', 186],[29,  'smartbox2', 165],[30,  'smartbox1', 60],[31,  'smartbox1', 49]
]
    data['data1'] = data1
    data2 = [
  [1, 'smartbox2', 37],[2, 'smartbox1', 62],[3, 'smartbox3', 38],[4, 'smartbox4', 21],[5, 'smartbox6', 42],[6, 'smartbox6', 52],[7, 'smartbox3', 30],
  [8, 'smartbox2', 48],[9, 'smartbox1', 85],[10, 'smartbox1', 81],[11, 'smartbox3', 39],[12, 'smartbox5', 51],[13, 'smartbox3', 69],
  [14, 'smartbox5', 105],[15, 'smartbox2', 68],[16, 'smartbox1', 68],[17, 'smartbox6', 27],[18, 'smartbox3', 61],[19, 'smartbox6', 71],
  [20, 'smartbox5', 102],[21, 'smartbox3', 50],[22, 'smartbox4', 94],[23, 'smartbox6', 77],[24, 'smartbox5', 130],[25, 'smartbox4', 84],
  [26, 'smartbox2', 108],[27, 'smartbox2', 48],[28, 'smartbox1', 48],[29, 'smartbox6', 92],[30, 'smartbox3', 116],[31, 'smartbox5', 50]
]
    data['data2'] = data2
    data3 =[
]
    data['data3'] = data3
    return Response(json.dumps(data), mimetype='application/json')



###获取（传递）参数​
@app.route('/alldata')
def alldata():
    d = request.args.get('d')
    return Response(json.dumps(d), mimetype='application/json')

if __name__ == "__main__":
    app.run(host='127.0.0.1', debug=True, threaded=True)


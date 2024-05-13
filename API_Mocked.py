import subprocess
import random
import datetime

from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/get_sensor_data/<sensor_id>', methods=['GET'])
def get_temperature(sensor_id):
    temperature = random.randint(20, 72)
    temperature = 333
    timestamp = int(datetime.datetime.now().timestamp() * 1000)
    return jsonify({'temperature': temperature, 'timestamp': timestamp})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)
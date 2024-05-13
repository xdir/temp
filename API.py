import threading
import time

from flask import Flask, jsonify
from w1thermsensor import W1ThermSensor, Sensor

app = Flask(__name__)

data = {}

sensor_ids = [sensor.id for sensor in W1ThermSensor.get_available_sensors([Sensor.DS18B20])]
print("Available sensors:", sensor_ids)


def update_sensor_readings():
    while True:
        for id in sensor_ids:
            try:
                data[id] = W1ThermSensor(sensor_type=Sensor.DS18B20, sensor_id=id).get_temperature()
            except Exception as e:
                print(f"Error reading sensor {id}: {e}")
                data[id] = None
        time.sleep(2)


thread = threading.Thread(target=update_sensor_readings)
thread.daemon = True
thread.start()


@app.route('/get_sensor_data/<sensor_id>', methods=['GET'])
def get_temperature(sensor_id):
    temperature = data.get(sensor_id)
    if temperature is None:
        return jsonify({'error': 'Temperature not available'}), 503
    return jsonify({'temperature': temperature})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)

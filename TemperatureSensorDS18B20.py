import requests


class TemperatureSensorDS18B20:
    sensor_id = ""

    def __init__(self, sensor_id):
        self.sensor_id = sensor_id

    def get_temperature(self):
        response = requests.get("http://192.168.0.40:8080/temperatura/" + self.sensor_id)
        # print("CODE: ")
        # print(response.status_code)
        # print(response.json())
        # print(response.json()["temperature"])
        return response.json()["temperature"]

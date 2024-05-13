from DS18B20 import DS18B20
from sensor_map import sensors_ids


class Boiler:
    __temp1_sensor = DS18B20(sensors_ids["boiler_temp_1"])
    __temp2_sensor = DS18B20(sensors_ids["boiler_temp_2"])
    __temp3_sensor = DS18B20(sensors_ids["boiler_temp_3"])
    __temp4_sensor = DS18B20(sensors_ids["boiler_temp_4"])
    __temp5_sensor = DS18B20(sensors_ids["boiler_temp_5"])

    def get_temp1(self):
        self.__temp1_sensor.get_temperature()

    def get_temp2(self):
        self.__temp2_sensor.get_temperature()

    def get_temp3(self):
        self.__temp3_sensor.get_temperature()

    def get_temp4(self):
        self.__temp4_sensor.get_temperature()

    def get_temp5(self):
        self.__temp5_sensor.get_temperature()
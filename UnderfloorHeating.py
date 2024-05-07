from Relay import Relay
from TemperatureSensorDS18B20 import TemperatureSensorDS18B20
from sensor_map import sensors_ids


class UnderfloorHeating:

    in_water_temperature = TemperatureSensorDS18B20(sensors_ids["paduodamas"])
    out_water_temperature = TemperatureSensorDS18B20(sensors_ids["gryztamas"])

    __main_circulation_pump_relay = Relay(6)
    __backup_circulation_pump_relay = Relay(7)

    # main circulation pump
    def start_circulation_pump(self):
        print("Starting circulation pump")
        self.__main_circulation_pump_relay.on()

    def stop_circulation_pump(self):
        print("Stopping circulation pump")
        self.__main_circulation_pump_relay.off()

    def is_circulation_pump_on(self):
        self.__main_circulation_pump_relay.is_on()
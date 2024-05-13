from EmergencyDischarge import EmergencyDischarge
from Relay import Relay
from DS18B20 import DS18B20
from sensor_map import sensors_ids


class Fireplace:
    __emergencyDischarge = EmergencyDischarge()
    __water_temperature_sensor = DS18B20(sensors_ids["zidinys"])
    __main_circulation_pump_relay = Relay(6)
    __backup_circulation_pump_relay = Relay(6)

    # emergency cooling
    def start_emergency_cooling(self):
        print("Starting emergency cooling")
        self.__emergency_water_relay.on()
        # tikrinti ismetimo srauta

    def stop_emergency_cooling(self):
        print("Stopping emergency cooling")
        self.__emergency_water_relay.off()

    def is_emergency_cooling_on(self):
        return self.__emergency_water_relay.is_on()

    # circulation pump
    def start_circulation_pump(self):
        print("Starting circulation pump")
        self.__main_circulation_pump_relay.on()

    def stop_circulation_pump(self):
        print("Stopping circulation pump")
        self.__main_circulation_pump_relay.off()

    def is_circulation_pump_on(self):
        self.__main_circulation_pump_relay.is_on();

    def is_heating_on(self):
        return self.__main_circulation_pump_relay.is_on()

    # ========================

    def determine_heating_state(self):
        if self.get_water_temperature() > 25:
            if not self.is_heating_on.is_on():
                self.start_circulation_pump()
        else:
            if self.is_heating_on():
                self.stop_circulation_pump()

    def determine_emergency_cooling(self):
        temperature = self.get_water_temperature()
        if temperature >= 30 and self.is_emergency_cooling_on() == False:
            self.start_emergency_cooling()
        else:
            if self.is_emergency_cooling_on() and temperature <= 28:
                self.stop_emergency_cooling()

    def get_water_temperature(self):
        return self.__water_temperature_sensor.get_temperature()

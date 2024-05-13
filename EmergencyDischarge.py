from Relay import Relay


class EmergencyDischarge:

    __relay = Relay(5)

    def get_discharge_flow(self):
        print("Matuoti koks srautas")

    def start(self):
        print("Starting emergency cooling")
        self.__relay.on()
        # Atidaryti rele
        # tikrinti

    def stop_emergency_cooling(self):
        print("Stopping emergency cooling")
        self.__relay.off()

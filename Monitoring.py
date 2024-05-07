import time
from threading import Thread

from flask import Flask

from Fireplace import Fireplace
from UnderfloorHeating import UnderfloorHeating
from html import return_html

app = Flask(__name__)
underfloorHeating = UnderfloorHeating()
fireplace = Fireplace()


def monitor():
    while True:
        startTime = time.time()
        c1 = fireplace.get_water_temperature()
        fireplace.determine_heating_state(c1)
        fireplace.determine_emergency_cooling(c1)
        # c2 = underfloorHeating.in_water_temperature.get_temperature()
        # c3 = underfloorHeating.out_water_temperature.get_temperature()
        endTime = time.time()
        elapsedTime = (int)((endTime - startTime) * 1000)
        print(f"Elapsed time: {elapsedTime} ms. "
              + "Sleep time=" + str(get_sleep_time()) + " "
              + "Heating=" + str(fireplace.is_heating_on()) + " "
              + str(fireplace.get_water_temperature()) + "C° "
              + "Emergency cooling=" + str(fireplace.is_emergency_cooling_on())
              )
        time.sleep(get_sleep_time())


@app.route('/t')
def status():
    c1 = fireplace.get_water_temperature()
    c2 = underfloorHeating.in_water_temperature.get_temperature()
    c3 = underfloorHeating.out_water_temperature.get_temperature()

    s1 = "Ijungtas" if fireplace.is_heating_on() else "Isjungtas !!!!"
    s2 = "Ijungtas" if underfloorHeating.main_circulation_pump.is_on() else "Isjungtas !!!!"
    s3 = "Isjungtas" if fireplace.is_emergency_cooling_on() else "Isjungtas !!!!"
    return return_html(c1, c2, c3, s1, s2, s3)


def get_sleep_time():
    return 2 if fireplace.is_heating_on() else 10


if __name__ == '__main__':
    monitor_thread = Thread(target=monitor)
    monitor_thread.daemon = True
    monitor_thread.start()
    app.run(host='0.0.0.0', port=8080)

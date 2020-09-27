import os

import psutil


class Temperature:
    def __init__(self):
        self.cpu_temperature = None
        self.update()

    def update(self):
        self.cpu_temperature = self.get_cpu_temperature()

    def get_cpu_temperature(self):
        temperatures = psutil.sensors_temperatures()
        if not 'cpu_thermal' in temperatures:
            return None
        return temperatures['cpu_thermal'][0].current


t = Temperature()
print(t.cpu_temperature)

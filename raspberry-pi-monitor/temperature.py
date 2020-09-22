import os

CPU_TEMPERATURE_FILEPATH = '/sys/class/thermal/thermal_zone0/temp'


class Temperature:
    def __init__(self):
        self.cpu_temperature = None
        self.update()

    def update(self):
        self.cpu_temperature = self.get_cpu_temperature()

    def get_cpu_temperature(self):
        with open(CPU_TEMPERATURE_FILEPATH, 'r') as file:
            t = int(file.read())
            return t / 1000.0


# t = Temperature()
# print(t.cpu_temperature)

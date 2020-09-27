import psutil
import subprocess


class Temperature:
    def __init__(self):
        self.cpu_temperature = None
        self.gpu_temperature = None
        self.update()

    def __str__(self):
        return 'cpu temperature: {}'.format(self.cpu_temperature) + '\n' \
            + 'gpu temperature: {}'.format(self.gpu_temperature)

    def update(self):
        self.cpu_temperature = self.get_cpu_temperature()
        self.gpu_temperature = self.get_gpu_temperature()

    def get_cpu_temperature(self):
        temperatures = psutil.sensors_temperatures()
        if not 'cpu_thermal' in temperatures:
            return None
        return temperatures['cpu_thermal'][0].current

    def get_gpu_temperature(self):
        output = subprocess.check_output(['vcgencmd', 'measure_temp'],
                                         encoding='utf-8')
        return float(output.replace('temp=', '').replace('\'C\n', ''))


t = Temperature()
print(t.cpu_temperature)
print(t.gpu_temperature)
print(t)

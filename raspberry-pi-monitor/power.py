import subprocess


class Power:
    def __init__(self):
        self.throttled = PowerThrottled()
        self.update()

    def __str__(self):
        return "Power throttled: {}".format(self.throttled)

    def update(self):
        self.throttled.update()


THROTTLED_MESSAGES = {
    0: 'Under-voltage detected.',
    1: 'ARM frequency capped.',
    2: 'Currently throttled.',
    3: 'Soft temperature limit active.',
    16: 'Under-voltage has occurred.',
    17: 'ARM frequency capping has occurred.',
    18: 'Throttling has occurred.',
    19: 'Soft temperature limit has occurred.'
}


class PowerThrottled:
    def __init__(self):
        self.status = None
        self.update()

    def __str__(self):
        msgs = []
        for b, m in THROTTLED_MESSAGES.items():
            if (1 << b) & self.status != 0:
                msgs.append(m)
        if not msgs:
            msgs.append('All good!')
        return '\n'.join(msgs)

    def update(self):
        output = subprocess.check_output(['vcgencmd', 'get_throttled'],
                                         encoding='utf-8')
        self.status = int(output.replace('throttled=', '').replace('\n', ''),
                          16)


pt = PowerThrottled()
print(pt)
p = Power()
print(p)

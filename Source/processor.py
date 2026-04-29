from collections import deque
import statistics

# Store last N values
WINDOW_SIZE = 20

temp_window = deque(maxlen=WINDOW_SIZE)
hum_window = deque(maxlen=WINDOW_SIZE)
air_window = deque(maxlen=WINDOW_SIZE)

def parse_data(line):
    try:
        parts = line.split(',')
        data = {}
        for p in parts:
            key, val = p.split(':')
            data[key] = float(val)
        return data
    except:
        return None


def detect_anomaly(value, window):
    if len(window) < WINDOW_SIZE:
        window.append(value)
        return False
    
    mean = statistics.mean(window)
    std = statistics.stdev(window)

    window.append(value)

    if std == 0:
        return False

    # anomaly condition
    if value > mean + 2 * std:
        return True
    return False
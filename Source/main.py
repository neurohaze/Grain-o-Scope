from serial_reader import connect, read_line
from processor import parse_data, detect_anomaly, temp_window, hum_window, air_window
from logger import log_data


import random
import time

def fake_data(): # For testing without hardware
    return f"TEMP:{random.uniform(25,30)},HUM:{random.uniform(50,70)},AIR:{random.uniform(100,200)}"

ser = connect(port='COM5', baud=9600)

print("Listening to Arduino...")

while True:
    if True:
        line = fake_data()
    else:
        line = read_line(ser)
        
    if not line:
        continue

    print("Raw:", line)

    data = parse_data(line)
    if not data:
        continue

    temp_anomaly = detect_anomaly(data['TEMP'], temp_window)
    hum_anomaly = detect_anomaly(data['HUM'], hum_window)
    air_anomaly = detect_anomaly(data['AIR'], air_window)

    anomalies = {
        'TEMP': temp_anomaly,
        'HUM': hum_anomaly,
        'AIR': air_anomaly
    }

    print(f"Processed: {data} | Anomalies: {anomalies}")

    log_data(data, anomalies)
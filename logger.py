import csv
from datetime import datetime

def log_data(data, anomaly_flags):
    with open("data.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            datetime.now(),
            data['TEMP'],
            data['HUM'],
            data['AIR'],
            anomaly_flags['TEMP'],
            anomaly_flags['HUM'],
            anomaly_flags['AIR']
        ])
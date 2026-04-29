import serial

def connect(port='COM5', baud=9600):
    return serial.Serial(port, baud, timeout=1)

def read_line(ser):
    try:
        line = ser.readline().decode().strip()
        return line
    except:
        return None
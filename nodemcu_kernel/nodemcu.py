from serial import Serial
from serial.tools.list_ports import comports

NODEMCU_PID = 29987
NODEMCU_VID = 6790
BAUDRATE = 115200
PARITY = 'N'

def find_nodemcu():
    """
    Returns the port for the first NodeMcu found connected to the computer.
    """
    for port in comports():
        if port.vid == NODEMCU_VID and port.pid == NODEMCU_PID:
            return port.device

def connect():
    """
    Returns a pySerial Serial object to talk to the nodemcu
    """
    s = Serial(find_nodemcu(), BAUDRATE, parity=PARITY)
    s.write(b'\x03\x01') # Ctrl-C: interrupt, Ctrl-A: switch to raw REPL
    s.read_until(b'raw REPL')
    s.read_until(b'\r\n>') # Wait for prompt
    return s

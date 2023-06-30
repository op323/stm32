import time
from pyb import UART

uart = UART(3, 9600)

send1 = "a"
send2 = "b"
while(True):
    uart.write(send1)
    time.sleep_ms(1000)
    uart.write(send2)
    time.sleep_ms(1000)

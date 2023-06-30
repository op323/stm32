from fpioa_manager import fm
from machine import UART
import time

fm.register(15, fm.fpioa.UART1_TX, force=True)
fm.register(16, fm.fpioa.UART1_RX, force=True)

uart_A = UART(UART.UART1, 9600, 8, 0, 1, timeout=1000, read_buf_len=4096)

send_char1 = 'a'
send_char2 = 'b'
while True:
    uart_A.write(send_char1)
    time.sleep(1)
    uart_A.write(send_char2)
    time.sleep(1)



from pyModbusTCP.client import ModbusClient
import time

# TCP auto connect on first modbus request
c = ModbusClient(host="172.31.0.21", port=23, unit_id=1, auto_open=True)

while True:
    regs = c.read_holding_registers(0)

    if regs:
        dB = regs[0] / 10
        print(dB, "dB")
    else:
        print("read error")
    time.sleep(1)

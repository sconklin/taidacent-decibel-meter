### Acoustic Sensor

# Description
I was looking for an inexpensive way to record sound levels outdoors. I don't care whether the sensor is traceable to a standard, as long as it's in the ballpark.

I found a sensing device on Ali Express which interfaces with Modbus RS-485, and I also found an ethernet to Modbus RS-485 adapter (from a different vendor). The total price for both was under $60 USD.

The vendor had posted no information for the sensor beyond the sales information. I found a negative product review for the same device that mentioned that the modbus settings were 4800 baud and device address 1. That saved me some experimentation.

I could only get a response from register number 1 on the device, and it contains the dB reading times 10.

This works well so far, and I've included a simple python script which demonstrates reading from the sensor every second.

# Sensor info
* [purchase link](https://www.aliexpress.us/item/3256801639491925.html)
* DC power supply 10-30V Dc
* Maximum power consumption 0.4w
* Output signal RS485/4-20mA/0-5V/0-10V
* Response time≤2S
* Measuring range 30dB-120dB
* Resolution 0.1dB
* Measurement error ± 0.5dB
* Frequency 20Hz- 12.5kHz
* Working temperature -20-60°c
* Working humidity 0%RH~80%RH
* Power consumption≤0.15W at 12V DC,25C
* Working pressure range 0.9-1.1atm
* Brown wire - +10-30 VDC
* Black - Power Supply return
* Yellow - RS485 A
* Blue - RS485 B

# USR-TCP232-304 TCP to RS-485 module info
* [purchase link](https://www.aliexpress.us/item/2255800110028561.html)
* [manual](USR-TCP232-304-User-Manual_V1.0.3.01.pdf)
* Set RS-485 baud rate to 4800
* Part Number USR-TCP232-304
* 5-7V Power Supply
* Default IP Address: 192.168.0.7

## Configuring the USR-TCP232-304

Access device configuration by accessing the default IP address with a browser

---

Set Local IP Config in a way that makes sense for your network

---

Set the Serial Port configuration as shown here.

Change the Baud Rate to 4800 bps

Change the work mode to TCP Server

![Serial Port Setup screen](https://github.com/sconklin/taidacent-decibel-meter/blob/main/serial_port_setup.png?raw=true)

---

Set the Expand Function configuration as shown here

Change Modbus Type to Modbus TCP/RTU

![Expand Function Setup screen](https://github.com/sconklin/taidacent-decibel-meter/blob/main/expand_function_setup.png?raw=true)

---

Set the Misc Config configuration as shown here

Change the admins password

![Expand Function Setup screen](https://github.com/sconklin/taidacent-decibel-meter/blob/main/misc_config_setup.png?raw=true)


# Measured Current Consumption
* Sensor Unit 8 mA @ 12 VDC
* TCP/485 module 140 mA @ 5 VDC

# HekProjek
Open the gate to your property with your phone, using wifi.

Hardware for the project:
  Raspberry Pi Zero Wireless
  Arduino Nano
  2 x NRF24L01 2.4GHz Transceivers
  5V Relay


How it works:
The RPi is setup with a wireless hotspot. It also hosts a local website which is password protected,
which serves as an interface with the 'registered devices' database stored locally. Through the use
of the website, the admin can add or remove devices using their MAC address, thus allowing or preventing
them to open the gate.
When a user connects to the wireless hotspot, the RPi retrieves the device's MAC address, and compares
it to the local database. If the MAC address is not present, the device will be ignored. If it is in
fact present, the RPi will use the connected NRF24L01 transceiver to send a specific code, which will
be received by the same type transceiver connected to the Arduino Nano. The Arduino confirms that the
correct value has been received, and briefly powers the relay, which is connected to the gate motor,
to open the gate. After a set time passes, the relay is powered once more to close the gate.

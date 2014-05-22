CCPIRDoor
=========

This program requires the [ComputerCraft](http://www.computercraft.info/) mod for [Minecraft](https://minecraft.net/).

These programs work to together to make a door open in minecraft when a PIR (Passive Infra Red) sensor is triggered.
The PIR sensor connects to the [Raspberry Pi](http://www.raspberrypi.org/) as follows:

```
PIR  |  PI

GND -> GND
VCC -> 5 volts
OUT -> 17
```

The python file runs on the Raspberry Pi. You will have to run it as root: `sudo python PIR.py`

The other file goes on the computer in Minecraft. You can either move it into the proper directory in your Minecraft saves folder. The command line parameters for the startup program are: `startup [raspberry pi url] [side] [delay]`. The raspberry pi url has to have `http://` at the beginning and the port `:3141` at the end. Delay is how long to wait between polls. It is recommended to have at least a one second delay. The default values are `http://raspberrypi.local:3141`, `back` and `1`.

This program is not just limited to PIR sensors and doors. It could be expanded to control nearly any element in Minecraft using a variety of sensors connected to the Raspberry Pi.

[Blog post](http://codinghobbit.no-ip.org/blog/?p=21)
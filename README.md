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

The other file goes on the computer in Minecraft. You can either move it into the proper directory in your Minecraft saves folder, or you can run this command on the computer within Minecraft: `pastebin get n8Vh3Mv2` The command line parameters for the PIR program are: `PIR [raspberry pi url] [delay]`. The raspberry pi url has to have "http://" at the beginning and the port ":3141" at the end. Delay is how long to wait between polls. It is recommended to have at least a one second delay. The default values are `http://raspberrypi.local` and `1`.

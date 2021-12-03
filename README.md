# PS4_HC05
Provides connectivity to Arduino control boards via HC-05 bluetooth board through a controller.  <br />

## Components and Specs

### Required Parts
PS4 or Xbox controller (pretty sure the XBOX script will work with a logitech controller I just am not able to test it) <br />
MicroUSB connection to controller <br />
Laptop (Current version is not OS specific, but will require you to change the ) <br />

## Connecting
The [Playstation Class] assumes that you only have one controller plugged in at a time, but should be able to handle input from two different controllers if you so wish. <br />
Since HC-05 can only handle single byte communication the script sends chars as input <br />
### Connecting to HC-05 on windows
To be Completed <br />

### Connecting to HC-05 on Mac
Plug in PS4 controller prior to running script
#### Directions
DO NOT ```cat -v /dev/YourChip``` as some tutorials reccomend. <br />
Instead connect to your chip through System Preferences. <br />
If you have not changed the name of your chip it should be tty.HC-05-SerialPort and you will not have to change it. <br />
If you HAVE changed the name the line simply edit ```FILE_PATH```  <br />
Run this script ~relativelyyyyy~ soon after you connect, otherwise you will disconnect automatically.<br />
I have the current controls formatted with [my code](https://github.com/kevinMaynard20/WCRL_2021), so you will have to change the char you are sending if you don't want to just copy mine. 

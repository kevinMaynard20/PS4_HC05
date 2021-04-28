# PS4_HC05
Allows PS4 controller to communicate with an HC05 bluetooth chip using serial.write().
# Directions
DO NOT ```cat -v /dev/YourChip``` as you would have previously done to connect to the HC05. \n
Instead connect to your chip through System Preferences. \n
If you have not changed the name of your chip it should be tty.HC-05-SerialPort and you will not have to change it. \n
Run this script ~relativelyyyyy~ soon after you connect, otherwise because of the way MacOS handles bluetooth you will auto disconnect.\n
I have the current controls formatted with [my code](https://github.com/kevinMaynard20/WCRL_2021), so you will have to change the char you are sending if you don't want to just copy mine. 

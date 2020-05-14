# lucka
Lucka is a smart lamp designed to turn itself on or off whenever it is dark or bright - in a smart way.

Such designs typically consist of a light sensor and some kind of logic that turns on and off a physical lamp. They often perform poorly in the sense that they turn on and off in error when values coming from the sensor are not perfect. Lucka aims at overcoming precisely that problem.
Lucka is programmed in Python, and it works on Raspberry Pi. It works by checking the light sensor plugged into a Raspberry Pi and makes the on/off decision based on the information it gets from the sensor. Lucka cannot be easily tricked into erroneously turning on or off by random light sources, such as bypassing cars, clouds.
To build Lucka you need: a Raspberry Pi with a power supply, SD card, LAN cable (optional), light sensor (basically a photoresistor and a capacitor), optocoupler module or a solid-state relay module, breadboard (optional) and breadboard wires. You can use Lucka for different purposes, for example, as a desk light, for controlling exterior lighting for your home or even serving as a “brain” for smart street lamps. 
Details about the hardware design of the light sensor can be found here: https://pimylifeup.com/raspberry-pi-light-sensor/.

To get the software, you can simply clone my GitHub repository and then clone a repository from which Lucka imports a function that reads data from the light sensor.
git clone https://github.com/DomenKorenini/lucka/
cd lucka
git clone https://github.com/pimylifeup/Light_Sensor/

I’ll be working on Lucka and try to teach it even more tricks, so stay in touch. It is always work in progress :)

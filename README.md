# IOT-Pi3-Alexa-Automation

Use Raspberry Pi 3 as home automation device with Alexa. This project allows you to control multiple devices connected to Raspberry Pi 3 with voice command. You are able to control GPIO pins thus control GPIO connected devices.

Ported from original repos for python 3
https://github.com/toddmedema/echo
https://github.com/xtacocorex/CHIP_IO 

## Instructions:
1. Launch Pi ssh session with putty or localy through VNC and type following two commands Pi command prompt to update it. "sudo apt-get update" and "sudo apt-get upgrade" (This will take a while)
1. Download this github project as zip file with following command
  "wget https://github.com/nassiramalik/IOT-Pi3-Alexa-Automation/archive/master.zip"
1. Unzip downloaded zip file with "unzip master.zip" command and type "cd IOT-Pi3-Alexa-Automation-master" command after unzip completes
1. (Optional) Entery "sudo pip install virtualenv" command to install virtualenv on Pi
1. (Optional) Enter "virtualenv ipaa-env" command to create virtual environment for your project
1. (Optional) Enter ". ipaa-env/bin/activate" command to activate your project's virtualen vironment
1. Enter "sudo python3 RPi_name_port_gpio.py" command to run Pi IOT program
1. Give voice command to Alex to discover devices "Alexa discover devices" it will search your network and discover your Raspberry Pi 3 as an IOT device.
1. Give a voice command to Alexa "Turn on the office" you should hear a relay clicking sound and led turn on
1. Give a voice command to Alexa "Turn off the office" you should hear a relay clicking sound and led should turn off

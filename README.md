# Raspberry Pi AWS IoT PWM Controller

AWS IoT connected relay automation for Raspberry Pi

## Installation

### Install the OS:

- Open Raspberry Pi Imager
- Select OS Lite & burn
- Eject & reinsert SD card
- Write empty file called `ssh` to the root of the `boot` partition.
- Write a text file called `wpa_supplicant.conf` with:

    ```
    country=US
    ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
    network={
      ssid="YOUR_NETWORK_NAME"
      psk="YOUR_PASSWORD"
      key_mgmt=WPA-PSK
    }
    ```

### Set up the PWM hat

- `ssh pi@raspberrypi.local`
- `sudo raspi-config` > Interfaces > Enable I2C

# Docker

## Build & Push the Docker Image

- `> docker build -t connollyst/rpi-aws-iot-pwm .`
- `> docker push connollyst/rpi-aws-iot-pwm`

## Install Docker on Raspberry Pi

- `> sudo apt-get update && sudo apt-get upgrade && sudo reboot`
- `> curl -fsSL https://get.docker.com -o get-docker.sh && sudo sh get-docker.sh`

## Pull the Docker Image

- `> sudo docker pull connollyst/rpi-aws-iot-pwm:latest`
- `> sudo docker run --privileged connollyst/rpi-aws-iot-pwm`
- `> sudo docker run --device /dev/gpiomem connollyst/rpi-aws-iot-relay`
- `> sudo docker run --device /dev/i2c-0 --device /dev/i2c-1 connollyst/rpi-aws-iot-relay`
  - Doesn't work: `"/dev/i2c-0": no such file or directory`
  - Try I2C detection instead?

# Troubleshooting

```
Traceback (most recent call last):
  File "main.py", line 10, in <module>
    pwm = PCA9685(0x40, debug=False)
  File "/home/pi/PCA9685.py", line 29, in __init__
    self.bus = smbus.SMBus(1)
IOError: [Errno 2] No such file or directory
```
`sudo raspi-config` > Interfaces > Enable I2C

TODO: Catch this IO error and give better feedback. 

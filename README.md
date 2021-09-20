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

## Install Docker on Raspberry Pi

- `> sudo apt-get update && sudo apt-get upgrade && sudo reboot`
- `> curl -sSL https://get.docker.com | sh`
- `> sudo groupadd docker`
- `> sudo usermod -aG docker ${USER}`

## Build & Push the Docker Image

- `> docker build -t connollyst/rpi-aws-iot-pwm . &&  docker run connollyst/rpi-aws-iot-pwm`
- `> docker build -t connollyst/rpi-aws-iot-pwm . &&  docker push connollyst/rpi-aws-iot-pwm`

- `> docker build -t connollyst/rpi-aws-iot-pwm:latest -t connollyst/rpi-aws-iot-pwm:v1.2.3 .`
- `> docker push connollyst/rpi-aws-iot-pwm:latest && docker push connollyst/rpi-aws-iot-pwm:v1.2.3`

## Pull the Docker Image

- `> docker pull connollyst/rpi-aws-iot-pwm:latest`
- `> docker run --restart=on-failure --privileged connollyst/rpi-aws-iot-pwm:v1.2.3 &`
- `> docker run --device /dev/gpiomem connollyst/rpi-aws-iot-pwm`
- `> docker run --device /dev/i2c-0 --device /dev/i2c-1 connollyst/rpi-aws-iot-pwm`
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

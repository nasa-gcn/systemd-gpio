# systemd-gpio

Use systemd to configure commands to run when a GPIO button is pressed on a Raspberry Pi.

This project is inspired by https://github.com/ali1234/systemd-gpio. The main difference is that we are using [gpiozero](https://github.com/gpiozero/gpiozero) rather than [WiringPi](https://web.archive.org/web/20220405225008/http://wiringpi.com/wiringpi-deprecated/), because WiringPi is no longer maintained.

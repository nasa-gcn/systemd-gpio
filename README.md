# systemd-gpio

Use systemd to configure commands to run when a GPIO button is pressed on a Raspberry Pi.

This project is inspired by https://github.com/ali1234/systemd-gpio. The main difference is that we are using [gpiozero](https://github.com/gpiozero/gpiozero) rather than [WiringPi](https://web.archive.org/web/20220405225008/http://wiringpi.com/wiringpi-deprecated/), because WiringPi is no longer maintained.

## Usage

To configure a GPIO pin, create a file called <code>/etc/gpio/<i>N</i></code>, where <code><i>N</i></code> is an integer pin number following [gpiozero's convention](https://gpiozero.readthedocs.io/en/latest/recipes.html#pin-numbering). For example, to configure actions for pin GPIO23, create the file `/etc/gpio/23`.

The file should use the [systemd EnvironmentFile syntax](https://www.freedesktop.org/software/systemd/man/latest/systemd.exec.html#EnvironmentFile=). All variables are optional.

The values for `GPIO_PULL_UP`, `GPIO_ACTIVE_STATE`, `GPIO_BOUNCE_TIME`, `GPIO_HOLD_TIME`, and `GPIO_HOLD_REPEAT` are passed to the Python [`gpiozero.Button`](https://gpiozero.readthedocs.io/en/latest/api_input.html#gpiozero.Button) class.

The values of `GPIO_WHEN_HELD`, `GPIO_WHEN_PRESSED`, and `GPIO_WHEN_RELEASED` control the commands to be executed when the button is held, pressed, or released, respectively. See the corresponding methods [`gpiozero.Button.when_held`](https://gpiozero.readthedocs.io/en/latest/api_input.html#gpiozero.Button.when_held), [`gpiozero.Button.when_pressed`](https://gpiozero.readthedocs.io/en/latest/api_input.html#gpiozero.Button.when_pressed), and [`gpiozero.Button.when_released`](https://gpiozero.readthedocs.io/en/latest/api_input.html#gpiozero.Button.when_released), respectively.

Once you have populated the configuration file, activate the button by running the following command, replacing <code><i>N</i></code> with the pin number:

<pre>sudo systemctl enable --now gpio@<i>N</i>.service</pre>

## Examples

```
# /etc/gpio/23
GPIO_HOLD_TIME=5
GPIO_WHEN_PRESSED="wall 'Hold the power button for 5 seconds to power off.'"
GPIO_WHEN_HELD=poweroff
```

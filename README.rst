SYSTEMD-GPIO(5)
===============

NAME
----
systemd-gpio - run commands when a button on a GPIO pin is pressed

DESCRIPTION
-----------

Use systemd to configure commands to run when a button attached to a GPIO pin is pressed, released, or held.

To configure a GPIO pin, create a file called /etc/gpio/*N*, where *N* is an integer pin number following the `gpiozero pin numbering`_ convention. Once you have populated the configuration file, activate the button by running the following command, replacing *N* with the pin number::

    sudo systemctl enable --now gpio@N.service

ENVIRONMENT
-----------

| GPIO_PULL_UP
| GPIO_ACTIVE_STATE
| GPIO_BOUNCE_TIME
| GPIO_HOLD_TIME
| GPIO_HOLD_REPEAT

    Button behavior. See the documentation for the corresponding constructor arguments of `gpiozero.Button`_.

| GPIO_WHEN_HELD
| GPIO_WHEN_PRESSED
| GPIO_WHEN_RELEASED

    Commands to run when the button is held, pressed, or released, respectively.  See the documentation for the corresponding properties of `gpiozero.Button`_.

FILES
-----

/etc/gpio/*N*

    Configuration file for GPIO pin *N*, where *N* corresponds to the `gpiozero pin numbering`_. The file should be in the `systemd EnvironmentFile syntax`_ and may define any of the environment variables listed above.

HISTORY
-------

This project is inspired by https://github.com/ali1234/systemd-gpio. The main difference is that we are using gpiozero_ rather than WiringPi_, because WiringPi is no longer maintained.

EXAMPLES
--------

The following example configures GPIO 23 so that when it is pressed, it prints a message to all TTYs, and when held, shuts down the machine::

    # /etc/gpio/23
    GPIO_HOLD_TIME=5
    GPIO_WHEN_PRESSED="wall 'Hold the power button for 5 seconds to power off.'"
    GPIO_WHEN_HELD=poweroff

To activate the pin, run the following command::

    sudo systemctl enable --now gpio@23.service

.. _gpiozero: https://github.com/gpiozero/gpiozero
.. _WiringPi: https://web.archive.org/web/20220405225008/http://wiringpi.com/wiringpi-deprecated/
.. _`gpiozero.Button`: https://gpiozero.readthedocs.io/en/latest/api_input.html#gpiozero.Button
.. _`gpiozero pin numbering`: https://gpiozero.readthedocs.io/en/latest/recipes.html#pin-numbering
.. _`systemd EnvironmentFile syntax`: https://www.freedesktop.org/software/systemd/man/latest/systemd.exec.html#EnvironmentFile=

SEE ALSO
--------

systemctl(1), systemd.exec(5)

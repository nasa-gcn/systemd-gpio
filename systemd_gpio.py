import click
import gpiozero

import functools
import os
import shlex
import signal


@click.command(context_settings=dict(auto_envvar_prefix="GPIO"))
@click.option("--pin", type=int, required=True)
@click.option("--pull-up", type=bool, default=True)
@click.option("--active-state", type=bool)
@click.option("--bounce-time", type=float)
@click.option("--hold-time", type=float, default=1)
@click.option("--hold-repeat", type=bool, default=False)
@click.option("--when-held", type=str)
@click.option("--when-pressed", type=str)
@click.option("--when-released", type=str)
def main(**kwargs):
    """Run commands when a button on GPIO%i is pressed, released, or held.

    Any of the options may be provided using either a command line argument or
    an environment variable whose name starts with the prefix GPIO_. For
    example, the command-line argument --pull-up is equivalent to the
    environment variable GPIO_PULL_UP=1.

    The values for the options --pin, --pull-up, --active-state, --bounce-time,
    --hold-time, and --hold-repeat are passed to gpio.Button (see
    https://gpiozero.readthedocs.io/en/latest/api_input.html#gpiozero.Button).

    The values for the options --when-held, --when-pressed, and --when-released
    control the commands to be run when the button is held, pressed, or
    released, respectively.
    """
    keys = ["when_held", "when_pressed", "when_released"]
    handlers = {key: kwargs.pop(key) for key in keys}
    button = gpiozero.Button(**kwargs)
    for key, command in handlers.items():
        if command and (args := shlex.split(command)):
            handler = functools.partial(os.spawnvp, os.P_NOWAIT, args[0], args)
            setattr(button, key, handler)
    signal.pause()


if __name__ == "__main__":
    main()

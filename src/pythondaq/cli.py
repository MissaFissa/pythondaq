import click
from pythondaq.diode_experiment import list_resources
from pythondaq.diode_experiment import DiodeExperiment

@click.group()
def diode():
    """Make a group of commands using the @click.group() decorator.
    """
    pass

@diode.command()
@click.argument("start")
@click.argument("stop")
@click.option(
    "-filename",
    "--output FILENAME",
    default = 1,
)
def list():

    print('Work in progress, list devices')

@diode.command()
def scan():

    print('Work in progress, scan LED')  

if __name__ == "__main__":

    diode()
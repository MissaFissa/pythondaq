import click
import csv
from pythondaq.diode_experiment import list_resources
from pythondaq.diode_experiment import DiodeExperiment

@click.group()
def diode():
    """Make a group of commands using the @click.group() decorator.
    """
    pass

@diode.command()
def list():

    print(list_resources())

@diode.command()
@click.argument("device")
def info(device):

    
    print(device.query("*IDN?"))

@diode.command()
@click.argument("start")
@click.argument("stop")
@click.option("-r", "--repeats", default = 1)
@click.option("-o", "--output", default = "")
def scan(start, stop, repeats, output):

    experiment = DiodeExperiment()

    start_DAC = int(float(start) * (1023 / 3.3))
    stop_DAC = int(float(stop) * (1023 / 3.3))

    voltages_LED, currents_LED = experiment.scan(start = start_DAC, stop = stop_DAC, iterations = repeats)[4:6]


    if output != "":

        with open(f'{output}.csv', 'w', newline = '') as csvfile:

            writer = csv.writer(csvfile)
            header = ['Voltages LED', 'Currents LED']
            writer.writerow(header)
            
            for voltages_LED, currents_LED in zip(voltages_LED[0], currents_LED[0]):

                writer.writerow([voltages_LED, currents_LED])

if __name__ == "__main__":

    diode()
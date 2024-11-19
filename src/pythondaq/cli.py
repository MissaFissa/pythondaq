"""Command line interface for the experiment.
"""
import click
import matplotlib.pyplot as plt
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
    """Print list of connected devices.
    """
    print(list_resources())

@diode.command()
@click.argument("device")
def info(device):
    """Print identification string of device.\n
    DEVICE: portname of device.
    """
    experiment = DiodeExperiment(device)
    print(experiment.get_identification())

@diode.command()
@click.argument("device")
@click.argument("start")
@click.argument("stop")
@click.option("-r", "--repeats", default = 1, help = "Select the amount of repetitions of the experiment.")
@click.option("-o", "--output", default = "", help = "Choose name of CSV file if wanted, otherwise just ignore it.")
@click.option("--graph/--no-graph", default = False, help = "Choose whether or not to show a graph.")
def scan(start, stop, repeats, output, device, graph):
    """Initiate experiment.\n
    DEVICE: portname of device, START: minimum value of the voltage range, STOP: maximum value of the voltage range.
    """
    experiment = DiodeExperiment(device)

    start_DAC = int(float(start) * (1023 / 3.3))
    stop_DAC = int(float(stop) * (1023 / 3.3))

    errors_voltages, errors_currents, means_voltages, means_currents, voltages_LED, currents_LED = experiment.scan(start = start_DAC, stop = stop_DAC, iterations = repeats)

    if output != "":

        with open(f'{output}.csv', 'w', newline = '') as csvfile:

            writer = csv.writer(csvfile)
            header = ['Mean voltages LED', 'Mean currents LED', 'Errors voltages', 'Errors currents']
            writer.writerow(header)

            for mean_voltage_LED, mean_current_LED, errors_voltages, errors_currents in zip(means_voltages, means_currents, errors_voltages, errors_currents):

                writer.writerow([mean_voltage_LED, mean_current_LED, errors_voltages, errors_currents])

    if graph:

        plt.figure(figsize = (10, 8))

        plt.errorbar(means_voltages, means_currents, xerr = errors_voltages, yerr = errors_currents, fmt = 'bo', markersize = 1.25, elinewidth = 0.5, capsize = 1, ecolor = 'r')
        plt.xticks(rotation = 'vertical')
        plt.xlabel('Mean voltages LED [V]')
        plt.ylabel('Mean currents LED [A]')
        plt.tight_layout()

        plt.show()

if __name__ == "__main__":

    diode()
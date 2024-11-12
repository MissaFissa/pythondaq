"""Plot the data from the experiment and create a csv file using the data. 
"""
import matplotlib.pyplot as plt
import csv
from pythondaq.diode_experiment import list_resources
from pythondaq.diode_experiment import DiodeExperiment

def initiate_experiment():
    
    experiment = DiodeExperiment()

    errors_voltages, errors_currents, means_voltages, means_currents = experiment.scan(start = 0, stop = 1023, iterations = 2)

    csv_file = create_csv_file(means_voltages, means_currents)

    fig = plt.figure(figsize = (10, 8))

    plt.errorbar(means_voltages, means_currents, xerr = errors_voltages, yerr = errors_currents, fmt = 'bo', markersize = 1.25, elinewidth = 0.5, capsize = 1, ecolor = 'r')
    plt.xticks(rotation = 'vertical')
    plt.xlabel('Voltage LED [V]')
    plt.ylabel('Current LED [A]')
    plt.tight_layout()

    plt.show()

def create_csv_file(means_voltages, means_currents):
    """Create a csv file containing the means of the voltages and the means of the currents.
    """
    with open('metingen.csv', 'w', newline = '') as csvfile:

        writer = csv.writer(csvfile)
        header = ['mean Voltages LED', 'mean Currents LED']
        writer.writerow(header)

        for mean_voltage_LED, mean_current_LED in zip(means_voltages, means_currents):

            writer.writerow([mean_voltage_LED, mean_current_LED])
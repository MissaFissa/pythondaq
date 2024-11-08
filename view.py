import matplotlib.pyplot as plt
from diode_experiment import list_resources
from diode_experiment import DiodeExperiment

experiment = DiodeExperiment()

voltages_LED, currents_LED, std_voltages, std_currents, mean_voltages, mean_currents = experiment.scan(start = 0, stop = 1023, iterations = 2)
csv_file = experiment.csv_file()

print(mean_voltages[0:10])

fig1 = plt.figure(figsize = (10, 8))

plt.errorbar(mean_voltages, mean_currents, xerr = std_voltages, yerr = std_currents, fmt = 'bo', markersize = 1.5, elinewidth = 0.5, ecolor = 'g')
plt.xticks(rotation = 'vertical')
plt.xlabel('Voltages LED [V]')
plt.ylabel('Currents LED [A]')
plt.tight_layout()

plt.show()
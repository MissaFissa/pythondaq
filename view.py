import matplotlib.pyplot as plt
from diode_experiment import list_resources
from diode_experiment import DiodeExperiment

experiment = DiodeExperiment()

voltages_LED, currents_LED, std_voltages, std_currents, mean_voltages, mean_currents = experiment.scan(start = 0, stop = 1023, iterations = 5)

fig = plt.figure(figsize = (10, 8))

plt.errorbar(mean_voltages, mean_currents, std_voltages, std_currents)

plt.xticks(rotation = 'vertical')
plt.xlabel('Voltages LED [V]')
plt.ylabel('Currents LED [A]')
plt.tight_layout()

plt.show()
import matplotlib.pyplot as plt
from diode_experiment import list_resources
from diode_experiment import DiodeExperiment

experiment = DiodeExperiment()

voltages_LED, currents_LED = experiment.scan(start = 0, stop = 1023)

fig = plt.figure(figsize = (10, 8))

plt.plot(voltages_LED, currents_LED)

plt.xticks(rotation = 'vertical')
plt.xlabel('Voltages LED [V]')
plt.ylabel('Currents LED [A]')
plt.tight_layout()

plt.show()
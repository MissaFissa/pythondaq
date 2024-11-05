import pyvisa
import time as t
import matplotlib.pyplot as plt
import csv

resistance_resistor = 220
raw_volt_values = [raw_volt_value for raw_volt_value in range(0, 1024)]

rm = pyvisa.ResourceManager("@py")
ports = rm.list_resources()

device = rm.open_resource(
    "ASRL9::INSTR", read_termination="\r\n", write_termination="\n"
)
identification = device.query("*IDN?")

voltages_resistor = []
voltages_LED = []
currents_LED = []

def raw_value_to_voltage(raw_value):

    return raw_value / (1024 / 3.3)

for raw_volt_value in raw_volt_values:

    device.query("OUT:CH0 "+str(raw_volt_value)+"")
    voltage = device.query("OUT:CH0?")
    voltage_resistor = raw_value_to_voltage(int(device.query("MEAS:CH2?")))
    voltage_LED = raw_value_to_voltage(int(device.query("MEAS:CH1?"))) - voltage_resistor
    voltages_resistor.append(voltage_resistor)
    voltages_LED.append(voltage_LED)
    current_LED = voltage_resistor / resistance_resistor
    currents_LED.append(current_LED)

fig = plt.figure(figsize = (12, 8))

plt.plot(voltages_LED, currents_LED)

plt.xticks(rotation = 'vertical')
plt.xlabel('Voltages LED (V)')
plt.ylabel('Currents LED (A)')
# plt.locator_params(axis = 'x', nbins = 4)
# plt.locator_params(axis = 'y', nbins = 4)

# plt.close(fig)

plt.show()


with open('pythondaq/metingen.csv', 'w', newline = '') as csvfile:

    writer = csv.writer(csvfile)
    writer.writerows(zip(voltages_LED, currents_LED))

import csv
import numpy as np
from arduino_device import ArduinoVISADevice, list_resources

class DiodeExperiment:

    def __init__(self):

        self.device = ArduinoVISADevice(port = "ASRL9::INSTR")
        self.resistance_resistor = 220
        self.voltages_resistor = []
        self.voltages_LED = []
        self.currents_LED = []
        self.voltages_LED_repeats = []
        self.currents_LED_repeats = []
        self.standard_deviations_voltages = []
        self.standard_deviations_currents = []
        self.means_voltages = []
        self.means_currents = []

    def scan(self, start, stop, iterations):

        raw_values = [raw_value for raw_value in range(start, stop + 1)]

        for _ in range(iterations):

            for raw_value in raw_values:

                self.device.set_output_value(value = raw_value)
                voltage_resistor = self.device.get_input_voltage(channel = 2)
                voltage_LED = self.device.get_input_voltage(channel = 1) - voltage_resistor
                self.voltages_resistor.append(voltage_resistor)
                self.voltages_LED.append(voltage_LED)
                current_LED = voltage_resistor / self.resistance_resistor
                self.currents_LED.append(current_LED)
            
            self.voltages_LED_repeats.append(self.voltages_LED)
            self.currents_LED_repeats.append(self.currents_LED)

        self.standard_deviations_voltages = np.std((np.array(self.voltages_LED_repeats)), axis = 0)
        self.standard_deviations_currents = np.std((np.array(self.currents_LED_repeats)), axis = 0)
        self.means_voltages = np.mean((np.array(self.voltages_LED_repeats)), axis = 0)
        self.means_currents = np.mean((np.array(self.currents_LED_repeats)), axis = 0)

        return self.voltages_LED, self.currents_LED, self.standard_deviations_voltages, self.standard_deviations_currents, self.means_voltages, self.means_currents

# with open('pythondaq/metingen.csv', 'w', newline = '') as csvfile:

#     writer = csv.writer(csvfile)
#     header = ['Voltages LED', 'Currents LED']
#     writer.writerow(header)

#     for voltage_LED, current_LED in zip(voltages_LED, currents_LED):

#         writer.writerow([voltage_LED, current_LED])
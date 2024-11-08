import csv
import numpy as np
from arduino_device import ArduinoVISADevice, list_resources

class DiodeExperiment:

    def __init__(self):

        self.device = ArduinoVISADevice(port = "ASRL9::INSTR")
        self.resistance_resistor = 220
        self.voltages_LED_repeats = []
        self.currents_LED_repeats = []
        self.standard_deviations_voltages = []
        self.standard_deviations_currents = []
        self.means_voltages = []
        self.means_currents = []

    def scan(self, start, stop, iterations):

        raw_values = [raw_value for raw_value in range(start, stop + 1)]

        for _ in range(iterations):

            voltages_resistor = []
            voltages_LED = []
            currents_LED = []

            for raw_value in raw_values:

                self.device.set_output_value(value = raw_value)
                voltage_resistor = self.device.get_input_voltage(channel = 2)
                voltage_LED = self.device.get_input_voltage(channel = 1) - voltage_resistor
                voltages_resistor.append(voltage_resistor)
                voltages_LED.append(voltage_LED)
                current_LED = voltage_resistor / self.resistance_resistor
                currents_LED.append(current_LED)
            
            self.voltages_LED_repeats.append(voltages_LED)
            self.currents_LED_repeats.append(currents_LED)

        self.standard_deviations_voltages = np.std((np.array(self.voltages_LED_repeats)), axis = 0) / np.sqrt(iterations)
        self.standard_deviations_currents = np.std((np.array(self.currents_LED_repeats)), axis = 0) / np.sqrt(iterations)
        self.means_voltages = np.mean((np.array(self.voltages_LED_repeats)), axis = 0)
        self.means_currents = np.mean((np.array(self.currents_LED_repeats)), axis = 0)

        return voltages_LED, currents_LED, self.standard_deviations_voltages, self.standard_deviations_currents, self.means_voltages, self.means_currents

    def csv_file(self):

        with open('pythondaq/metingen.csv', 'w', newline = '') as csvfile:

            writer = csv.writer(csvfile)
            header = ['mean Voltages LED', 'mean Currents LED']
            writer.writerow(header)

            for mean_voltage_LED, mean_current_LED in zip(self.means_voltages, self.means_currents):

                writer.writerow([mean_voltage_LED, mean_current_LED])
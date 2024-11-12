import numpy as np
from pythondaq.arduino_device import ArduinoVISADevice, list_resources

class DiodeExperiment:
    """Initiate the experiment.
    """
    def __init__(self):
        """Initialize variables used in the class.
        """
        self.device = ArduinoVISADevice(port = "ASRL9::INSTR")
        self.resistance_resistor = 220
        self.voltages_LED_repeats = []
        self.currents_LED_repeats = []
        self.errors_voltages = []
        self.errors_currents = []
        self.means_voltages = []
        self.means_currents = []

    def scan(self, start, stop, iterations):
        """Starts a measurement.

        Args:
            start (int): minimum value of the input channel.
            stop (int): maximum value of the input channel.
            iterations (int): how many times to repeat the experiment.

        Returns:
            list: list containing the errors on the voltages.
            list: list containing the errors on the currents.
            list: list containing the means of the voltages.
            list: list containing the means of the currents.
        """
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

        self.errors_voltages = np.std((np.array(self.voltages_LED_repeats)), axis = 0) / np.sqrt(iterations)
        self.errors_currents = np.std((np.array(self.currents_LED_repeats)), axis = 0) / np.sqrt(iterations)
        self.means_voltages = np.mean((np.array(self.voltages_LED_repeats)), axis = 0)
        self.means_currents = np.mean((np.array(self.currents_LED_repeats)), axis = 0)

        return self.errors_voltages, self.errors_currents, self.means_voltages, self.means_currents
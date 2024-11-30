import time, threading
import numpy as np
from pythondaq.arduino_device import ArduinoVISADevice, list_resources

class DiodeExperiment:
    """Initiate the experiment.
    """
    def __init__(self, port):
        """Initialize variables used in the class.
        """
        self.device = ArduinoVISADevice(port = port)
        self.resistance_resistor = 220
        self.errors_voltages = []
        self.errors_currents = []
        self.means_voltages = []
        self.means_currents = []

    def get_identification(self):
        """return identification string of connected device.

        Returns:
            str: identification string of connected device.
        """
        return self.device.get_identification()

    def close(self):

        self.device.close()

    def start_scan(self, start, stop, iterations):
        """Start a new thread to execute a scan.
        """
        is_scanning = threading.Event()

        if is_scanning.is_set() == False:

            self._scan_thread = threading.Thread(
                target = self.scan, args = (start, stop, iterations)
            )
            self._scan_thread.start()
            is_scanning.set()
            # # time.sleep(3)
            # is_scanning.clear()

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
        self.errors_voltages = []
        self.errors_currents = []
        self.means_voltages = []
        self.means_currents = []

        for raw_value in raw_values:

            voltages_resistor = []
            voltages_LED = []
            currents_LED = []

            for _ in range(iterations):

                self.device.set_output_value(value = raw_value)
                voltage_resistor = self.device.get_input_voltage(channel = 2)
                voltage_LED = self.device.get_input_voltage(channel = 1) - voltage_resistor
                voltages_resistor.append(voltage_resistor)
                voltages_LED.append(voltage_LED)
                current_LED = voltage_resistor / self.resistance_resistor
                currents_LED.append(current_LED * 1000)
    
            self.errors_voltages.append(np.std((np.array(voltages_LED))) / np.sqrt(iterations))
            self.errors_currents.append(np.std((np.array(currents_LED))) / np.sqrt(iterations))
            self.means_voltages.append(np.mean((np.array(voltages_LED))))
            self.means_currents.append(np.mean((np.array(currents_LED))))
        
            time.sleep(0.01)
   
        self.device.set_output_value(value = 0)
        self.device.close()

        return self.errors_voltages, self.errors_currents, self.means_voltages, self.means_currents
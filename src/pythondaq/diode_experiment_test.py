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
        self.is_scanning = threading.Event()
        self.stop_scanning = threading.Event()
        self.resistance_resistor = 220
        self.errors_voltages = []
        self.errors_currents = []
        self.means_voltages = []
        self.means_currents = []
        self.counter = 0

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
        if  self.is_scanning.is_set():

            return

        self.is_scanning.set()
        self.stop_scanning.clear()
        self._scan_thread = threading.Thread(target = self.scan, args = (start, stop, iterations))
        self._scan_thread.start()
    
    def stop_scan(self):

        if not self.is_scanning.is_set():

            return

        self.stop_scanning.set()

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
        self.counter = 0
        
        try:
                
            for raw_value in raw_values:

                voltages_resistor = []
                voltages_LED = []
                currents_LED = []

                if self.stop_scanning.is_set():

                    break
                
                for _ in range(iterations):

                    self.device.set_output_value(value = raw_value)
                    voltage_resistor = self.device.get_input_voltage(channel = 2)
                    voltage_LED = self.device.get_input_voltage(channel = 1) - voltage_resistor
                    voltages_resistor.append(voltage_resistor)
                    voltages_LED.append(voltage_LED)
                    current_LED = voltage_resistor / self.resistance_resistor
                    currents_LED.append(current_LED * 1000)
                    self.counter += 1
        
                self.errors_voltages.append(np.std((np.array(voltages_LED))) / np.sqrt(iterations))
                self.errors_currents.append(np.std((np.array(currents_LED))) / np.sqrt(iterations))
                self.means_voltages.append(np.mean((np.array(voltages_LED))))
                self.means_currents.append(np.mean((np.array(currents_LED))))
            
                time.sleep(0.01)

        finally:

            self.is_scanning.clear()
            self.device.set_output_value(value = 0)
            self.device.close()
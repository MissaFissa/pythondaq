# import pyvisa
try:
    from nsp2visasim import sim_pyvisa as pyvisa
except ModuleNotFoundError:
    import pyvisa
def list_resources():
    """Get list of available ports.

    Returns:
        list: list of all availabe ports.
    """
    rm = pyvisa.ResourceManager("@py")

    return rm.list_resources()

class ArduinoVISADevice:
    """Communicate with Arduino.
    """
    def __init__(self, port):
        """Ask port from user.

        Args:
            port (str): used port.
        """
        rm = pyvisa.ResourceManager("@py")
        self.device = rm.open_resource(port, read_termination = "\r\n", write_termination = "\n")

    def get_identification(self):
        """return identification string of connected device.

        Returns:
            str: identification string of connected device.
        """
        return self.device.query("*IDN?")

    def set_output_value(self, value):
        """Set value on the output channel.

        Args:
            value (int): value for the output channel.
        """
        self.device.query("OUT:CH0 "+str(value)+"")

    def get_output_value(self):  
        """Get value of the output channel.

        Returns:
            str: value of the output channel.
        """
        return self.device.query("OUT:CH0?")

    def get_input_value(self, channel):
        """Get value of the input channel.

        Args:
            channel (int): channel used for the input.

        Returns:
            str: value of the input channel.
        """
        return self.device.query("MEAS:CH"+str(channel)+"?")

    def get_input_voltage(self, channel):
        """Get value of the input channel in Volt.

        Args:
            channel (int): channel used for the input.

        Returns:
            int: value of the input channel in Volt.
        """
        return int(self.device.query("MEAS:CH"+str(channel)+"?")) / (1024 / 3.3)

    def close(self):

            self.device.close
            # self._is_open = False
        
if __name__ == "__main__":
    help(ArduinoVISADevice)
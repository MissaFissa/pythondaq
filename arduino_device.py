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

        Returns:
            _type_: _description_
        """
        self.device.query("OUT:CH0 "+str(value)+"")

    def get_input_value(self, channel):
        """_summary_

        Args:
            channel (_type_): _description_

        Returns:
            _type_: _description_
        """
        return self.device.query("MEAS:CH"+str(channel)+"?")

    def get_input_voltage(self, channel):

        return int(self.device.query("MEAS:CH"+str(channel)+"?")) / (1024 / 3.3)

    def get_output_value(self):  

        return self.device.query("OUT:CH0?")

if __name__ == "__main__":
    help(ArduinoVISADevice)
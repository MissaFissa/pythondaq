import pyvisa

def list_resources():

    rm = pyvisa.ResourceManager("@py")

    return rm.list_resources()

class ArduinoVISADevice:

    def __init__(self, port):

        rm = pyvisa.ResourceManager("@py")
        self.device = rm.open_resource(port, read_termination = "\r\n", write_termination = "\n")

    def get_identification(self):

        return self.device.query("*IDN?")

    def set_output_value(self, value):

        return self.device.query("OUT:CH0 "+str(value)+"")

    def get_input_value(self, channel):

        return self.device.query("MEAS:CH"+str(channel)+"?")

    def get_input_voltage(self, channel):

        return int(self.device.query("MEAS:CH"+str(channel)+"?")) / (1024 / 3.3)

    def get_output_value(self):  

        return self.device.query("OUT:CH0?")
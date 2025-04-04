import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/krristudent/boson_flir_ws/install/boson_thermal_publisher'

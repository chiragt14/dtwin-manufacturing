# data_sync.py

from sensor_interface import get_sensor_data
from actuator_control import control_actuators

def sync_data():
    print("Synchronizing physical and virtual systems...")
    sensor_data = get_sensor_data()
    if sensor_data["temperature"] > 80:
        control_actuators("COOLING_ON")
    else:
        control_actuators("COOLING_OFF")

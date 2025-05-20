# src/main.py

import json
import time
from simulation import run_simulation
from sensor_interface import read_sensors
from actuator_control import control_actuators
from data_sync import sync_data

def load_config(config_file='config/settings.json'):
    with open(config_file, 'r') as f:
        config = json.load(f)
    return config

def main():
    print("Starting Digital Twin for Manufacturing Plant...")

    # Load configuration
    config = load_config()
    print(f"Configuration loaded: {config}")

    try:
        while True:
            # Step 1: Read sensor data (simulate or real)
            sensor_data = read_sensors()
            print(f"Sensor data: {sensor_data}")

            # Step 2: Run the plant simulation/model based on sensor data
            simulation_result = run_simulation(sensor_data)
            print(f"Simulation result: {simulation_result}")

            # Step 3: Control actuators based on simulation result
            control_actuators(simulation_result)

            # Step 4: Sync data between physical and digital twin (e.g., update dashboard or database)
            sync_data(sensor_data, simulation_result)

            # Sleep based on sync interval config
            time.sleep(config.get('sync_interval_sec', 5))

    except KeyboardInterrupt:
        print("\nDigital Twin stopped by user.")

if __name__ == "__main__":
    main()

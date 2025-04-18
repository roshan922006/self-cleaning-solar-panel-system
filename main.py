import time
from sensors import read_humidity, read_temperature
from misting import activate_misting
from fan_control import control_fan

def main():
    while True:
        # Read humidity and temperature
        humidity = read_humidity()
        temperature = read_temperature()

        print(f"Humidity: {humidity}%")
        print(f"Temperature: {temperature}°C")

        # Activate misting if humidity is sufficient and temperature is within range
        if humidity > 60 and temperature > 15:
            print("Sufficient humidity detected. Activating misting system...")
            activate_misting()

        # Control fan for increased airflow if needed
        if humidity < 30:
            print("Low humidity detected. Activating fans for airflow...")
            control_fan("ON")

        time.sleep(60)  # Check every 60 seconds

if __name__ == "__main__":
    main()

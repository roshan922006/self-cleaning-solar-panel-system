def control_fan(status):
    if status == "ON":
        print("Fan activated to increase airflow.")
        # Code to turn on the fan (e.g., GPIO pin control for Raspberry Pi)
        # gpio.output(fan_pin, gpio.HIGH)
    else:
        print("Fan deactivated.")
        # Code to turn off the fan
        # gpio.output(fan_pin, gpio.LOW)

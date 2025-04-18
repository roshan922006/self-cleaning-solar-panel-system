import random

# Simulate humidity and temperature readings (for testing purposes)
def read_humidity():
    return random.randint(40, 80)  # Random value between 40% and 80%

def read_temperature():
    return random.randint(15, 35)  # Random value between 15°C and 35°C

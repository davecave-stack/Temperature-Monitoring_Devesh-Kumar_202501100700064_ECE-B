import random
import time
min_limit = float(input("Enter minimum temperature limit: "))
max_limit = float(input("Enter maximum temperature limit: "))
print("\nTemperature Monitoring Started...\n")
while True:
    temperature = round(random.uniform(0, 100), 2)
    print("Current Temperature:", temperature, "°C")
    if temperature < min_limit:
        print("⚠️ Temperature is BELOW minimum limit!\n")
    elif temperature > max_limit:
        print("⚠️ Temperature is ABOVE maximum limit!\n")
    else:
        print("✅ Temperature is within safe range.\n")
    time.sleep(2)   
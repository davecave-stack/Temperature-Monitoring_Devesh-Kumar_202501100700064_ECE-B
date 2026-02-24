# Temperature-Monitoring_Devesh-Kumar_202501100700064_ECE-B


**Problem Statement**
Build a Python code to display messages according to the temperature received from an assumed IoT system.
Accept max and min limit temperature.
Generate random values for temperature at every 2 second interval.
Compare with the limits to display appropriate value.


**Approach**
Import required modules:
random → To generate random temperature values.
time → To create a 2-second delay between readings.
Accept input from user:
Minimum temperature limit.
Maximum temperature limit.
Generate random temperature values (e.g., between 0°C and 100°C).
Use conditional statements:
If temperature < minimum limit → Display Low Temperature Alert
If temperature > maximum limit → Display High Temperature Alert
Otherwise → Display Temperature within Safe Range
Repeat the process every 2 seconds to simulate real-time monitoring.


**SAMPLE OUTPUT** 
Enter minimum temperature limit: 25
Enter maximum temperature limit: 60

Temperature Monitoring Started...

Current Temperature: 93.37 °C
⚠️ Temperature is ABOVE maximum limit!

Current Temperature: 87.73 °C
⚠️ Temperature is ABOVE maximum limit!

Current Temperature: 99.76 °C
⚠️ Temperature is ABOVE maximum limit!

Current Temperature: 52.85 °C
✅ Temperature is within safe range.

Current Temperature: 47.32 °C
✅ Temperature is within safe range.

Current Temperature: 52.45 °C
✅ Temperature is within safe range.

Current Temperature: 23.99 °C
⚠️ Temperature is BELOW minimum limit!

Current Temperature: 4.24 °C
⚠️ Temperature is BELOW minimum limit!

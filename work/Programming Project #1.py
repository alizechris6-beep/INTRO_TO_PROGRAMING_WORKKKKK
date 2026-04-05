# Weather Severity Project

total_rain = 0.0
total_wind = 0.0
count = 0

# Sentinel-controlled loop
while True:
    data = input().strip()

    # Split input into parts
    parts = data.split()

    # First value is rain
    rain = float(parts[0])

    # Check sentinel
    if rain == -1.0:
        break

    # Second value is wind
    wind = float(parts[1])

    total_rain += rain
    total_wind += wind
    count += 1

# Calculate averages
avg_rain = total_rain / count
avg_wind = total_wind / count

# Calculate severity
severity = (avg_rain * 10) + avg_wind

# Output results
print(f"The average rain is {avg_rain:.1f} inches")
print(f"\nThe average wind is {avg_wind:.1f} mph")
print(f"\nThe weather severity for these {count} readings is:     {severity:.1f}")
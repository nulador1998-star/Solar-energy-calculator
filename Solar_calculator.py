# Solar Energy Calculator v4 (with CO2 impact)

print("\n==============================")
print("  SOLAR ENERGY + IMPACT CALCULATOR")
print("==============================\n")

# Inputs
panels = int(input("Number of solar panels: "))
panel_watt = float(input("Panel wattage (W): "))
battery_capacity = float(input("Battery capacity (kWh): "))
sunlight_hours = float(input("Sunlight hours per day: "))
efficiency = float(input("System efficiency (%): "))

# Convert values
efficiency = efficiency / 100
panel_kw = panel_watt / 1000

# Energy calculation
total_power_kw = panels * panel_kw
raw_energy = total_power_kw * sunlight_hours
usable_energy = raw_energy * efficiency

# CO2 calculation (important assumption)
# 1 kWh from diesel generator ≈ 0.7 kg CO2 (average estimate)
co2_per_kwh = 0.7
co2_saved = usable_energy * co2_per_kwh

# Output
print("\n---------- ENERGY RESULTS ----------")
print(f"Usable Energy: {usable_energy:.2f} kWh/day")

print("\n---------- ENVIRONMENTAL IMPACT ----------")
print(f"CO₂ Saved per Day: {co2_saved:.2f} kg")

print("\n---------- INTERPRETATION ----------")

if co2_saved > 10:
    print("🌍 High impact system — strong environmental benefit")
elif co2_saved > 3:
    print("🌱 Moderate impact — good for small communities")
else:
    print("⚡ Small system — scalable opportunity")

print("\nBuilt by Mamadu Bah | BNM Sustainable Energy")

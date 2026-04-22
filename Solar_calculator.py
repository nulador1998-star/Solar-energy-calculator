# Solar Energy Calculator v2

print("=== Solar Energy Calculator ===\n")

# User inputs
panels = int(input("Enter number of solar panels: "))
panel_watt = float(input("Enter wattage of each panel (W): "))
battery_capacity = float(input("Enter battery capacity (kWh): "))
sunlight_hours = float(input("Enter average sunlight hours per day: "))
efficiency = float(input("Enter system efficiency (%) e.g. 80: "))

# Convert efficiency to decimal
efficiency = efficiency / 100

# Convert panel watt to kW
panel_power_kw = panel_watt / 1000

# Energy calculation
daily_energy = panels * panel_power_kw * sunlight_hours * efficiency

# Output
print("\n--- Solar Energy Report ---")
print(f"Panels: {panels}")
print(f"Panel Wattage: {panel_watt} W")
print(f"System Efficiency: {efficiency*100:.0f}%")
print(f"Sunlight Hours: {sunlight_hours} hrs")

print(f"\nEstimated Daily Energy: {daily_energy:.2f} kWh")

# Battery comparison
if daily_energy > battery_capacity:
    print("⚡ Excess energy: Your system generates MORE than battery capacity.")
elif daily_energy < battery_capacity:
    print("⚠️ Deficit: Your system generates LESS than battery capacity.")
else:
    print("✅ Balanced system.")

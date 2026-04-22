# Solar Energy Calculator v3 (Professional Version)

print("\n==============================")
print("  SOLAR ENERGY CALCULATOR")
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

# Calculations
total_power_kw = panels * panel_kw
raw_energy = total_power_kw * sunlight_hours
usable_energy = raw_energy * efficiency

# Output
print("\n---------- RESULTS ----------")
print(f"Total Installed Power: {total_power_kw:.2f} kW")
print(f"Raw Daily Energy: {raw_energy:.2f} kWh")
print(f"Usable Energy (after losses): {usable_energy:.2f} kWh")

print("\n---------- ANALYSIS ----------")

if usable_energy > battery_capacity:
    excess = usable_energy - battery_capacity
    print(f"⚡ System OVER capacity by {excess:.2f} kWh")
    print("👉 You may need a larger battery or storage system.")
elif usable_energy < battery_capacity:
    deficit = battery_capacity - usable_energy
    print(f"⚠️ System UNDER capacity by {deficit:.2f} kWh")
    print("👉 Battery is underutilized or system is small.")
else:
    print("✅ Perfect balance between generation and storage.")

print("\n----------------------------")
print("Built by Mamadu Bah | BNM Sustainable Energy")
print("----------------------------\n")

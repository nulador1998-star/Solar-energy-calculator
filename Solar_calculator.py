# Solar Energy Calculator

panels = int(input("Enter number of solar panels: "))
battery_capacity = float(input("Enter battery capacity (kWh): "))
sunlight_hours = float(input("Enter average sunlight hours per day: "))

panel_power_kw = 0.3

daily_energy = panels * panel_power_kw * sunlight_hours

print("\n--- Solar Energy Report ---")
print(f"Total daily energy generation: {daily_energy:.2f} kWh")

if daily_energy > battery_capacity:
    print("Your system generates MORE energy than your battery can store.")
elif daily_energy < battery_capacity:
    print("Your system generates LESS energy than your battery capacity.")
else:
    print("Your system is perfectly balanced.")

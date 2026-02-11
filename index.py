import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("hvac_data.csv")



df["timestamp"] = pd.to_datetime(df["timestamp"])
df.set_index("timestamp", inplace=True)

df["delta_T"] = df["indoor_temp"] - df["outdoor_temp"]

df["cooling_load_BTU"] = 1.08 * df["airflow_CFM"] * df["delta_T"]

print("Average Power Consumption:", df["power_kW"].mean())
print("Max Power Consumption:", df["power_kW"].max())
print("Correlation (Outdoor Temp vs Power):",
      df["outdoor_temp"].corr(df["power_kW"]))

plt.figure(figsize=(8,5))
plt.plot(df.index, df["power_kW"], marker="o")
plt.title("HVAC Power Consumption Over Time")
plt.xlabel("Time")
plt.ylabel("Power (kW)")
plt.grid(True)
plt.savefig("hvac_power_time.png")
plt.show()

plt.figure(figsize=(8,5))
plt.scatter(df["outdoor_temp"], df["power_kW"])
plt.title("Outdoor Temperature vs Power Consumption")
plt.xlabel("Outdoor Temperature (°C)")
plt.ylabel("Power (kW)")
plt.grid(True)
plt.savefig("temp_vs_power.png")
plt.show()
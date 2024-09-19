import numpy as np
import matplotlib.pyplot as plt rainfall_data = {
'City X': np.array([100, 120, 85, 90, 110, 95]), 'City Y': np.array([80, 75, 60, 95, 85, 90]),
'City Z': np.array([150, 140, 135, 160, 155, 170])
}
for city, data in rainfall_data.items():
total_rainfall = np.sum(data)
average_rainfall = np.mean(data)
print(f"{city}: Total Rainfall = {total_rainfall} mm, Average Monthly Rainfall =
{average_rainfall:.2f} mm")
def monthly_average(rainfall_data):
monthly_avg = np.mean(np.array(list(rainfall_data.values())), axis=0)
return monthly_avg
monthly_avg_rainfall = monthly_average(rainfall_data) print("\nMonthly Average Rainfall (across all cities):")
for month, avg in enumerate(monthly_avg_rainfall, start=1):
print(f"Month {month}: {avg:.2f} mm") months = np.arange(1, 7)
plt.figure(figsize=(10, 6))
for city, data in rainfall_data.items():
plt.plot(months, data, marker='o', label=city)
plt.title('Monthly Rainfall Trends in Three Cities') plt.xlabel('Month')
plt.ylabel('Rainfall (mm)')
plt.xticks(months)
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()
rainfall_range = {city: np.max(data) - np.min(data) for city, data in rainfall_data.items()} print("\nRainfall Range for Each City:")
for city, r_range in rainfall_range.items(): print(f"{city}: Range = {r_range} mm")
plt.figure(figsize=(10, 6))
plt.bar(rainfall_range.keys(), rainfall_range.values(), color=['blue', 'orange', 'green']) plt.title('Range of Rainfall for Each City (6 Months)')
plt.xlabel('City')
plt.ylabel('Rainfall Range (mm)')
plt.grid(axis='y')

 plt.tight_layout() plt.show()

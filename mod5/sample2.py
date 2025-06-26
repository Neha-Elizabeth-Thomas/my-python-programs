import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('Weather_data.csv')

# Convert 'date' column to datetime format (for better plotting)
# df['date'] = pd.to_datetime(df['date'])

# 1. Line Plot: Temperature vs Date
plt.figure(figsize=(10, 5))
plt.plot(df['date'], df['temperature'], marker='o', linestyle='-')
plt.title('Temperature Report')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 2. Scatter Plot: Humidity vs Date
plt.figure(figsize=(10, 5))
plt.scatter(df['date'], df['humidity'], color='green')
plt.title('Humidity Report')
plt.xlabel('Date')
plt.ylabel('Humidity (%)')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

# path = Path('python/data_visualization/chapter 16 downloading data/weather_data/sitka_weather_07-2021_simple.csv')
path = Path('python/data_visualization/chapter 16 downloading data/weather_data/sitka_weather_2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)
for index, column_header in enumerate(header_row):
    print(index, column_header)

# Extract dates and high temperatures.
date, highs, lows = [], [], []
tmax = header_row.index('TMAX')
tmin = header_row.index('TMIN')
date_index = header_row.index('DATE')
for row in reader:
    current_date = datetime.strptime(row[date_index], "%Y-%m-%d")
    high = int(row[tmax])
    low = int(row[tmin])
    date.append(current_date)
    highs.append(high)
    lows.append(low)
print(highs)

# Plot the high tempreature
plt.style.use('seaborn-v0_8')
fig,ax = plt.subplots()
# ax.plot(date, highs, low, color = 'red')
ax.plot(date, highs, color = 'red', alpha = 0.5)
ax.plot(date, lows, color = 'red', alpha = 0.5)
ax.fill_between(date, highs, lows, facecolor = 'blue', alpha = 0.1)

# Format plot
# ax.set_title("Daily High Temperatures, July 2021", fontsize = 24)
ax.set_title("Daily High and Low Temperatures 2021",fontsize= 24)
fig.autofmt_xdate()
ax.set_xlabel(" ", fontsize = 16)
ax.set_ylabel("Tempreature (F)", fontsize = 16)
ax.tick_params(labelsize = 16)

plt.show()
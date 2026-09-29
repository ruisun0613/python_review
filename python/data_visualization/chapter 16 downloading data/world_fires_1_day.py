"""
16-9. World Fires: In the resources for this chapter, you’ll find a file called
world_fires_1_day.csv. This file contains information about fires burning in
different locations around the globe, including the latitude, longitude, and
brightness of each fire. Using the data-processing work from the first part of
this chapter and the mapping work from this section, make a map that
shows which parts of the world are affected by fires.
You can download more recent versions of this data at https://earthdata.na
sa.gov/earth-observation-data/near-real-time/firms/active-fire-data. You can
find links to the data in CSV format in the SHP, KML, and TXT Files section.
"""

from pathlib import Path
import csv
import plotly.express as px

path = Path('python/data_visualization/chapter 16 downloading data/eq_data/world_fires_1_day.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)
for index, column_header in enumerate(header_row):
    print(index, column_header)

lats, lons, brights = [], [], []
fire_latitude = header_row.index('latitude')
fire_longitude = header_row.index('longitude')
fire_brightness = header_row.index('brightness')

for row in reader:
    lat = float(row[fire_latitude])
    lon = float(row[fire_longitude])
    bright = float(row[fire_brightness])

    lats.append(lat)
    lons.append(lon)
    brights.append(bright)

# Plot
title = "World Fire Event"
fire_fig = px.scatter_geo(
    lon = lons,
    lat = lats,
    size = brights,
    title = title,
    color = brights,
    color_continuous_scale = 'ylorrd',
    projection = 'natural earth'
)
fire_fig.show()
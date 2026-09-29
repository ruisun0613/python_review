from pathlib import Path
import json

import plotly.express as px

# Read the data as a string and convert to a Python object.
# path = Path('python/data_visualization/chapter 16 downloading data/readable_eq_data.geojson')
path_30 = Path('python/data_visualization/chapter 16 downloading data/eq_data/eq_data_30_day_m1.geojson')

contents = path_30.read_text('utf-8')
all_eq_data = json.loads(contents)

# Examine all earthquakes in the dataset.
all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts))

mags, lons, lats, eq_titles= [], [], [], []
for eq_dicts in all_eq_dicts:
    # mag = eq_dicts['properties']['mag']
    # lon = eq_dicts['geometry']['coordinates'][0]
    # lat = eq_dicts['geometry']['coordinates'][1]
    # eq_title = eq_dicts['properties']['title']
    # mags.append(mag)
    # lons.append(lon)
    # lats.append(lat)
    # eq_titles.append(eq_title)

    # 16-6. Refactoring
    mags.append(eq_dicts['properties']['mag'])
    lons.append(eq_dicts['geometry']['coordinates'][0])
    lats.append(eq_dicts['geometry']['coordinates'][1])
    eq_titles.append(eq_dicts['properties']['title'])

# 16.7 Automated Title
map_title = all_eq_data['metadata']['title']

# title = 'Global Earthquakes'
fig = px.scatter_geo(
    lon = lons, 
    lat = lats, 
    size = mags, 
    title = map_title, 
    color = mags, 
    color_continuous_scale = 'Viridis', 
    labels = {'color':'Magnitude'},
    projection = 'natural earth',
    hover_name = eq_titles
)
fig.show() 

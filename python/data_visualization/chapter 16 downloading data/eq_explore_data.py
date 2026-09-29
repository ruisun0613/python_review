from pathlib import Path
import json

# Read the data as a string and convert to a Python object.
path = Path('python/data_visualization/chapter 16 downloading data/eq_data/eq_data_1_day_m1.geojson')
contents = path.read_text()
all_eq_data = json.loads(contents)

# Create a more readable version of the data file.
path = Path('python/data_visualization/chapter 16 downloading data/readable_eq_data.geojson')
readable_contents = json.dumps(all_eq_data, indent = 4)
path.write_text(readable_contents)

# Examine all earthquakes in the dataset.
all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts))

mags, lons, lats = [], [], []
for eq_dicts in all_eq_dicts:
    mag = eq_dicts['properties']['mag']
    lon = eq_dicts['geometry']['coordinates'][0]
    lat = eq_dicts['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

print(mags[:10])
print(lons[:5])
print(lats[:5])
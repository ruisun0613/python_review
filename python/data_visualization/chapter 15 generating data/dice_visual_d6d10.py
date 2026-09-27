from die import Die
import plotly.express as px

# Create a D6 and a D10 
die_6 = Die()
die_10 = Die(10)

# Make some rolls and store the results in a list.
results = []

for roll in range(50000):
    result = die_6.roll() + die_10.roll()
    results.append(result)

print(results)

# Analyze the results
frequencies = []
max_result = die_6.num_sides + die_10.num_sides
poss_results = range(2, max_result+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)

# Visualize the result
title = "Results of Rolling a D6 and a D10 50,000 Times"
labels= {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x = poss_results, y = frequencies, title = title, labels = labels)
# Further customize chart.
fig.update_layout(xaxis_dtick=1)
fig.show()
fig.write_html('/Python_Review/python/data_visualization/chapter 15 generating data/dice_visual_d6d10.xhtml')
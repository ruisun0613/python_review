from die import Die
import plotly.express as px

# Create a D6
# die = Die()

# Create two D6 dice
die_1 = Die()
die_2 = Die()

# Make some rolls and store the results in a list.
results = []

for roll in range(1000):
    # result = die.roll()
    result = die_1.roll() + die_2.roll()
    results.append(result)

print(results)

# Analyze the results
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
# poss_results = range(2, die.num_sides+1)
poss_results = range(2, max_result+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)

# Visualize the result
# title = "Results of Rolling One D6 1,000 Times"
title = "Results of Rolling Two D6 Dice 1,000 Times"
labels= {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x = poss_results, y = frequencies, title = title, labels = labels)
# Further customize chart.
fig.update_layout(xaixs_dtick = 1)
fig.show()
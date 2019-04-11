from die import Die
import pygal

die1 = Die()
die2 = Die(10)
results = []
for roll_num in range(50000):
    result = die1.roll() + die2.roll()
    results.append(result)

frequencies = []
max_result = die1.num_sides + die2.num_sides
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

hist = pygal.Bar()
hist.title = "result of rolling two D6 dice 1000 times."
hist.x_labels = [str(i) for i in range(2, max_result + 1)]
hist.x_title = "result"
hist.y_title = "frequency of result"

hist.add('D6 + D10', frequencies)
hist.render_to_file('dice_visual.svg')

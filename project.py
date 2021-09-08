import pandas as pd
import plotly.figure_factory as ff
import statistics

df = pd.read_csv('project.csv')
data = df["claps"].tolist()

fig = ff.create_distplot([data],['Math Scores'],show_hist=False)
fig.show()

mean = statistics.mean(data)
stdev = statistics.stdev(data)

range1_min, range1_max = mean-stdev, mean+stdev
range2_min, range2_max = mean-stdev*2, mean+stdev*2
range3_min, range3_max = mean-stdev*3, mean+stdev*3

range1_array = [i for i in data if i > range1_min and i < range1_max]
range2_array = [i for i in data if i > range2_min and i < range2_max]
range3_array = [i for i in data if i > range3_min and i < range3_max]

percent_range1 = len(range1_array)*100/len(data)
percent_range2 = len(range2_array)*100/len(data)
percent_range3 = len(range3_array)*100/len(data)

print(percent_range1)
print(percent_range2)
print(percent_range3)
import statistics 
import csv
import pandas as pd
import random
import plotly.graph_objects as go
import plotly.figure_factory as ff

df = pd.read_csv("StudentsPerformance.csv")
data = df["reading score"].tolist()

data_mean = statistics.mean(data)
data_median = statistics.median(data)
data_mode = statistics.mode(data)
data_stdev = statistics.stdev(data)

first_stdev_start, first_stdev_end = data_mean - data_stdev, data_mean + data_stdev
second_stdev_start, second_stdev_end = data_mean - (2*data_stdev), data_mean + (2*data_stdev)
third_stdev_start, third_stdev_end = data_mean - (3*data_stdev), data_mean + (3*data_stdev)

li_first_stdev = [ result for result in data if result > first_stdev_start and result < first_stdev_end]
li_second_stdev = [ result for result in data if result > second_stdev_start and result < second_stdev_end]
li_third_stdev = [ result for result in data if result > third_stdev_start and result < third_stdev_end]

print("The mean is {}".format(data_mean))
print("The median is {}".format(data_median))
print("The mode is {}".format(data_mode))

print("{}% of data that lies in first deviation".format(len(li_first_stdev)*100/len(data)))
print("{}% of data that lies in second deviation".format(len(li_second_stdev)*100/len(data)))
print("{}% of data that lies in third deviation".format(len(li_third_stdev)*100/len(data)))
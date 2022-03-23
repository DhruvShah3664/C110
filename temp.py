import csv 
import random
import pandas as pd 
import statistics
import plotly.figure_factory as ff 
import plotly.graph_objects as go 

df = pd.read_csv("data4.csv")
data = df["temp"].tolist()

dataset = []

for i in range(0, 100):
    random_index = random.randint(0, len(data))
    value = data[random_index]
    dataset.append(value)
mean  = statistics.mean(dataset)
stddev = statistics.stdev(dataset)

print("mean of sample: ",mean)
print("Standard deviation of sample: ", stddev)

#code to find the mean of 100 data points 1000 times and plot it. Function to get a mean of the given data samples, pass teh number the data points you want as counter.

def random_set_of_mean(counter):
    dataset = []

    for i in range(0, counter):
        random_index = random.randint(0, len(data))
        value = data[random_index]
        dataset.append(value)
    mean  = statistics.mean(dataset)
    return mean

#function to plot the mean on the graph
def show_fig(mean_list):
    df = mean_list
    mean = statistics.mean(df)
    fig  = ff.create_distplot([df], ["temp"], ["Temp"], show_hist = False)
    fig.add_trace(go.Scatter(x = [mean, mean], y = [0, 1], mode = "lines", name = "mean"))
    fig.show()

#pass the no of time u want the mean of the data points as a parametre in range function in for loop

def setup():
    mean_list = []
    for i in range(0, 1000):
        set_of_means = random_set_of_mean(100)
        mean_list.append(set_of_means)
    show_fig(mean_list)
    mean = statistics.mean(mean_list)

    print("Mean of Sampling Distribution: ", mean)

setup()

population_mean = statistics.mean(data)
print("The mean of population: ", population_mean)

def sd():
    mean_list = []
    for i in range(0, 1000):
        set_of_means = random_set_of_mean(100)
        mean_list.append(set_of_means)
    stddev = statistics.stdev(data)
    print("The SD of data: ", stddev)

#sd()

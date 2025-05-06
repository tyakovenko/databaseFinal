import pandas as pd
import matplotlib.pyplot as plt


#graph all times for each question
def graphOneFileTime (qNum):
    df = pd.read_csv(f"/home/taya/PycharmProjects/databaseFinal/analysis/finalTimes/q{qNum}.csv", header=None)
    df.plot(kind='bar', legend=False)
    plt.ylabel('Time(seconds)')
    plt.title(f'Execution Time for Each Run of Query {qNum}')
    plt.xticks([])  # Remove x-axis ticks
    plt.xlabel('')  # Remove x-axis label
    plt.savefig(f'/home/taya/PycharmProjects/databaseFinal/analysis/timeGraphs/time{qNum}.png')
    plt.close()
def graphAllTime ():
    graphOneFileTime(1)
    graphOneFileTime(2)
    graphOneFileTime(3)
    graphOneFileTime(4)
    graphOneFileTime(5)
    graphOneFileTime(6)
    graphOneFileTime(7)
    graphOneFileTime(8)
    graphOneFileTime(9)
    graphOneFileTime(10)
    graphOneFileTime(11)
    graphOneFileTime(12)
    graphOneFileTime(13)
    graphOneFileTime(14)
    graphOneFileTime(15)
    graphOneFileTime(16)
    graphOneFileTime(18)
    graphOneFileTime(19)
    graphOneFileTime(21)

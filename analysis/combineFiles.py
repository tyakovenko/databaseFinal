import pandas as pd
'''
Data preparation steps
1. combine data rom 40 runs and 10 runs
2. combine all the time data from all runs for all the possible ques
3.  Normalize time data, find std and avg. Make bar graphs. Take a note of any outliers
4. Get all the memory data from combined data. Only consider non-zero values. Normalize the data and note any outliers. Find the averages and standard deviation
'''
#get all the data for execution times
def combineAllTime (qNum):
    f1 = f"/home/taya/PycharmProjects/databaseFinal/finalMetrics/10run/10run - q{qNum}.csv"
    f2 = f"/home/taya/PycharmProjects/databaseFinal/finalMetrics/run1/q{qNum}Run.csv"
    f3 = f"/home/taya/PycharmProjects/databaseFinal/finalMetrics/run3/q{qNum}.csv"
    f4 = f"/home/taya/PycharmProjects/databaseFinal/finalMetrics/run4/q{qNum}.csv"

    df1 = pd.read_csv(f1, header=None, usecols=[0], skiprows=[0], index_col=False)
    df2 = pd.read_csv(f2, header=None, usecols=[1], skiprows=[0], index_col=False)
    df3 = pd.read_csv(f3, header=None, usecols=[1], skiprows=[0], index_col=False)
    df4 = pd.read_csv(f4, header=None, usecols=[1], skiprows=[0], index_col=False)

    ser1 = df1.iloc[:,0]
    ser2 = df2.iloc[:,0]
    ser3 = df3.iloc[:, 0]
    ser4 = df4.iloc[:,0]

    final = pd.concat([ser1, ser2, ser3, ser4], ignore_index = True)
    outputFile = f"/home/taya/PycharmProjects/databaseFinal/analysis/finalTimes/q{qNum}.csv"
    final.to_csv(outputFile, index=False, header=False)
    print(final)
def getAllSummary(qNum):
    df = pd.read_csv(f"/home/taya/PycharmProjects/databaseFinal/analysis/finalTimes/q{qNum}.csv", header=None)
    summary_stats = df.describe()
    filtered_stats_series = summary_stats.drop('count').iloc[:, 0]
    return filtered_stats_series
def saveAllStatsTime (outFile):
    s1 = getAllSummary(1)
    s2 = getAllSummary(2)
    s3 = getAllSummary(3)
    s4 = getAllSummary(4)
    s5 = getAllSummary(5)
    s6 = getAllSummary(6)
    s7 = getAllSummary(7)
    s8 = getAllSummary(8)
    s9 = getAllSummary(9)
    s10 = getAllSummary(10)
    s11 = getAllSummary(11)
    s12 = getAllSummary(12)
    s13 = getAllSummary(13)
    s14 = getAllSummary(14)
    s15 = getAllSummary(15)
    s16 = getAllSummary(16)
    s18 = getAllSummary(18)
    s19 = getAllSummary(19)
    s21 = getAllSummary(21)

    sf = pd.concat([s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14, s15, s16, s18, s19, s21], axis=1)
    sf.columns = ['q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'q12', 'q13', 'q14', 'q15', 'q16',
                  'q18', 'q19', 'q21']

    sf.to_csv(outFile)
    print(sf)


#get all the data for memory usage
#note: a lot of filtering and normalization was done here since true memory usage per process was difficult to measure; all the results are approximate in these instances
def combineAllMemory(qNum):
    f1 = f"/home/taya/PycharmProjects/databaseFinal/finalMetrics/10run/10run - q{qNum}.csv"
    f4 = f"/home/taya/PycharmProjects/databaseFinal/finalMetrics/run4/q{qNum}.csv"

    df1 = pd.read_csv(f1, header=None, usecols=[1], skiprows=[0], index_col=False)
    df4 = pd.read_csv(f4, header=None, usecols=[4], skiprows=[0], index_col=False)

    ser1 = df1.iloc[:, 0]
    ser4 = df4.iloc[:, 0]

    final = pd.concat([ser1, ser4], ignore_index=True)
    final = final[final > 0]
    final = final.drop_duplicates()
    outputFile = f"/home/taya/PycharmProjects/databaseFinal/analysis/finalMem/q{qNum}.csv"
    final.to_csv(outputFile, index=False, header=False)
    print(final)
def getAllTime ():
    combineAllMemory(1)
    combineAllMemory(2)
    combineAllMemory(3)
    combineAllMemory(4)
    combineAllMemory(5)
    combineAllMemory(6)
    combineAllMemory(7)
    combineAllMemory(8)
    combineAllMemory(9)
    combineAllMemory(10)
    combineAllMemory(11)
    combineAllMemory(12)
    combineAllMemory(13)
    combineAllMemory(14)
    combineAllMemory(15)
    combineAllMemory(16)
    combineAllMemory(19)
    combineAllMemory(21)
def getAllSummaryMem(qNum):
    df = pd.read_csv(f"/home/taya/PycharmProjects/databaseFinal/analysis/finalMem/q{qNum}.csv", header=None)
    summary_stats = df.describe()
    filtered_stats_series = summary_stats.drop('count').iloc[:, 0]
    return filtered_stats_series

def saveAllStatsMem (outFile):
    s1 = getAllSummaryMem(1)
    s2 = getAllSummaryMem(2)
    s3 = getAllSummaryMem(3)
    s4 = getAllSummaryMem(4)
    s5 = getAllSummaryMem(5)
    s6 = getAllSummaryMem(6)
    s7 = getAllSummaryMem(7)
    s8 = getAllSummaryMem(8)
    s9 = getAllSummaryMem(9)
    s10 = getAllSummaryMem(10)
    s11 = getAllSummaryMem(11)
    s12 = getAllSummaryMem(12)
    s13 = getAllSummaryMem(13)
    s14 = getAllSummaryMem(14)
    s15 = getAllSummaryMem(15)
    s16 = getAllSummaryMem(16)
    s18 = getAllSummaryMem(18)
    s19 = getAllSummaryMem(19)
    s21 = getAllSummaryMem(21)

    sf = pd.concat([s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14, s15, s16, s18, s19, s21], axis=1)
    sf.columns = ['q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'q12', 'q13', 'q14', 'q15', 'q16',
                  'q18', 'q19', 'q21']

    sf.to_csv(outFile)
    print(sf)


#execute commands
saveAllStatsMem("/home/taya/PycharmProjects/databaseFinal/analysis/mem_allStats.csv")
#getAllTime()
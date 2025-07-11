import pandas as pd
import numpy as np
import pathlib
file_path = pathlib.Path("D:/Praveen/Python Core Projects/HPE Python Practice Projects"
                         "/Data/Excel Files/Data Analysis.xlsx")
reading_excel = pd.read_excel(file_path, sheet_name='Correlation', skiprows=1, engine='openpyxl')

dataframe = reading_excel.iloc[:, 1:]

dataframe1 = dataframe.iloc[:, 0:2]
dataframe2 = dataframe.iloc[:, 3:5]
dataframe3 = dataframe.iloc[:, 6:8]

dataframe1.columns = ['Productivity', 'Absenteeism']
dataframe2.columns = ['Productivity', 'Handle Time']
dataframe3.columns = ['Productivity', 'Defect Rate']

print(dataframe1)
print(dataframe2)
print(dataframe3)

merged_df1_df2 = pd.merge(dataframe1, dataframe2, on='Productivity')
merged_dfs = pd.merge(merged_df1_df2, dataframe3, on='Productivity')

print(merged_dfs)


def own_mean(dataframes, column_name):
    total = 0
    count = 0
    for each_value in dataframes[column_name]:
        total += each_value
        count += 1

    if count == 0:
        return None

    return total/count


def own_median(dataframes, column_name):
    sorted_values = sorted(dataframes[column_name])
    n = len(sorted_values)

    if n == 0:
        return None

    mid = n // 2

    if n % 2 == 1:
        return sorted_values[mid]
    else:
        return (sorted_values[mid - 1] + sorted_values[mid]) / 2


columns = ['Absenteeism', 'Handle Time', 'Defect Rate']
for header in columns:
    mean = round(own_mean(merged_dfs, header), 5)
    median = round(own_median(merged_dfs, header), 5)
    mode = merged_dfs[header].mode().tolist()
    print(f"\nName: {header}")
    print(f"Mean: {mean}")
    print(f"Median: {median}")
    print(f"Mode: {mode}")

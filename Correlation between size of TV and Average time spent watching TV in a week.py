import plotly.express as px
import csv
import numpy as np

def getDataSource(data_path):
    size_of_tv = []
    Average_time_spent = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            size_of_tv.append(float(row["Size of TV"]))
            Average_time_spent.append(float(row["Average time spent watching TV in a week (hours)"]))
# return function should be outside the for loop
    return{"x":size_of_tv, "y":Average_time_spent}# x and y axis name should match with csv file

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"],datasource["y"])#this return the matrix
    print("Correlation between size of TV and Average time spent watching TV in a week: \n.....>",correlation[0,1]) #to access 0 row and 1 columns           

def setup():
    data_path = "Size of TV.csv"

    datasource = getDataSource(data_path)
    findCorrelation(datasource)

setup()



    
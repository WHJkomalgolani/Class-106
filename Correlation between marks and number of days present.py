import plotly.express as px
import csv
import numpy as np

def getDataSource(data_path):
    days_present = []
    marks_in_percentage = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            days_present.append(float(row["Days Present"]))
            marks_in_percentage.append(float(row["Marks In Percentage"]))
# return function should be outside the for loop
    return {"x":days_present, "y":marks_in_percentage}# x and y axis name should match with csv file

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"],datasource["y"])#this return the matrix
    print("correlation ", correlation)
    print("Correlation between marks and number of days present: \n.....>",correlation[0,1]) #to access 0 row and 1 columns           

def setup():
    data_path = "Student details.csv"
    datasource = getDataSource(data_path)
    findCorrelation(datasource)

setup()



    
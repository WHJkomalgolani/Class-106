import plotly.express as px
import csv
import numpy as np

def getDataSource(data_path):
    Temperature = []
    Icecreamsales = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            
            Temperature.append(float(row["Temperature"]))
            Icecreamsales.append(float(row["Ice-cream sales"]))
# return function should be outside the for loop
    return{"x" : Temperature, "y" : Icecreamsales}# x and y axis name should match with csv file

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"],datasource["y"])#this return the matrix
    print("Correlation between Temperature vs Ice Cream Sales: \n.....>",correlation[0,1]) #to access 0 row and 1 columns           

def setup():
    data_path="Temperature,Ice-cream Sales,Cold Drinks.csv"    
    
    datasource = getDataSource(data_path)
    findCorrelation(datasource)

setup()

#cold drink cumns is not required

    
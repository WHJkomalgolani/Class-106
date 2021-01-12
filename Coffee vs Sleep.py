import plotly.express as px
import csv

with open("Coffee vs Sleep.csv") as csv_file:
    df = csv.DictReader(csv_file)
    fig = px.scatter(df,x="Coffee", y="Sleep")
    fig.show()
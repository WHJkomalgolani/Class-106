import plotly.express as px
import csv

with open("Student details.csv") as csv_file:
    df = csv.DictReader(csv_file)
    fig = px.scatter(df,x="Days Present", y="Marks In Percentage")
    fig.show()
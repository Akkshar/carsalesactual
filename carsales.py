import pandas as pd
import plotly.express as px

graph = pd.read_csv("Car_sales.csv")
fig = px.bar(graph, x = "Manufacturer", y = "Horsepower", color = "Manufacturer", title = " Car facts ")

fig.show()

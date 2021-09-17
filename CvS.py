import pandas as pd
import numpy as np
import plotly_express as px

df = pd.read_csv("coffeeVsSleep.csv")
data1 = df["Coffee in ml"].tolist()
data2 = df["sleep in hours"].tolist()

dependency = np.corrcoef(data1,data2)
print(dependency[0][1])

chart = px.scatter(df,x="Coffee in ml",y="sleep in hours",color="week")
chart.show()
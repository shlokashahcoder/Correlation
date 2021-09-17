import pandas as pd
import numpy as np
import plotly_express as px

df = pd.read_csv("marksVsPresenties.csv")
data1 = df["Marks In Percentage"].tolist()
data2 = df["Days Present"].tolist()

#thing which is depended comes on y axis
dependency = np.corrcoef(data2,data1)
print(dependency[0][1])

chart = px.scatter(df,x="Days Present",y="Marks In Percentage",color="Roll No")
chart.show()
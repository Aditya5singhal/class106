import pandas as pd
import plotly.express as px

df=pd.read_csv("ice.csv")
fig=px.scatter(df,x="Temperature",y="Ice-cream Sales( ₹ )",title="summer")
fig.show()
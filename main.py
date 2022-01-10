import pandas as pd
import numpy as np
from datetime import datetime
import plotly.express as px
import plotly.graph_objects as go
from jupyter_dash import JupyterDash
import dash_core_components as dcc
import dash_html_components as html
import categorization

# read csv and make dataframe
df = pd.read_csv("accountactivity.csv")

# convert dates to datetime
df.date = pd.to_datetime(df.date)

# budgets dictionary, key = category, value = budget
budget = {
    "entertainment": 50,
    "food": 100,
    "rent": 1000,
    "grocery": 200,
    "transit": 70
}

# categories dictionary, key = category, value = keyword list
categories = {}
for cat in budget:
    categories[cat] = getattr(categorization, cat)

# automatic categorization based on keywords from categorization.py
for cat in categories:
    df.category = np.where(df.description.str.contains(categories.get(cat)), cat, df.category)
    
print(df)

# create monthly expenses bar graph
df = df[df.amount > 0]
Total_Monthly_Expenses_Table = df.groupby(df.date.dt.strftime("%B, %Y"))['amount'].sum().reset_index(name = "sum").sort_values("date", ascending = False)
Total_Monthly_Expenses_Chart = px.bar(Total_Monthly_Expenses_Table, x = "date", y = "sum", title = "Total Monthly Expenses")
Total_Monthly_Expenses_Chart.update_yaxes(title = "Expenses ($)", visible = True, showticklabels = True)
Total_Monthly_Expenses_Chart.update_xaxes(title = "Date", visible=True, showticklabels=True)
Total_Monthly_Expenses_Chart.show()
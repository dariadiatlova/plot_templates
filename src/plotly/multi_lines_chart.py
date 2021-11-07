import plotly.graph_objects as go
import pandas as pd
import numpy as np
from typing import List


def plot_multi_lines_chart(df: pd.DataFrame, x_axis_name: str, y_axis_list_names: List[str]):
    """
    Create dataframe with x column and multiple y-column values. Pass df to the
    function with the column names corresponded to the x and y-axis
    :param df: pandas dataframe with data for x and y axis
    :param x_axis_name: the name of df column common for all data
    :param y_axis_list_names: list of df column names with multiple y-values
    :return: None
    """
    fig = go.Figure()
    for y in y_axis_list_names:
        fig.add_trace(go.Scatter(x=df[x_axis_name], y=df[y], name=y))
    try:
        fig.show()
    except RecursionError:
        print("Recursion Error occurred, please check the data types you pass in the dataframe. Plotly accepts"
              "only native Python data type, for example, try to change np.float128 -> np.float64.")


# df example:
df = pd.DataFrame({'x': range(20),
                   'sin(x)': [np.sin(i) for i in range(20)],
                   'cos(x)': [np.cos(i) for i in range(20)]
                   })
plot_multi_lines_chart(df, 'x', ['sin(x)', 'cos(x)'])

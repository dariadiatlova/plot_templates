import plotly.graph_objects as go
import pandas as pd
import numpy as np
from typing import List


def plot_multi_lines_chart(df: pd.DataFrame, x_axis_name: str, y_axis_list_names: List[str],
                           title_text: str = None, axis_titles: List[str] = None, layout_shapes: List[int] = None):
    """
    Create dataframe with x column and multiple y-column values. Pass df to the
    function with the column names corresponded to the x and y-axis.

    :param df: pd.DataFrame with data for x and y axis
    :param x_axis_name: str, the name of df column common for all data
    :param y_axis_list_names: List[str], df column names with multiple y-values
    :param title_text: str, plot name
    :param axis_titles: List[str], names for x and y axis
    :param layout_shapes: List[int], 4 values correspond to left, right, top and bottom indent.
    :return: None
    """
    fig = go.Figure(layout_title_text=title_text)
    for y in y_axis_list_names:
        fig.add_trace(go.Scatter(x=df[x_axis_name], y=df[y], name=y))

    if axis_titles:
        fig.update_layout(xaxis_title=axis_titles[0], yaxis_title=axis_titles[1])

    if layout_shapes:
        assert len(layout_shapes) == 4, f"Param {layout_shapes} should be a list of 4 integers."
        l, r, t, b = layout_shapes
        fig.update_layout(margin=dict(l=l, r=r, t=t, b=b))

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

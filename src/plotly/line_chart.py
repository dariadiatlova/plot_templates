import pandas as pd
import plotly.express as px
import numpy as np


def plot_line_chart(df: pd.DataFrame, title: str, y: str = 'y', x: str = 'x',):
    """
    Create dataframe with at least 2 columns for x and y axis. Pass df to the
    function with the column names corresponded to the x and y axis
    :param df: pandas dataframe with data for x and y axis
    :param title: your plot title
    :param y: the name of df column with data to plot over y axis
    :param x: the name of df column with data to plot over x axis
    :return: None
    """
    px.line(df, x=x, y=y, title=title).show()


# DF example
df = pd.DataFrame({'sin(x)': [np.sin(i) for i in range(100)], 'x': range(100)})

plot_line_chart(df, y="sin(x)", title='Sin(x)')

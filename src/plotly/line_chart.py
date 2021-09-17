import pandas as pd
import plotly.express as px
import numpy as np


def plot_line_chart(df: pd.DataFrame, x: str = 'x', y: str = 'y'):
    """
    Create dataframe with at least 2 columns for x and y axis. Pass df to the
    function with the collumn names corresponded to the x and y axis
    :param df: pandas dataframe with data for x and y axis
    :return: None
    """
    px.line(df, x='x', y='y').show()

# DF example
df = pd.DataFrame({'y': [np.sin(i) for i in range(100)], 'x': range(100)})

plot_line_chart(df)

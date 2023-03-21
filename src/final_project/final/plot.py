"""Functions plotting results."""

import plotly.express as px


def plot_own_wage(data):
    """Plot regression results for own wage labor elasticity.

    Args:
        data (pandas.DataFrame): The data set.

    Returns:
        plotly.express.Figure: The figure.

    """
    fig_wage = px.scatter(
        data_frame=data,
        y="log_wage",
        x="year",
        trendline="ols",
        labels={"log_wage": "Own wage labor elasticity"},
    )
    fig_wage.update_traces(mode="lines")
    fig_wage.data[-1].line.color = "red"
    fig_wage.data[-1].line.dash = "dash"
    fig_wage.update_layout(
        title_text="Change in own wage labor elasticity for married women throughout time",
        title_x=0.5,
    )

    return fig_wage


def plot_husband_wage(data):
    """Plot regression results for husband wage labor elasticity.

    Args:
        data (pandas.DataFrame): The data set.

    Returns:
        plotly.express.Figure: The figure.

    """
    fig_hus = px.scatter(
        data_frame=data,
        y="husband_wage",
        x="year",
        trendline="ols",
        labels={"husband_wage": "Husband's wage labor elasticity"},
    )
    fig_hus.update_traces(mode="lines")
    fig_hus.data[-1].line.color = "red"
    fig_hus.data[-1].line.dash = "dash"
    fig_hus.update_layout(
        title_text="Change in husband's wage labor elasticity for married women throughout time",
        title_x=0.5,
    )

    return fig_hus

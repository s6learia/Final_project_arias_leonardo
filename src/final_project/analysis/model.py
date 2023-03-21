"""Functions for fitting the regression model."""

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression


def fit_linear_model(data):
    """Fit a linear model to data.

    Args:
        data (pandas.DataFrame): The data set.

    Returns:
        statsmodels.base.model.Results: The fitted model.

    """
    data.replace([np.inf, -np.inf], np.nan, inplace=True)
    data = data.dropna(subset=["log_wage", "husband_wage", "log_hours"])
    years = data.year.unique()
    results = pd.DataFrame(columns=["year", "intercept", "log_wage", "husband_wage"])
    for t in years:
        data_year = data[(data.year == t)]
        x = data_year[["log_wage", "husband_wage"]]
        y = data_year["log_hours"]
        model = LinearRegression().fit(x, y, data_year["wgt"])
        results.loc[len(results)] = [t, model.intercept_, *list(model.coef_)]
    return results

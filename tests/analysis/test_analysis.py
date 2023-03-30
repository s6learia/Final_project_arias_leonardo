"""Tests for the analysis part model."""

import pandas as pd
import pytest
from final_project.analysis.model import fit_linear_model
from final_project.analysis.summary import summary_statistics
from final_project.config import BLD


@pytest.fixture()
def data_for_summary():
    return pd.read_csv(BLD / "python" / "data" / "data_clean.csv")


@pytest.fixture()
def data_for_model():
    return pd.read_csv(BLD / "python" / "data" / "data_for_analysis.csv")


def test_summary(data_for_summary):
    """Tests whether the average annual working hour of every subset of the population
    is positive.

    If the function works correctly it should not create any error.

    """
    summary = summary_statistics(data_for_summary)
    means_men = (
        list(summary["mean of all men"].values())
        + list(summary["mean of married men"].values())
        + list(summary["mean of unmarried men"].values())
    )
    means_women = (
        list(summary["mean of all women"].values())
        + list(summary["mean of married women"].values())
        + list(summary["mean of unmarried women"].values())
    )
    means = means_men + means_women
    assert all(v >= 0 for v in means)


def test_model_rows(data_for_model):
    """Tests whether the created data frame has the expected number of rows."""
    model_df = fit_linear_model(data_for_model)
    assert model_df.shape[0] == 8

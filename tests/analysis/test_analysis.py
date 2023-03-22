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
    model_df = fit_linear_model(data_for_model)
    assert model_df.shape[0] == 8

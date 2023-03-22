import pandas as pd
import pytest
from final_project.config import BLD
from final_project.data_management.clean_data import (
    _count_hh,
    clean_data,
    data_analysis,
)


@pytest.fixture()
def data_for_cleaning():
    return pd.read_csv(BLD / "python" / "data" / "data_total.csv")


@pytest.fixture()
def data_for_analysis():
    return pd.read_csv(BLD / "python" / "data" / "data_for_analysis.csv")


def test_clean_data_age(data_for_cleaning):
    data_clean = clean_data(data_for_cleaning)
    condition = (data_clean["age"] < 25) | (data_clean["age"] > 54)
    out_of_range = data_clean.loc[condition]
    assert len(out_of_range) == 0


def test_clean_data_int(data_for_cleaning):
    data_clean = clean_data(data_for_cleaning)
    assert pd.api.types.is_integer_dtype(data_clean["hhseq"])


def test_data_analysis_number(data_for_analysis):
    data_for_analysis = data_for_analysis[
        (data_for_analysis.hhrel2 == 1) | (data_for_analysis.hhrel2 == 2)
    ]
    data_for_analysis = data_for_analysis[(data_for_analysis.married == 1)]
    analysis_data = _count_hh(data_for_analysis)
    count = analysis_data.groupby(["hhseq", "year"])["hhseq"].count()
    num = count.loc[(count != 2)]
    assert len(num) == 0


def test_data_analysis_female(data_for_analysis):
    analysis_data = data_analysis(data_for_analysis)
    male = analysis_data.loc[(analysis_data["female"] == 0)]
    assert len(male) == 0


def test_data_analysis_married(data_for_analysis):
    analysis_data = data_analysis(data_for_analysis)
    unmarried = analysis_data.loc[(analysis_data["married"] != 1)]
    assert len(unmarried) == 0

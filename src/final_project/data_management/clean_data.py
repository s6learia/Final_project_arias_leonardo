"""Function(s) for cleaning the data set(s)."""
import numpy as np
import pandas as pd


def clean_data(data):
    """Clean the data set by dropping all variables that are not going to be use and
    only keeping individuals in prime age (25 to 56 years old). Besides that, the
    variable annual working hours is created.

    Args:
        data: data set with all appended years.

    Returns:
        pandas.DataFrame: The cleaned data set.

    """
    data["hhseq"] = data["hhseq"].astype(int)
    data = data[
        [
            "age",
            "year",
            "wkslyr",
            "hrslyr",
            "female",
            "wgt",
            "marstat",
            "hhrel2",
            "married",
            "hhseq",
            "rhrwage",
        ]
    ]

    data = data[(data.age > 24) | (data.age < 55)]

    data["anual_worked_hours"] = data["wkslyr"] * data["hrslyr"]

    return data


def data_analysis(data):
    """Modify the cleaned data set for later use in the analysis part. First, drops all
    members of the household that are not head and spouse. Second, drops all unmarried
    couples. Third, keeps only household where both head and spouse were surveyed.
    Finally, gets the variables that are going to be used in the regression.

    Args:
        df: cleaned data set as csv-file.

    Returns:
        pandas.DataFrame: The modified cleaned data set.

    """
    data = data[(data.hhrel2 == 1) | (data.hhrel2 == 2)]
    data = data[(data.married == 1)]
    data_count = data.groupby(["hhseq", "year"])["hhseq"].count()
    data_count = pd.DataFrame(data_count)
    data_count = data_count.rename(columns={"hhseq": "hh_count"})
    merge_data = pd.merge(data, data_count, how="inner", on=["hhseq", "year"])
    merge_data = merge_data[(merge_data.hh_count == 2)]
    merge_data = merge_data.sort_values(["year", "hhseq", "female"])
    merge_data["log_wage"] = np.log(merge_data["rhrwage"])
    merge_data["log_hours"] = np.log(merge_data["anual_worked_hours"])
    merge_data["husband_wage"] = merge_data["log_wage"].shift(1)
    merge_data = merge_data[(merge_data.female == 0)]

    return merge_data

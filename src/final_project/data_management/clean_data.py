"""Function(s) for cleaning the data set(s)."""


def integer_name(df, names, newnames=None):
    """Convert variable from floats to integers and rename it if wishes.

    Needed as in STATA most variables are floats.
    Important for id variables that need to be very precise.

    Args:
        df: The data set.
        names: Name of id variable that needs to be converted.
        newnames: if the one wants to change the name of the variable.

    Returns:
        pandas.DataFrame: The data set with converted id variables.

    """
    if newnames is None:
        df[names] = df[names].astype(int)
        return df
    else:
        df[newnames] = df[names].astype(int)
        df = df.drop(columns=names)
        return df


def clean_data(df):
    """Clean data set.

    Args:
        df: data set with all appended years.

    Returns:
        pandas.DataFrame: The cleaned data set.

    """
    df = integer_name(df, ["hhseq", "hhid"])
    df = df[
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
            "hhid",
        ]
    ]

    df = df[(df.age > 24) | (df.age < 55)]

    df["anual_worked_hours"] = df["wkslyr"] * df["hrslyr"]

    return df

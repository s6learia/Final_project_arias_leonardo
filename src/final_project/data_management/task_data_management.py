"""Tasks for managing the data."""

import zipfile

import pandas as pd
import pytask

from final_project.config import BLD, SRC
from final_project.data_management.clean_data import clean_data


@pytask.mark.depends_on(SRC / "data" / "cepr_march.zip")
@pytask.mark.produces(BLD / "python" / "data")
def task_unzip(depends_on, produces):
    """Task for unzipping data."""
    with zipfile.ZipFile(depends_on, "r") as zip_ref:
        zip_ref.extractall(produces)


@pytask.mark.depends_on(BLD / "python" / "data")
@pytask.mark.produces(BLD / "python" / "data" / "data_clean.csv")
def task_clean_data(depends_on, produces):
    """Task for cleaning the data."""
    data_1980 = pd.read_stata(
        depends_on / "cepr_march_1980.dta",
        convert_categoricals=False,
    )
    data_1985 = pd.read_stata(
        depends_on / "cepr_march_1985.dta",
        convert_categoricals=False,
    )
    data_1990 = pd.read_stata(
        depends_on / "cepr_march_1990.dta",
        convert_categoricals=False,
    )
    data_1995 = pd.read_stata(
        depends_on / "cepr_march_1995.dta",
        convert_categoricals=False,
    )
    data_2000 = pd.read_stata(
        depends_on / "cepr_march_2000.dta",
        convert_categoricals=False,
    )
    data_2005 = pd.read_stata(
        depends_on / "cepr_march_2005.dta",
        convert_categoricals=False,
    )
    data_2010 = pd.read_stata(
        depends_on / "cepr_march_2010.dta",
        convert_categoricals=False,
    )
    data_2015 = pd.read_stata(
        depends_on / "cepr_march_2015.dta",
        convert_categoricals=False,
    )

    res = [
        data_1980,
        data_1985,
        data_1990,
        data_1995,
        data_2000,
        data_2005,
        data_2010,
        data_2015,
    ]

    total = pd.concat(res)

    data = clean_data(total)
    data.to_csv(produces, index=False)

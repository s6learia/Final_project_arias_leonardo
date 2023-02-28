"""Tasks for managing the data."""

import pandas as pd
import pytask

from final_project.config import BLD, SRC
from final_project.data_management.clean_data import clean_data


@pytask.mark.depends_on(
    {
        "1980": SRC / "data" / "cepr_march_1980.dta",
        "1985": SRC / "data" / "cepr_march_1985.dta",
        "1990": SRC / "data" / "cepr_march_1990.dta",
        "1995": SRC / "data" / "cepr_march_1995.dta",
        "2000": SRC / "data" / "cepr_march_2000.dta",
        "2005": SRC / "data" / "cepr_march_2005.dta",
        "2010": SRC / "data" / "cepr_march_2010.dta",
        "2015": SRC / "data" / "cepr_march_2015.dta",
    },
)
@pytask.mark.produces(BLD / "python" / "data" / "data_clean.csv")
def task_clean_data(depends_on, produces):
    """task."""
    data_1980 = pd.read_stata(depends_on["1980"], convert_categoricals=False)
    data_1985 = pd.read_stata(depends_on["1985"], convert_categoricals=False)
    data_1990 = pd.read_stata(depends_on["1990"], convert_categoricals=False)
    data_1995 = pd.read_stata(depends_on["1995"], convert_categoricals=False)
    data_2000 = pd.read_stata(depends_on["2000"], convert_categoricals=False)
    data_2005 = pd.read_stata(depends_on["2005"], convert_categoricals=False)
    data_2010 = pd.read_stata(depends_on["2010"], convert_categoricals=False)
    data_2015 = pd.read_stata(depends_on["2015"], convert_categoricals=False)

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

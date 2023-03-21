"""Tasks for transforming the data for later analysis."""

import pandas as pd
import pytask

from final_project.config import BLD
from final_project.data_management.clean_data import data_analysis


@pytask.mark.depends_on(BLD / "python" / "data" / "data_clean.csv")
@pytask.mark.produces(BLD / "python" / "data" / "data_for_analysis.csv")
def task_clean_data(depends_on, produces):
    """task."""
    clean = pd.read_csv(depends_on)
    analysis = data_analysis(clean)
    analysis.to_csv(produces, index=False)

"""Tasks running the core analyses."""

import pickle

import pandas as pd
import pytask

from final_project.analysis.model import fit_linear_model
from final_project.analysis.summary import summary_statistics
from final_project.config import BLD


@pytask.mark.depends_on(BLD / "python" / "data" / "data_clean.csv")
@pytask.mark.produces(BLD / "python" / "models" / "summary.pickle")
def task_summary_statistics(depends_on, produces):
    """Task for calculating summary statistics."""
    data = pd.read_csv(depends_on)
    stats = summary_statistics(data)
    with open(produces, "wb") as f:
        pickle.dump(stats, f)


@pytask.mark.depends_on(BLD / "python" / "data" / "data_for_analysis.csv")
@pytask.mark.produces(BLD / "python" / "models" / "estimation.csv")
def task_fitting_model(depends_on, produces):
    """Task for fitting a linear model and getting elasticities."""
    data = pd.read_csv(depends_on)
    ols = fit_linear_model(data)
    ols.to_csv(produces, index=False)

"""Tasks running the core analyses."""

import pickle

import pandas as pd
import pytask

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


# for group in GROUPS:


#     @pytask.mark.depends_on(
#         },
#     @pytask.mark.task(id=group, kwargs=kwargs)
#     def task_predict_python(depends_on, group, produces):

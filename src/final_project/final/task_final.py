"""Tasks running the results formatting (tables, figures)."""


# for group in GROUPS:


#     @pytask.mark.depends_on(
#         },
#     @pytask.mark.task(id=group, kwargs=kwargs)
#     def task_plot_results_by_age_python(depends_on, group, produces):


# @pytask.mark.depends_on(BLD / "python" / "models" / "model.pickle")
# @pytask.mark.produces(BLD / "python" / "tables" / "estimation_results.tex")
# def task_create_results_table_python(depends_on, produces):
#     with open(produces, "w") as f:

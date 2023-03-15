"""Tasks running the results formatting (tables, figures)."""

import pickle

import pandas as pd
import pytask

from final_project.config import BLD
from final_project.final.plot import plot_husband_wage, plot_own_wage


@pytask.mark.depends_on(BLD / "python" / "models" / "summary.pickle")
@pytask.mark.produces(BLD / "python" / "tables" / "summary_statistics.tex")
def task_summary_statistics_table(depends_on, produces):
    """Task that creates LaTex table for summary statistics."""
    with open(depends_on, "rb") as summary:
        summary = pickle.load(summary)
    with open(produces, "w") as f:
        f.write(
            "\\begin{table}[hp]\n\\centering\n\\caption{Summary statistics} \n\\renewcommand{\\arraystretch}{1.5}\n\\setlength{\\tabcolsep}{0.3cm}\n",
        )
        f.write(
            "\\begin{tabular}{l|ccccccccc}\n\\toprule\n & \\multicolumn{8}{c}{Year} \\\\\n",
        )
        f.write(
            "Annual hours worked & 1980     & 1985     & 1990     & 1995     & 2000 & 2005 & 2010 & 2015 &  total  \\\\\n",
        )
        f.write(
            "\\midrule\n\\midrule\n& \\multicolumn{8}{c}{\\textbf{Men}}\\\\\n\\midrule\n& \\multicolumn{8}{c}{All}\\\\\n\\midrule\n",
        )
        f.write(
            "mean & "
            + " & ".join(
                str(summary["mean of all men"][x])
                for x in sorted(summary["mean of all men"])
            )
            + " & \\\\\n",
        )
        f.write(
            "$\\Delta$\\% & "
            + " & ".join(
                str(summary["percentage change all men"][x])
                for x in sorted(summary["percentage change all men"])
            )
            + "\\\\\n",
        )
        f.write("\\midrule\n & \\multicolumn{8}{c}{Married}\\\\\n\\midrule\n")
        f.write(
            "mean & "
            + " & ".join(
                str(summary["mean of married men"][x])
                for x in sorted(summary["mean of married men"])
            )
            + " & \\\\\n",
        )
        f.write(
            "$\\Delta$\\% & "
            + " & ".join(
                str(summary["percentage change married men"][x])
                for x in sorted(summary["percentage change married men"])
            )
            + "\\\\\n",
        )
        f.write("\\midrule\n & \\multicolumn{8}{c}{Single}\\\\\n\\midrule\n")
        f.write(
            "mean & "
            + " & ".join(
                str(summary["mean of unmarried men"][x])
                for x in sorted(summary["mean of unmarried men"])
            )
            + " & \\\\\n",
        )
        f.write(
            "$\\Delta$\\% & "
            + " & ".join(
                str(summary["percentage change unmarried men"][x])
                for x in sorted(summary["percentage change unmarried men"])
            )
            + "\\\\\n",
        )
        f.write(
            "\\midrule\n\\midrule\n& \\multicolumn{8}{c}{\\textbf{Wommen}}\\\\\n\\midrule\n& \\multicolumn{8}{c}{All}\\\\\n\\midrule\n",
        )
        f.write(
            "mean & "
            + " & ".join(
                str(summary["mean of all women"][x])
                for x in sorted(summary["mean of all women"])
            )
            + " & \\\\\n",
        )
        f.write(
            "$\\Delta$\\% & "
            + " & ".join(
                str(summary["percentage change all women"][x])
                for x in sorted(summary["percentage change all women"])
            )
            + "\\\\\n",
        )
        f.write("\\midrule\n & \\multicolumn{8}{c}{Married}\\\\\n\\midrule\n")
        f.write(
            "mean & "
            + " & ".join(
                str(summary["mean of married women"][x])
                for x in sorted(summary["mean of married women"])
            )
            + " & \\\\\n",
        )
        f.write(
            "$\\Delta$\\% & "
            + " & ".join(
                str(summary["percentage change married women"][x])
                for x in sorted(summary["percentage change married women"])
            )
            + "\\\\\n",
        )
        f.write("\\midrule\n & \\multicolumn{8}{c}{Single}\\\\\n\\midrule\n")
        f.write(
            "mean & "
            + " & ".join(
                str(summary["mean of unmarried women"][x])
                for x in sorted(summary["mean of unmarried women"])
            )
            + " & \\\\\n",
        )
        f.write(
            "$\\Delta$\\% & "
            + " & ".join(
                str(summary["percentage change unmarried women"][x])
                for x in sorted(summary["percentage change unmarried women"])
            )
            + "\\\\\n",
        )
        f.write("\\bottomrule\n\\end{tabular}\n\\end{table}")


@pytask.mark.depends_on(BLD / "python" / "models" / "estimation.csv")
@pytask.mark.produces(BLD / "python" / "figures" / "Own_wage_elasticity.png")
def task_own_wage_figure(depends_on, produces):
    """Task that plots own wage labor elasticity for married women throughout time."""
    data = pd.read_csv(depends_on)
    own_wage = plot_own_wage(data)
    own_wage.write_image(produces)


@pytask.mark.depends_on(BLD / "python" / "models" / "estimation.csv")
@pytask.mark.produces(BLD / "python" / "figures" / "Husband_wage_elasticity.png")
def task_husband_wage_figure(depends_on, produces):
    """Task that plots husband wage labor elasticity for married women throughout
    time.
    """
    data = pd.read_csv(depends_on)
    husband_wage = plot_husband_wage(data)
    husband_wage.write_image(produces)

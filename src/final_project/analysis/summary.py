"""Functions for getting weighted summary statistics."""

from statsmodels.stats.weightstats import DescrStatsW


def _mean_of_subset(data, female, years, married=None):
    """Creates the weighted mean of the annual working hour of a specific subset of
    population.

    Args:
        married:  1 if married individuals are wanted, 0 if single
        female: 1 if female individuals are wanted, 0 if male
        years: list of all years that are relevant

    Returns:
        dictionary: One weighted mean for each year

    """
    mean = {}
    if married is None:
        for year in years:
            data_subset = data[(data.female == female) & (data.year == year)]
            data_subset = data_subset.dropna(subset=["anual_worked_hours"])
            stats = DescrStatsW(
                data_subset["anual_worked_hours"],
                weights=data_subset["wgt"],
            )
            mean[str(year)] = round(stats.mean)
    else:
        for year in years:
            data_subset = data[
                (data.female == female)
                & (data.married == married)
                & (data.year == year)
            ]
            data_subset = data_subset.dropna(subset=["anual_worked_hours"])
            stats = DescrStatsW(
                data_subset["anual_worked_hours"],
                weights=data_subset["wgt"],
            )
            mean[str(year)] = round(stats.mean)
    return mean


def _per_change(dic, years):
    """Calculates percentage change for a given dictionary of summary statistics.

    Args:
        dic: the dictionary of a specific summary statistic
        years: list of all years that are relevant

    Returns:
        dictionary: The percentage change for each year and the total change

    """
    per = {}
    for k in range(0, len(years)):
        per[str(years[k])] = round(
            100
            * (dic[str(years[k])] - dic[str(years[k - 1])])
            / dic[str(years[k - 1])],
            1,
        )
    per[str(years[0])] = 0
    per["total"] = round(
        100 * (dic[str(years[-1])] - dic[str(years[0])]) / dic[str(years[0])],
        1,
    )
    return per


def summary_statistics(data):
    """Gets summary statistics on working hours along the different years for different
    population subsets.

    The different population groups are: all men, married men, unmarried men, all women,
    married women, unmarried women. First, calculates for the different weighted mean for the different
    years and later, calculated the percentage change

    Args:
        data (pandas.DataFrame): The data set.

    Returns:
        pandas.DataFrame: Predictions. Has columns 'age' and one column for each

    """
    years = data.year.unique()

    mean_men_total = _mean_of_subset(data=data, female=0, years=years, married=None)
    per_men_total = _per_change(mean_men_total, years)

    mean_men_married = _mean_of_subset(data=data, female=0, years=years, married=1)
    per_men_married = _per_change(mean_men_married, years)

    mean_men_unmarried = _mean_of_subset(data=data, female=0, years=years, married=0)
    per_men_unmarried = _per_change(mean_men_unmarried, years)

    mean_women_total = _mean_of_subset(data=data, female=1, years=years, married=None)
    per_women_total = _per_change(mean_women_total, years)

    mean_women_married = _mean_of_subset(data=data, female=1, years=years, married=1)
    per_women_married = _per_change(mean_women_married, years)

    mean_women_unmarried = _mean_of_subset(data=data, female=1, years=years, married=0)
    per_women_unmarried = _per_change(mean_women_unmarried, years)

    return {
        "mean of all men": mean_men_total,
        "percentage change all men": per_men_total,
        "mean of married men": mean_men_married,
        "percentage change married men": per_men_married,
        "mean of unmarried men": mean_men_unmarried,
        "percentage change unmarried men": per_men_unmarried,
        "mean of all women": mean_women_total,
        "percentage change all women": per_women_total,
        "mean of married women": mean_women_married,
        "percentage change married women": per_women_married,
        "mean of unmarried women": mean_women_unmarried,
        "percentage change unmarried women": per_women_unmarried,
    }

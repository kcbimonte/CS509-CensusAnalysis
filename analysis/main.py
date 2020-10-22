import analysis.individual_analyses as ia


def _hispanic_percentage_analysis():
    ia.hispanic_percentage()


def _black_percentage_analysis():
    ia.black_percentage()


def _white_percentage_analysis():
    ia.white_percentage()


if __name__ == '__main__':
    # Analyses the ratio of hispanics vs the total population
    # _hispanic_percentage_analysis()

    # Analyses the ratio of blacks vs the total population
    _black_percentage_analysis()

    # Analyses the ratio of blacks vs the total population
    # _white_percentage_analysis()

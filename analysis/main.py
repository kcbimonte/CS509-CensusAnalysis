import analysis.individual_analyses as ia


def _hispanic_percentage_analysis():
    ia.hispanic_percentage()


def _black_percentage_analysis():
    ia.black_percentage()


def _white_percentage_analysis():
    ia.white_percentage()


def _asian_percentage_analysis():
    ia.asian_percentage()


def _pacific_percentage_analysis():
    ia.pacific_percentage()


def _other_percentage_analysis():
    ia.other_percentage()


def _indian_alaskan_percentage_analysis():
    ia.indian_alaskan_percentage()


def _two_more_percentage_analysis():
    ia.two_more_percentage()


def _racial_diversity_analysis():
    ia.racial_diversity()


def _invalid_analysis():
    print("Invalid Analysis")


if __name__ == '__main__':
    switch = {
        1: _hispanic_percentage_analysis,        # Analyzes the ratio of hispanics vs the total population
        2: _black_percentage_analysis,           # Analyzes the ratio of blacks vs the total population
        3: _white_percentage_analysis,           # Analyzes the ratio of white vs the total population
        4: _asian_percentage_analysis,           # Analyzes the ratio of asian vs the total population
        5: _pacific_percentage_analysis,         # Analyzes the ratio of pacific/native hawaiian vs the total population
        6: _other_percentage_analysis,           # Analyzes the ratio of other vs the total population
        7: _indian_alaskan_percentage_analysis,  # Analyzes the ratio of indian or native alaskan vs the total population
        8: _two_more_percentage_analysis,        # Analyzes the ratio of two or more vs the total population.
        'r': _racial_diversity_analysis          # Calculates the Racial Diversity Index. Only runs properly when all racial files are created
    }

    func = switch.get(8, lambda: _invalid_analysis())
    func()


import analysis.individual_analyses as ia
import analysis.individual_analyses.hispanic.race as hr


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


def _black_hispanic_percentage_analysis():
    hr.hispanic_black_percentage()


def _white_hispanic_percentage_analysis():
    hr.hispanic_white_percentage()


def _asian_hispanic_percentage_analysis():
    hr.hispanic_asian_percentage()


def _pacific_hispanic_percentage_analysis():
    hr.hispanic_pacific_percentage()


def _other_hispanic_percentage_analysis():
    hr.hispanic_other_percentage()


def _indian_alaskan_hispanic_percentage_analysis():
    hr.hispanic_indian_alaskan_percentage()


def _two_more_hispanic_percentage_analysis():
    hr.hispanic_two_more_percentage()


def _racial_hispanic_diversity():
    hr.racial_hispanic_diversity()


if __name__ == '__main__':
    _black_hispanic_percentage_analysis()
    _white_hispanic_percentage_analysis()
    _asian_hispanic_percentage_analysis()
    _pacific_hispanic_percentage_analysis()
    _other_hispanic_percentage_analysis()
    _indian_alaskan_hispanic_percentage_analysis()
    _two_more_hispanic_percentage_analysis()

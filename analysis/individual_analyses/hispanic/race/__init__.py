import analysis.individual_analyses.hispanic.race.racial_percentage as rp
import analysis.individual_analyses.hispanic.race.racial_percentage_not as rpn
import analysis.individual_analyses.hispanic.race.racial_diversity as rd


def hispanic_black_percentage():
    rp.percentage('black', 'Black_Perc', 'Black Hispanic Percentage')


def hispanic_white_percentage():
    rp.percentage('white', 'White_Perc', 'White Hispanic Percentage')


def hispanic_asian_percentage():
    rp.percentage('asian', 'Asian_Perc', 'Asian Hispanic Percentage')


def hispanic_pacific_percentage():
    rp.percentage('pacific', 'Pacific_Perc', 'Native Hawaiian and Other Pacific Hispanic Percentage')


def hispanic_other_percentage():
    rp.percentage('other', 'Other_Perc', 'Other Hispanic Percentage')


def hispanic_indian_alaskan_percentage():
    rp.percentage('indian_alaska', 'Indian_Alaska_Perc', 'Indian or Alaskan Native Hispanic Percentage')


def hispanic_two_more_percentage():
    rp.percentage('two_more', 'Two_More_Perc', 'Two or More Hispanic Percentage')


def not_hispanic_black_percentage():
    rpn.percentage('black', 'Black_Perc', 'Black Not Hispanic Percentage')


def not_hispanic_white_percentage():
    rpn.percentage('white', 'White_Perc', 'White Not Hispanic Percentage')


def not_hispanic_asian_percentage():
    rpn.percentage('asian', 'Asian_Perc', 'Asian Not Hispanic Percentage')


def not_hispanic_pacific_percentage():
    rpn.percentage('pacific', 'Pacific_Perc', 'Native Hawaiian and Other Pacific Not Hispanic Percentage')


def not_hispanic_other_percentage():
    rpn.percentage('other', 'Other_Perc', 'Other Not Hispanic Percentage')


def not_hispanic_indian_alaskan_percentage():
    rpn.percentage('indian_alaska', 'Indian_Alaska_Perc', 'Indian or Alaskan Native Not Hispanic Percentage')


def not_hispanic_two_more_percentage():
    rpn.percentage('two_more', 'Two_More_Perc', 'Two or More Not Hispanic Percentage')


def racial_hispanic_diversity():
    rd.racial_diversity()

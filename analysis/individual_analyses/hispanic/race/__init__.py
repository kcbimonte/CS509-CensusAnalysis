import analysis.individual_analyses.hispanic.race.racial_percentage as rp
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


def racial_hispanic_diversity():
    rd.racial_diversity()

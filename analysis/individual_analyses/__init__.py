import analysis.individual_analyses.hispanic.hispanic_percentage as hp
import analysis.individual_analyses.racial.racial_percentage as rp
import analysis.individual_analyses.racial.racial_diversity as rd


def black_percentage():
    rp.percentage('black', 'Black_Perc', 'Black Percentage')


def white_percentage():
    rp.percentage('white', 'White_Perc', 'White Percentage')


def asian_percentage():
    rp.percentage('asian', 'Asian_Perc', 'Asian Percentage')


def pacific_percentage():
    rp.percentage('pacific', 'Pacific_Perc', 'Native Hawaiian and Other Pacific Percentage')


def other_percentage():
    rp.percentage('other', 'Other_Perc', 'Other Percentage')


def indian_alaskan_percentage():
    rp.percentage('indian_alaska', 'Indian_Alaska_Perc', 'Indian or Alaskan Native Percentage')


def two_more_percentage():
    rp.percentage('two_more', 'Two_More_Perc', 'Two or More Percentage')


def racial_diversity():
    rd.racial_diversity()


def hispanic_percentage():
    hp.percentage_hispanic()

import analysis.individual_analyses.hispanic.hispanic_percentage as hp
import analysis.individual_analyses.racial.black_percentage as bp
import analysis.individual_analyses.racial.white_percentage as wp
import analysis.individual_analyses.racial.asian_percentage as ap
import analysis.individual_analyses.racial.pacific_percentage as pp
import analysis.individual_analyses.racial.other_percentage as op
import analysis.individual_analyses.racial.indian_alaskan_percentage as iap
import analysis.individual_analyses.racial.two_or_more_percentage as tmp

import analysis.individual_analyses.racial.racial_percentage as rp


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


def hispanic_percentage():
    hp.percentage_hispanic()

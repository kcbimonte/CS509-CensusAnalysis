import analysis.individual_analyses as ia
import pandas as pd
import analysis.helper.helper_functions as h


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


def tester():
    print('Analyzing everything')
    with open('../Census_Analysis/Race/asian_perc.json', 'r') as f:
        asian_df = pd.read_json(f, orient='records', dtype=False)

    with open('../Census_Analysis/Race/black_perc.json', 'r') as f:
        black_df = pd.read_json(f, orient='records', dtype=False)
        black_df = black_df[['fips', 'Black_Perc']]

    with open('../Census_Analysis/hispanic_perc.json', 'r') as f:
        hispanic_df = pd.read_json(f, orient='records', dtype=False)
        hispanic_df = hispanic_df[['fips', 'Hispanic_Perc']]

    with open('../Census_Analysis/Race/other_perc.json', 'r') as f:
        other_df = pd.read_json(f, orient='records', dtype=False)
        other_df = other_df[['fips', 'Other_Perc']]

    with open('../Census_Analysis/Race/pacific_perc.json', 'r') as f:
        pacific_df = pd.read_json(f, orient='records', dtype=False)
        pacific_df = pacific_df[['fips', 'Pacific_Perc']]

    with open('../Census_Analysis/Race/white_perc.json', 'r') as f:
        white_df = pd.read_json(f, orient='records', dtype=False)
        white_df = white_df[['fips', 'White_Perc']]

    df = asian_df.merge(black_df, on='fips')
    df = df.merge(other_df, on='fips')
    df = df.merge(pacific_df, on='fips')
    df = df.merge(white_df, on='fips')

    pd.set_option('display.max_columns', None)
    cols = df.columns.tolist()

    cols = cols[:1] + cols[2:3] + cols[1:2] + cols[3:]
    df = df[cols]

    df['Non-White'] = df.iloc[:, 2:-1].sum(axis=1)

    df['Diversity'] = df['Non-White'] / df['White_Perc']

    df['Total Percentage'] = df['Non-White'] + df['White_Perc']

    print(df.head())

    helper = h.Helpers()

    labels = {"Diversity": "sum(Non_White)/White"}
    color = 'Diversity'

    helper.plot(df, color, labels)


if __name__ == '__main__':
    # # Analyzes the ratio of hispanics vs the total population
    # _hispanic_percentage_analysis()
    #
    # # Analyzes the ratio of blacks vs the total population
    _black_percentage_analysis()
    #
    # # Analyzes the ratio of white vs the total population
    _white_percentage_analysis()
    #
    # # Analyzes the ratio of asian vs the total population
    _asian_percentage_analysis()
    #
    # # Analyzes the ratio of pacific/native hawaiian vs the total population
    _pacific_percentage_analysis()

    # Analyzes the ratio of other vs the total population
    _other_percentage_analysis()

    # Analyzes the ratio of indian or native alaskan vs the total population
    _indian_alaskan_percentage_analysis()

    # Analyzes the ratio of two or more vs the total population
    _two_more_percentage_analysis()

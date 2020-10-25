import pandas as pd
import analysis.helper.helper_functions as h


def racial_diversity():
    df = _prepare_dataframe()

    df = _calculate_diversity_index(df)

    df['Text'] = '<br>Breakdowns by Percentages: ' \
                 '<br>Asian: ' + df['Asian_Perc'].round(2).astype(str) + '%' + \
                 '<br>Black: ' + df['Black_Perc'].round(2).astype(str) + '%' +\
                 '<br>Indian or Alaskan Native: ' + df['Indian_Alaska_Perc'].round(2).astype(str) + '%' +\
                 '<br>Other: ' + df['Other_Perc'].round(2).astype(str) + '%' +\
                 '<br>Native Hawaiian and Other Pacific: ' + df['Pacific_Perc'].round(2).astype(str) + '%' +\
                 '<br>White: ' + df['White_Perc'].round(2).astype(str) + '%' +\
                 '<br>Two or More: ' + df['Two_More_Perc'].round(2).astype(str) + '%'

    helper = h.Helpers()

    labels = {"Diversity Index": "Diversity Index (See Readme)"}
    color = 'Diversity Index'

    helper.plot(df, color, labels, hover_data=True)


def _prepare_dataframe():
    path = '../Census_Analysis/Hispanic/Race/'

    with open(path + 'asian_perc.json', 'r') as f:
        asian_df = pd.read_json(f, orient='records', dtype=False)
    with open(path + 'black_perc.json', 'r') as f:
        black_df = pd.read_json(f, orient='records', dtype=False)
        black_df = black_df[['fips', 'Black_Perc']]
    with open(path + 'indian_alaska_perc.json', 'r') as f:
        indian_alaska_df = pd.read_json(f, orient='records', dtype=False)
        indian_alaska_df = indian_alaska_df[['fips', 'Indian_Alaska_Perc']]
    with open(path + 'other_perc.json', 'r') as f:
        other_df = pd.read_json(f, orient='records', dtype=False)
        other_df = other_df[['fips', 'Other_Perc']]
    with open(path + 'pacific_perc.json', 'r') as f:
        pacific_df = pd.read_json(f, orient='records', dtype=False)
        pacific_df = pacific_df[['fips', 'Pacific_Perc']]
    with open(path + 'two_more_perc.json', 'r') as f:
        two_more_df = pd.read_json(f, orient='records', dtype=False)
        two_more_df = two_more_df[['fips', 'Two_More_Perc']]
    with open(path + 'white_perc.json', 'r') as f:
        white_df = pd.read_json(f, orient='records', dtype=False)
        white_df = white_df[['fips', 'White_Perc']]

    df = asian_df.merge(black_df, on='fips')
    df = df.merge(indian_alaska_df, on='fips')
    df = df.merge(other_df, on='fips')
    df = df.merge(pacific_df, on='fips')
    df = df.merge(two_more_df, on='fips')
    df = df.merge(white_df, on='fips')
    cols = df.columns.tolist()
    cols = cols[:1] + cols[2:3] + cols[1:2] + cols[3:]

    df = df[cols]
    return df


def _calculate_diversity_index(df):
    df['Diversity Index'] = (1.00 - (
            (df['Asian_Perc'] / 100) ** 2 + (df['Black_Perc'] / 100) ** 2 +
            (df['Indian_Alaska_Perc'] / 100) ** 2 + (df['Other_Perc'] / 100) ** 2 +
            (df['Pacific_Perc'] / 100) ** 2 + (df['Two_More_Perc'] / 100) ** 2 + (df['White_Perc'] / 100) ** 2))*100

    df['Diversity Index'] = df['Diversity Index'].round(2)

    return df

import pandas as pd
import analysis.helper.helper_functions as h
from os import path


def racial_diversity():
    df = _prepare_dataframe()

    df = _calculate_diversity_index(df)

    df['Text'] = '<br>Breakdowns by Percentages: ' + \
                 '<br>Asian (Hispanic, Not Hispanic): (' + df['Asian_Perc_Yes'].round(2).astype(str) + '%, ' + df[
                     'Asian_Perc_Not'].round(2).astype(str) + '%)' + \
                 '<br>Black (Hispanic, Not Hispanic): (' + df['Black_Perc_Yes'].round(2).astype(str) + '%, ' + df[
                     'Black_Perc_Not'].round(2).astype(str) + '%)' + \
                 '<br>Indian or Alaskan Native (Hispanic, Not Hispanic): (' + df['Indian_Alaska_Perc_Yes'].round(
        2).astype(str) + '%, ' + df['Indian_Alaska_Perc_Not'].round(2).astype(str) + '%)' + \
                 '<br>Other (Hispanic, Not Hispanic): (' + df['Other_Perc_Yes'].round(2).astype(str) + '%, ' + df[
                     'Other_Perc_Not'].round(2).astype(str) + '%)' + \
                 '<br>Native Hawaiian and Other Pacific (Hispanic, Not Hispanic): (' + df['Pacific_Perc_Yes'].round(
        2).astype(str) + '%, ' + df['Pacific_Perc_Not'].round(2).astype(str) + '%)' + \
                 '<br>White (Hispanic, Not Hispanic): (' + df['White_Perc_Yes'].round(2).astype(str) + '%, ' + df[
                     'White_Perc_Not'].round(2).astype(str) + '%)' + \
                 '<br>Two or More (Hispanic, Not Hispanic): (' + df['Two_More_Perc_Yes'].round(2).astype(str) + '%, ' + \
                 df['Two_More_Perc_Not'].round(2).astype(str) + '%)'

    file_path = "../Census_Analysis/Hispanic/Race/diversity_index.json"

    if not path.exists(file_path):
        with open(file_path, 'w') as f:
            df.to_json(f, orient='records')
    else:
        print('File Exists')

    helper = h.Helpers()

    labels = {"Diversity Index": "Diversity Index (See Readme)"}
    color = 'Diversity Index'

    fig = helper.plot(df, color, labels, hover_data=True)

    file_path = "../web_json/diversity/hispanic_racial_diversity.json"

    if not path.exists(file_path):
        import plotly.io as pio
        pio.write_json(fig, file=file_path)
    else:
        print("Plot already written")


def _prepare_dataframe():
    path = '../Census_Analysis/Hispanic/Race/'

    with open(path + 'asian_perc.json', 'r') as f:
        asian_df = pd.read_json(f, orient='records', dtype=False)
        asian_df = asian_df[['fips', 'Location', 'Asian_Perc_Yes', 'Asian_Perc_Not']]
    with open(path + 'black_perc.json', 'r') as f:
        black_df = pd.read_json(f, orient='records', dtype=False)
        black_df = black_df[['fips', 'Black_Perc_Yes', 'Black_Perc_Not']]
    with open(path + 'indian_alaska_perc.json', 'r') as f:
        indian_alaska_df = pd.read_json(f, orient='records', dtype=False)
        indian_alaska_df = indian_alaska_df[['fips', 'Indian_Alaska_Perc_Yes', 'Indian_Alaska_Perc_Not']]
    with open(path + 'other_perc.json', 'r') as f:
        other_df = pd.read_json(f, orient='records', dtype=False)
        other_df = other_df[['fips', 'Other_Perc_Yes', 'Other_Perc_Not']]
    with open(path + 'pacific_perc.json', 'r') as f:
        pacific_df = pd.read_json(f, orient='records', dtype=False)
        pacific_df = pacific_df[['fips', 'Pacific_Perc_Yes', 'Pacific_Perc_Not']]
    with open(path + 'two_more_perc.json', 'r') as f:
        two_more_df = pd.read_json(f, orient='records', dtype=False)
        two_more_df = two_more_df[['fips', 'Two_More_Perc_Yes', 'Two_More_Perc_Not']]
    with open(path + 'white_perc.json', 'r') as f:
        white_df = pd.read_json(f, orient='records', dtype=False)
        white_df = white_df[['fips', 'White_Perc_Yes', 'White_Perc_Not']]

    df = asian_df.merge(black_df, on='fips')
    df = df.merge(indian_alaska_df, on='fips')
    df = df.merge(other_df, on='fips')
    df = df.merge(pacific_df, on='fips')
    df = df.merge(two_more_df, on='fips')
    df = df.merge(white_df, on='fips')

    return df


def _calculate_diversity_index(df):
    df['Diversity Index'] = (1.00 - (
            (df['Asian_Perc_Yes'] / 100) ** 2 + (df['Asian_Perc_Not'] / 100) ** 2 +
            (df['Black_Perc_Yes'] / 100) ** 2 + (df['Black_Perc_Not'] / 100) ** 2 +
            (df['Indian_Alaska_Perc_Yes'] / 100) ** 2 + (df['Indian_Alaska_Perc_Not'] / 100) ** 2 +
            (df['Other_Perc_Yes'] / 100) ** 2 + (df['Other_Perc_Not'] / 100) ** 2 +
            (df['Pacific_Perc_Yes'] / 100) ** 2 + (df['Pacific_Perc_Not'] / 100) ** 2 +
            (df['Two_More_Perc_Yes'] / 100) ** 2 + (df['Two_More_Perc_Not'] / 100) ** 2 +
            (df['White_Perc_Yes'] / 100) ** 2 + (df['White_Perc_Not'] / 100) ** 2)) * 100

    df['Diversity Index'] = df['Diversity Index'].round(2)

    return df

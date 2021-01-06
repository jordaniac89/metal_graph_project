import pandas as pd


def read_bands():
    bands_df = pd.read_csv('/Users/jordanmiles/Downloads/bands.csv')

    groupby = bands_df.groupby(['musical_group', 'musical_groupLabel', 'has_part', 'has_partLabel'])
    bands_df = groupby.apply(lambda df: ','.join(df['genreLabel'])).reset_index()

    return bands_df


def read_members():
    df = pd.read_csv('/Users/jordanmiles/Downloads/band_members.csv')
    df = df[~df['member_of'].isnull().values]

    return df
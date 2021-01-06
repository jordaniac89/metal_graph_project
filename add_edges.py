def add_edges(bands_df, band_members_df):
    edges = [()]
    edges.extend([(row['human'], row['member_of']) for _, row in band_members_df.iterrows()])
    edges.extend([[(row['musical_group'], row['has_part']) for _, row in bands_df.iterrows()]])

    return edges



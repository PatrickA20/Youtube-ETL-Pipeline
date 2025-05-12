import pandas as pd

def transform_data(df):
    # Convert columns to numeric types
    df['view_count'] = pd.to_numeric(df['view_count'], errors='coerce')
    df['like_count'] = pd.to_numeric(df['like_count'], errors='coerce')
    df['comment_count'] = pd.to_numeric(df['comment_count'], errors='coerce')

    # Create Engagement Rate (avoid division by zero)
    df['engagement_rate'] = (df['like_count'] + df['comment_count']) / df['view_count']
    df['engagement_rate'].fillna(0, inplace=True)

    return df

print("Transform function loaded successfully!")

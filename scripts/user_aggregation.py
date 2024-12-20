import pandas as pd

def aggregate_metrics(df):
    """
    Aggregates user behavior data.

    Parameters:
    df (pd.DataFrame): The input dataframe containing user data.

    Returns:
    pd.DataFrame: Aggregated dataframe.
    """

    # Required columns for engagement tracking
    required_columns = [
        'MSISDN/Number', 'Dur. (ms)', 'Total DL (Bytes)', 'Total UL (Bytes)'
    ]

    # Validate required columns
    if not all(col in df.columns for col in required_columns):
        raise ValueError("Dataframe is missing one or more required columns: "
                         + ", ".join(required_columns))

    # Calculate session total traffic
    df['total_traffic'] = df['Total DL (Bytes)'] + df['Total UL (Bytes)']

    # Group by MSISDN/Number to track engagement
    engagement_metrics = df.groupby('MSISDN/Number').agg(
        sessions_frequency=('MSISDN/Number', 'count'),
        total_duration=('Dur. (ms)', 'sum'),
        total_traffic=('total_traffic', 'sum')
    ).reset_index()

    return engagement_metrics
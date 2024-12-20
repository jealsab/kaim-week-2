import pandas as pd
def segment_into_deciles(df):
    """Segment the users into deciles based on total session duration and compute total data per decile."""
    # Ensure the 'Total_Session_Duration' column is numeric for segmentation
    df['total_session_duration'] = pd.to_numeric(df['total_session_duration'], errors='coerce')
    
    # Use pd.qcut to create deciles based on 'Total_Session_Duration'
    df['Decile'] = pd.qcut(df['total_session_duration'], 10, labels=False) + 1  # Adding 1 to make deciles 1-10
    
    # Calculate the total data per decile (DL + UL)
    decile_data = df.groupby('Decile').agg({
        'total_session_duration': 'sum',
        'total_download_data': 'sum',
        'total_upload_data': 'sum',
        'total_data_volume': 'sum'
    }).reset_index()
    
    return decile_data
import pandas as pd

def aggregate_user_traffic(df):
    """
    Aggregate total traffic per user across all applications (download + upload).
    """
   

    
    applications = {
        'Social Media': ['Social Media DL (Bytes)', 'Social Media UL (Bytes)'],
        'YouTube': ['Youtube DL (Bytes)', 'Youtube UL (Bytes)'],
        'Netflix': ['Netflix DL (Bytes)', 'Netflix UL (Bytes)'],
        'Google': ['Google DL (Bytes)', 'Google UL (Bytes)'],
        'Email': ['Email DL (Bytes)', 'Email UL (Bytes)'],
        'Gaming': ['Gaming DL (Bytes)', 'Gaming UL (Bytes)'],
        'Other': ['Other DL (Bytes)', 'Other UL (Bytes)']
    }
    
    
      # Initialize a dictionary to hold the top 10 users per application
    top_users_per_application = {}
    
    # Iterate over each application to calculate total traffic per user
    for app, cols in applications.items():
        # Calculate the total traffic for the current application (sum of DL and UL bytes)
        df[f'{app}_traffic'] = df[cols[0]] + df[cols[1]]
        
        # Group by user (MSISDN/Number) and sum the traffic for each user
        app_user_traffic = df.groupby('MSISDN/Number')[f'{app}_traffic'].sum()
        
        # Sort the users by total traffic and get the top 10 most engaged users
        top_users = app_user_traffic.nlargest(10).reset_index()
        
        # Add the result to the dictionary
        top_users_per_application[app] = top_users
    
    return top_users_per_application
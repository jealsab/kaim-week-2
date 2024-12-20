import matplotlib.pyplot as plt

def plot_top_3_applications(df):
    """
    Plot the top 3 most used applications based on total traffic.
    """
    # Aggregate total traffic per application across all users
    applications = [
        'Social Media DL (Bytes)', 'Social Media UL (Bytes)',
        'Youtube DL (Bytes)', 'Youtube UL (Bytes)', 
        'Netflix DL (Bytes)', 'Netflix UL (Bytes)',
        'Google DL (Bytes)', 'Google UL (Bytes)', 
        'Email DL (Bytes)', 'Email UL (Bytes)', 
        'Gaming DL (Bytes)', 'Gaming UL (Bytes)',
        'Other DL (Bytes)', 'Other UL (Bytes)'
    ]
    
    # Calculate total traffic for each application
    total_app_traffic = df[applications].sum()

    # Sort and select the top 3 most used applications
    top_3_applications = total_app_traffic.nlargest(3)

    # Plotting the top 3 applications
    top_3_applications.plot(kind='bar', color='skyblue')
    plt.title('Top 3 Most Used Applications')
    plt.ylabel('Total Traffic (Bytes)')
    plt.xlabel('Application')
    plt.xticks(rotation=45, ha='right')
    plt.show()


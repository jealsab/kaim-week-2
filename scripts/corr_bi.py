import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def bivariate_and_correlation(df,ad):
    """
    Perform bivariate analysis and correlation analysis on the provided DataFrame.

    Parameters:
    df (pd.DataFrame): DataFrame containing data for various applications and total download/upload data.
    
    Outputs:
    Displays scatter plots for bivariate analysis and a correlation matrix heatmap for the download data.
    Prints the correlation between each application and total data (DL+UL).
    """
    # Bivariate Analysis - Relationship between each application & Total DL+UL
    applications = ['Social Media', 'Google', 
                    'Youtube', 'Netflix', 'Gaming', 'Other']
    ad['total_DL_UL'] = ad['total_download_data'] + ad['total_upload_data']
    merged_df = pd.concat([df, ad['total_DL_UL']], axis=1)
    # Ensure total data for each app (Total_DL_UL)
    for app in applications:
        df[f"{app} Total (Bytes)"] = df[f"{app} DL (Bytes)"] + df[f"{app} UL (Bytes)"]

    df["total data volume"] = df[[f"{app} Total (Bytes)" for app in applications]].sum(axis=1)

    # 1. Scatter Plots for Bivariate Analysis
    plt.figure(figsize=(15, 10))
    for i, app in enumerate(applications, 1):
        plt.subplot(2, 3, i)  # Arrange scatter plots in a grid of 2 rows, 3 columns
        plt.scatter(merged_df[f"{app} Total (Bytes)"], merged_df['total_DL_UL'], alpha=0.7)
        plt.title(f'{app} Total vs Total DL+UL')
        plt.xlabel(f'{app} Total (Bytes)')
        plt.ylabel('Total DL+UL')
        plt.grid(True)
    plt.tight_layout()
    plt.show()
    
    for app in applications:
        correlation = merged_df[f"{app} Total (Bytes)"].corr(merged_df['total_DL_UL'])
        print(f"Correlation between {app} Total and Total DL+UL: {correlation}")
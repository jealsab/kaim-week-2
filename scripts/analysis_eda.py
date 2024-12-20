import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import pandas as pd

# Function to compute and explain basic metrics (mean, median, etc.) using pandas
def basic_metrics(df, numerical_columns):
    """
    Compute and explain basic metrics such as mean, median, standard deviation, and more.
    """
    metrics = df[numerical_columns].describe().T  # Using describe to get mean, std, etc.
    
    # Adding skewness and kurtosis to the summary
    metrics['skewness'] = df[numerical_columns].skew()
    metrics['kurtosis'] = df[numerical_columns].kurt()
    
    print("Basic Metrics:")
    print(metrics[['mean', '50%', 'std', 'skewness', 'kurtosis']])  # '50%' is the median
    print("\n")

# Function for non-graphical univariate analysis using pandas
def non_graphical_univariate_analysis(df, numerical_columns):
    """
    Computes dispersion parameters (mean, std, skewness, kurtosis) for each numerical column.
    """
    # Calculating dispersion parameters for all numerical columns
    analysis_results = df[numerical_columns].agg(['mean', 'std', 'skew', 'kurt']).T
    return analysis_results
def graphical_univariate_analysis(df, numerical_columns):
    """
    This function creates histograms, box plots, and density plots for each numerical column
    to visualize their distributions and detect any outliers or patterns.
    """
    # Set up the plotting grid
    fig, axes = plt.subplots(nrows=3, ncols=len(numerical_columns), figsize=(15, 12))
    fig.tight_layout(pad=5.0)

    # Loop through each column for visualization
    for i, col in enumerate(numerical_columns):
        # Plot Histogram
        sns.histplot(df[col], kde=False, ax=axes[0, i], color='skyblue', bins=20)
        axes[0, i].set_title(f'{col} Histogram')

        # Plot Box Plot
        sns.boxplot(x=df[col], ax=axes[1, i], color='lightgreen')
        axes[1, i].set_title(f'{col} Box Plot')

        # Plot Density Plot
        sns.kdeplot(df[col], ax=axes[2, i], color='red')
        axes[2, i].set_title(f'{col} Density Plot')

    plt.show()

# def top_handsets(data):
#     """Identify the top 10 handsets used by customers."""
#     return data['handset'].value_counts().head(10)

# def top_manufacturers(data):
#     """Identify the top 3 handset manufacturers."""
#     return data['manufacturer'].value_counts().head(3)

# def top_5_handsets_per_manufacturer(data):
#     """
#     Identify the top 5 handsets for each of the top 3 handset manufacturers.
#     """
#     top_manufacturers = data['manufacturer'].value_counts().head(3).index
#     result = {}
#     for manufacturer in top_manufacturers:
#         top_handsets = data[data['manufacturer'] == manufacturer]['handset'].value_counts().head(5)
#         result[manufacturer] = top_handsets
#     return result

# def visualize_data_distribution(data):
#     """Visualize the total data volume and session duration distribution."""
#     plt.figure(figsize=(10, 6))
#     sns.boxplot(data['total_data_volume'])
#     plt.title('Total Data Volume Distribution')
#     plt.show()

#     plt.figure(figsize=(10, 6))
#     sns.histplot(data['session_duration'], bins=30, kde=True)
#     plt.title('Session Duration Distribution')
#     plt.show()

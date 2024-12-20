import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

def compute_cluster_statistics(aggregated_data):
    """
    Compute min, max, avg, and total for each cluster using non-normalized metrics.
    """
    # Ensure we are working with non-normalized data
    cluster_stats = aggregated_data.groupby('cluster')[['sessions_frequency', 'total_duration', 'total_traffic']].agg(
        min_value_sessions=('sessions_frequency', 'min'),
        max_value_sessions=('sessions_frequency', 'max'),
        avg_value_sessions=('sessions_frequency', 'mean'),
        total_value_sessions=('sessions_frequency', 'sum'),
        
        min_value_duration=('total_duration', 'min'),
        max_value_duration=('total_duration', 'max'),
        avg_value_duration=('total_duration', 'mean'),
        total_value_duration=('total_duration', 'sum'),
        
        min_value_traffic=('total_traffic', 'min'),
        max_value_traffic=('total_traffic', 'max'),
        avg_value_traffic=('total_traffic', 'mean'),
        total_value_traffic=('total_traffic', 'sum')
    ).reset_index()

    return cluster_stats


def plot_cluster_statistics(cluster_stats):
    """
    Visualize the statistics with bar plots for each metric (min, max, avg, total)
    """
    fig, ax = plt.subplots(3, 1, figsize=(12, 18))

    # Plot the session frequency statistics
    ax[0].bar(cluster_stats['cluster'], cluster_stats['avg_value_sessions'], label='Average Frequency', color='blue', alpha=0.6)
    ax[0].bar(cluster_stats['cluster'], cluster_stats['min_value_sessions'], label='Min Frequency', color='red', alpha=0.6)
    ax[0].bar(cluster_stats['cluster'], cluster_stats['max_value_sessions'], label='Max Frequency', color='green', alpha=0.6)
    ax[0].set_title('Session Frequency by Cluster')
    ax[0].set_xlabel('Cluster')
    ax[0].set_ylabel('Session Frequency')
    ax[0].legend()

    # Plot the total duration statistics
    ax[1].bar(cluster_stats['cluster'], cluster_stats['avg_value_duration'], label='Average Duration', color='blue', alpha=0.6)
    ax[1].bar(cluster_stats['cluster'], cluster_stats['min_value_duration'], label='Min Duration', color='red', alpha=0.6)
    ax[1].bar(cluster_stats['cluster'], cluster_stats['max_value_duration'], label='Max Duration', color='green', alpha=0.6)
    ax[1].set_title('Total Duration by Cluster')
    ax[1].set_xlabel('Cluster')
    ax[1].set_ylabel('Total Duration (ms)')
    ax[1].legend()

    # Plot the total traffic statistics
    ax[2].bar(cluster_stats['cluster'], cluster_stats['avg_value_traffic'], label='Average Traffic', color='blue', alpha=0.6)
    ax[2].bar(cluster_stats['cluster'], cluster_stats['min_value_traffic'], label='Min Traffic', color='red', alpha=0.6)
    ax[2].bar(cluster_stats['cluster'], cluster_stats['max_value_traffic'], label='Max Traffic', color='green', alpha=0.6)
    ax[2].set_title('Total Traffic by Cluster')
    ax[2].set_xlabel('Cluster')
    ax[2].set_ylabel('Total Traffic (Bytes)')
    ax[2].legend()

    # Show the plot
    plt.tight_layout()
    plt.show()



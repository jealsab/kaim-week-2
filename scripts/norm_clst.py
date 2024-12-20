import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def normalize_metrics(aggregated_data):
    """
    Normalize the engagement metrics (sessions_frequency, total_duration, total_traffic).
    """
    scaler = StandardScaler()
    
    # Select the columns to normalize
    metrics_to_normalize = ['sessions_frequency', 'total_duration', 'total_traffic']
    
    # Apply normalization to the selected columns
    aggregated_data[metrics_to_normalize] = scaler.fit_transform(aggregated_data[metrics_to_normalize])
    
    return aggregated_data

def run_kmeans_clustering(aggregated_data, n_clusters=3):
    """
    Run K-means clustering on normalized data to classify customers into engagement groups.
    """
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    
    # Fit the model and predict cluster assignments
    aggregated_data['cluster'] = kmeans.fit_predict(aggregated_data[['sessions_frequency', 'total_duration', 'total_traffic']])
    
    return aggregated_data, kmeans

def plot_clusters(aggregated_data):
    """
    Visualize the customer segmentation based on the engagement metrics.
    """
    plt.figure(figsize=(10, 6))

    # Scatter plot of total_duration vs total_traffic, color-coded by cluster
    plt.scatter(aggregated_data['total_duration'], aggregated_data['total_traffic'], c=aggregated_data['cluster'], cmap='viridis')
    plt.xlabel('Total Duration (ms)')
    plt.ylabel('Total Traffic (Bytes)')
    plt.title('Customer Segmentation based on Engagement Metrics')
    plt.colorbar(label='Cluster')
    plt.show()

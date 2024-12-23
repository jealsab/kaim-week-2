from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import pandas as pd

def perform_kmeans_clustering(df, features, k=3):
    """
    Perform K-means clustering on the given features of the dataset.
    
    Parameters:
    - df: pandas DataFrame containing the data
    - features: list of columns to include in the clustering
    - k: number of clusters (default: 3)
    
    Returns:
    - DataFrame: The original data with an added cluster label column
    - KMeans: The trained KMeans model
    """
    # Extract relevant features
    X = df[features].dropna()
    
    # Standardize the data
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # Perform K-means clustering
    kmeans = KMeans(n_clusters=k, random_state=42)
    cluster_labels = kmeans.fit_predict(X_scaled)
    
    # Add cluster labels to the DataFrame
    df_clustered = df.copy()
    df_clustered['Cluster'] = -1
    df_clustered.loc[X.index, 'Cluster'] = cluster_labels
    
    return df_clustered, kmeans

def describe_clusters_and_display(df_clustered, cluster_column, features):
    """
    Describe clusters based on their mean feature values and display the results.
    
    Parameters:
    - df_clustered: DataFrame with cluster labels
    - cluster_column: Name of the column containing cluster labels
    - features: List of features used for clustering
    
    Returns:
    - dict: A dictionary with descriptions for each cluster
    """
    cluster_descriptions = {}
    grouped = df_clustered.groupby(cluster_column)
    
    for cluster, group in grouped:
        feature_means = group[features].mean()
        cluster_descriptions[cluster] = feature_means.to_dict()
    
    # Display cluster descriptions
    print("Cluster Descriptions:")
    for cluster, description in cluster_descriptions.items():
        print(f"\nCluster {cluster}:")
        for feature, value in description.items():
            print(f"- {feature}: {value:.2f}")
    
    return cluster_descriptions

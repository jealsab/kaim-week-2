import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

def kmeans_clustering(df):
    """
    Apply K-means clustering and use the elbow method to determine the optimal k.
    """

    engagement_metrics = [
        'Social Media DL (Bytes)', 'Social Media UL (Bytes)',
        'Youtube DL (Bytes)', 'Youtube UL (Bytes)',
        'Netflix DL (Bytes)', 'Netflix UL (Bytes)',
        'Google DL (Bytes)', 'Google UL (Bytes)',
        'Email DL (Bytes)', 'Email UL (Bytes)',
        'Gaming DL (Bytes)', 'Gaming UL (Bytes)',
        'Total DL (Bytes)', 'Total UL (Bytes)',
        'Other DL (Bytes)', 'Other UL (Bytes)'
        
    ]

    # Normalize the data (Scaling the features)
    scaler = StandardScaler()
    df_normalized = scaler.fit_transform(df[engagement_metrics])

    # Elbow Method to Find Optimal k
    inertia = []
    k_range = range(1, 11)

    for k in k_range:
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(df_normalized)
        inertia.append(kmeans.inertia_)

    # Plot inertia vs k
    plt.figure(figsize=(8, 6))
    plt.plot(k_range, inertia, marker='o', linestyle='--')
    plt.title("Elbow Method for Optimal k")
    plt.xlabel("Number of Clusters (k)")
    plt.ylabel("Inertia")
    plt.show()

    # After identifying optimal k from the plot, apply KMeans
    optimal_k = 3  # Example: Replace with your chosen optimal k

    kmeans = KMeans(n_clusters=optimal_k, random_state=42)
    df['engagement_cluster'] = kmeans.fit_predict(df_normalized)

    # View cluster assignments
    print(df[['MSISDN/Number', 'engagement_cluster']].head())


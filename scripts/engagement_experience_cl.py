# task 4
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import euclidean_distances
def eng_exp_cl(df):
# Check if required columns exist
    engagement_features = ["Dur. (ms)", "Total DL (Bytes)", "Total UL (Bytes)"]
    experience_features = [
        "Avg Bearer TP DL (kbps)", "Avg RTT DL (ms)", "TCP DL Retrans. Vol (Bytes)", "Handset Type"
    ]
    if all(col in df.columns for col in engagement_features + experience_features):

        required_features = engagement_features + experience_features
        scaler = StandardScaler()

        # **Engagement Score Calculation**
        # Extract and scale engagement data
        engagement_data = df[engagement_features]
        engagement_scaled = scaler.fit_transform(engagement_data)

        # Perform KMeans clustering for engagement
        kmeans_engagement = KMeans(n_clusters=2, random_state=42)
        kmeans_engagement.fit(engagement_scaled)

        # Identify the less engaged cluster center
        cluster_centers_engagement = kmeans_engagement.cluster_centers_
        less_engaged_cluster_center = cluster_centers_engagement[np.argmin(cluster_centers_engagement.sum(axis=1))]

        # Calculate Euclidean distances for engagement score
        engagement_distances = euclidean_distances(engagement_scaled, [less_engaged_cluster_center])
        df["Engagement Score"] = engagement_distances.flatten()

        # **Experience Score Calculation**
        # Extract and scale experience data
        experience_data = df[experience_features]
        experience_scaled = scaler.fit_transform(experience_data)

        # Perform KMeans clustering for experience
        kmeans_experience = KMeans(n_clusters=2, random_state=42)
        kmeans_experience.fit(experience_scaled)

        # Identify the worst experience cluster center
        cluster_centers_experience = kmeans_experience.cluster_centers_
        worst_experience_cluster_center = cluster_centers_experience[np.argmax(cluster_centers_experience.sum(axis=1))]

        # Calculate Euclidean distances for experience score
        experience_distances = euclidean_distances(experience_scaled, [worst_experience_cluster_center])
        df["Experience Score"] = experience_distances.flatten()

        # **K-Means on Engagement & Experience Scores**
        # Prepare the data for clustering (using only Engagement Score and Experience Score)
        X_clustering = df[["Engagement Score", "Experience Score"]]

        # Perform KMeans clustering with k=2
        kmeans_clustering = KMeans(n_clusters=2, random_state=42)
        kmeans_clustering.fit(X_clustering)

        # Assign the cluster labels to the DataFrame
        df["Cluster Label"] = kmeans_clustering.labels_

        # Output the clusters and a few rows
        print("Clusters have been assigned successfully!")
        print(df[["Engagement Score", "Experience Score", "Cluster Label"]].head())

    else:
        print("Some required columns are missing in the DataFrame. Please verify the dataset.")

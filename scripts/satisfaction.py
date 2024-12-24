import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler, LabelEncoder
from scipy.spatial.distance import euclidean
from sklearn.metrics import euclidean_distances
def calculate_satisfaction_scores(df):

    #  Check if required columns exist
    engagement_features = ["Dur. (ms)", "Total DL (Bytes)", "Total UL (Bytes)"]
    experience_features = [
        "Avg Bearer TP DL (kbps)", "Avg RTT DL (ms)", "TCP DL Retrans. Vol (Bytes)", "Handset Type"
    ]
    # Encode categorical features (e.g., Handset Type)
    if "Handset Type" in df.columns:
        label_encoder = LabelEncoder()
        df["Handset Type"] = label_encoder.fit_transform(df["Handset Type"])
    if all(col in df.columns for col in engagement_features + experience_features):

        required_features = engagement_features + experience_features
        scaler = StandardScaler()

        # **Engagement Score Calculation**
        # Extract and scale engagement data
        engagement_data = df[engagement_features]
        engagement_scaled = scaler.fit_transform(engagement_data)

        # Perform KMeans clustering
        kmeans_engagement = KMeans(n_clusters=2, random_state=42)
        kmeans_engagement.fit(engagement_scaled)

        # Identify the less engaged cluster center (lower average value across features)
        cluster_centers_engagement = kmeans_engagement.cluster_centers_
        less_engaged_cluster_center = cluster_centers_engagement[np.argmin(cluster_centers_engagement.sum(axis=1))]

        # Calculate Euclidean distances for engagement score
        engagement_distances = euclidean_distances(engagement_scaled, [less_engaged_cluster_center])
        df["Engagement Score"] = engagement_distances.flatten()

        # **Experience Score Calculation**
        # Extract and scale experience data
        experience_data = df[experience_features]
        experience_scaled = scaler.fit_transform(experience_data)

        # Perform KMeans clustering
        kmeans_experience = KMeans(n_clusters=2, random_state=42)
        kmeans_experience.fit(experience_scaled)

        # Identify the worst experience cluster center (higher average value across features)
        cluster_centers_experience = kmeans_experience.cluster_centers_
        worst_experience_cluster_center = cluster_centers_experience[np.argmax(cluster_centers_experience.sum(axis=1))]

        # Calculate Euclidean distances for experience score
        experience_distances = euclidean_distances(experience_scaled, [worst_experience_cluster_center])
        df["Experience Score"] = experience_distances.flatten()
        
        #task 2 
        
        # Calculate the average of engagement and experience scores
        df["Satisfaction Score"] = (df["Engagement Score"] + df["Experience Score"]) / 2

        # **Top 10 Satisfied Users**
        # Sort by Satisfaction Score in descending order and select the top 10
        top_10_satisfied_users = df.nlargest(10, "Satisfaction Score")

        # Output the top 10 satisfied users
        print("Top 10 satisfied users:")
        print(top_10_satisfied_users[["Satisfaction Score", "Engagement Score", "Experience Score"]])
        
        # task 3

        # Output the scores
        print("Scores have been calculated successfully!")
        print(df[["Engagement Score", "Experience Score"]].head())

    else:
        print("Some required columns are missing in the DataFrame. Please verify the dataset.")

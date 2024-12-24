import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import euclidean_distances
def calc_predict_satisfaction(df):
    # task 3

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

        # **Satisfaction Score Calculation**
        # Calculate the average of engagement and experience scores
        df["Satisfaction Score"] = (df["Engagement Score"] + df["Experience Score"]) / 2

        # **Regression Model to Predict Satisfaction Score**
        # Prepare the data for regression model
        features = ["Engagement Score", "Experience Score"]
        X = df[features]  # Predictor variables
        y = df["Satisfaction Score"]  # Target variable

        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Initialize the regression model (Linear Regression in this case)
        model = LinearRegression()

        # Train the model
        model.fit(X_train, y_train)

        # Make predictions on the test set
        y_pred = model.predict(X_test)

        # **Evaluate the model**
        mae = mean_absolute_error(y_test, y_pred)
        mse = mean_squared_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)

        # Print the evaluation metrics
        print("Model Evaluation:")
        print(f"Mean Absolute Error (MAE): {mae}")
        print(f"Mean Squared Error (MSE): {mse}")
        print(f"R-squared (R2): {r2}")

        # Print a sample of the predicted vs actual satisfaction scores
        result_df = pd.DataFrame({"Actual": y_test, "Predicted": y_pred})
        print("\nSample Predicted vs Actual Satisfaction Scores:")
        print(result_df.head())

    else:
        print("Some required columns are missing in the DataFrame. Please verify the dataset.")

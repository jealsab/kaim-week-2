# task 5
# Assuming the satisfaction score has already been computed as the average of Engagement and Experience Scores
def aggregation(df):
    df["Satisfaction Score"] = (df["Engagement Score"] + df["Experience Score"]) / 2

# Group by 'Cluster Label' and compute the mean for Satisfaction and Experience Scores
    cluster_aggregates = df.groupby("Cluster Label")[["Satisfaction Score", "Experience Score"]].mean()

    # Output the aggregated results
    print("Aggregated average scores per cluster:")
    print(cluster_aggregates)

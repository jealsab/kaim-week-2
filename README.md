# kaim-week-2

Telecom User Behavior and Engagement Analysis

This project analyzes telecom user behavior and engagement metrics to provide actionable insights, improve Quality of Service (QoS), and optimize resource allocation through exploratory data analysis (EDA) and machine learning.

Features and Functionality

This project is divided into two main tasks: User Overview Analysis and User Engagement Analysis. The features and functionalities include:

Task 1: User Overview Analysis

1.Top Devices Insights

    Identifies the top 10 handsets used by customers.

    Highlights the top 3 handset manufacturers.

    Lists the top 5 handsets for each of the top 3 manufacturers.

2.User Behavior Aggregation

    Aggregates data on user sessions, including session frequency, duration, total download (DL), and upload (UL) data.

    Summarizes data usage for various applications such as Social Media, Google, Email, YouTube, Netflix, Gaming, and others.

3.Exploratory Data Analysis (EDA)

    Handles missing values and outliers by replacing them with statistical measures like the mean.

    Segments users into decile classes based on session duration and analyzes data usage.

    Provides univariate and bivariate analyses of user behavior.

    Computes correlation matrices to identify relationships between data usage across applications.

    Uses Principal Component Analysis (PCA) for dimensionality reduction to simplify data interpretation.

Task 2: User Engagement Analysis

Engagement Metrics

    Aggregates session frequency, duration, and total traffic (DL+UL) for each customer.

    Reports the top 10 customers based on engagement metrics.

Clustering Analysis

    Normalizes engagement metrics and uses k-means clustering to classify users into three engagement groups.

    Computes cluster-specific metrics (minimum, maximum, average, total) for engagement.

    Visualizes and interprets cluster-based results.

Application Usage Analysis

    Aggregates total traffic per application and identifies the top 10 users for each application.

    Visualizes the top 3 most-used applications with appropriate charts.

Optimal Cluster Count

    Determines the optimal value of k for clustering using the elbow method.

    Provides interpretations of engagement clusters and actionable insights for business strategies.

Steps to Run the Project

Step 1: Clone the repository:

    git clone https://github.com/jealsab/kaim-week-2.git

Step 2: Navigate to the project directory:

    cd kaim-week-2

Step 3: Install the required dependencies

    pip install -r requirements.txt

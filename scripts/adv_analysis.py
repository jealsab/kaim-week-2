import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
# Function to perform the analysis
def adv_analysis(df):
    # Safely checking for column existence before performing operations
    if 'Handset Type' in df.columns and 'Handset Manufacturer' in df.columns:
        # 1. Identify the Top 10 Handsets Used by Customers
        top_10_handsets = df['Handset Type'].value_counts().head(10)
        print("Top 10 Handsets:")
        print(top_10_handsets)
    else:
        print("Error: 'Handset Type' column not found in the dataset.")
    
    # Check if 'Handset Manufacturer' column exists before processing
    if 'Handset Manufacturer' in df.columns:
        # 2. Identify the Top 3 Handset Manufacturers
        top_3_manufacturers = df['Handset Manufacturer'].value_counts().head(3)
        print("\nTop 3 Handset Manufacturers:")
        print(top_3_manufacturers)
    else:
        print("Error: 'Handset Manufacturer' column not found in the dataset.")
    
    # Ensure we have both 'Handset Type' and 'Handset Manufacturer' columns before proceeding
    if 'Handset Manufacturer' in df.columns and 'Handset Type' in df.columns:
        top_5_per_manufacturer = {}
        for manufacturer in top_3_manufacturers.index:
            manufacturer_data = df[df['Handset Manufacturer'] == manufacturer]
            top_5_handsets = manufacturer_data['Handset Type'].value_counts().head(5)
            top_5_per_manufacturer[manufacturer] = top_5_handsets

        print("\nTop 5 Handsets Per Manufacturer:")
        for manufacturer, handsets in top_5_per_manufacturer.items():
            print(f"\n{manufacturer}:")
            print(handsets)
    else:
        print("Error: Missing required columns for identifying top 5 handsets per manufacturer.")

def perform_pca(data):
    """Perform Principal Component Analysis (PCA)."""
    numeric_data = data.select_dtypes(include='number')
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(numeric_data)
    
    pca = PCA(n_components=2)
    pca_result = pca.fit_transform(scaled_data)

    # Explained variance ratio of PCA components
    explained_variance = pca.explained_variance_ratio_

    # Visualize the PCA result
    plt.figure(figsize=(8, 6))
    plt.scatter(pca_result[:, 0], pca_result[:, 1], alpha=0.5)
    plt.title('PCA: First Two Principal Components')
    plt.xlabel('PC 1')
    plt.ylabel('PC 2')
    plt.show()

    return explained_variance

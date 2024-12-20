from sklearn.decomposition import PCA
import pandas as pd
import matplotlib.pyplot as plt

def perform_pca(df, ad):
    # Calculate total data for each application (DL + UL)
    applications = ['Social Media', 'Google', 'Youtube', 'Netflix', 'Gaming', 'Other']
    for app in applications:
        df[f"{app} Total (Bytes)"] = df[f"{app} DL (Bytes)"] + df[f"{app} UL (Bytes)"]
    
    # Merge with total DL+UL data from 'ad'
    ad['total_DL_UL'] = ad['total_download_data'] + ad['total_upload_data']
    merged_df = pd.concat([df, ad['total_DL_UL']], axis=1)

    # Select relevant columns for PCA (all applications and total DL+UL)
    pca_columns = [f"{app} Total (Bytes)" for app in applications] + ['total_DL_UL']
    data_for_pca = merged_df[pca_columns]
    
    # Perform PCA
    pca = PCA(n_components=2)  # Reduce to 2 components for visualization
    pca_result = pca.fit_transform(data_for_pca)
    
    # Create a DataFrame with PCA results
    pca_df = pd.DataFrame(pca_result, columns=['PC1', 'PC2'])

    # Plot the results of PCA
    plt.figure(figsize=(8, 6))
    plt.scatter(pca_df['PC1'], pca_df['PC2'], alpha=0.7, c='blue')
    plt.title('PCA - Dimensionality Reduction')
    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.grid(True)
    plt.show()

    # Print the explained variance ratio for each principal component
    print(f"Explained Variance by PC1: {pca.explained_variance_ratio_[0]:.2f}")
    print(f"Explained Variance by PC2: {pca.explained_variance_ratio_[1]:.2f}")
    
    # Return PCA result for interpretation
    return pca, pca_df

# Usage:
# pca, pca_df = perform_pca(df, ad)

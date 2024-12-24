import pandas as pd

def analyze_columns(df, columns, top_n=10):
    """
    Analyzes a list of columns in a DataFrame by computing the top, bottom,
    and most frequent values and displays the results.

    Args:
        df (pd.DataFrame): The input DataFrame.
        columns (list): List of column names to analyze.
        top_n (int): The number of values to retrieve for top, bottom, and frequent categories.
    """
    for column in columns:
        try:
            if column not in df.columns:
                raise ValueError(f"Column '{column}' not found in the DataFrame.")
            
            # Ensure the column is numeric if computing top and bottom
            if not pd.api.types.is_numeric_dtype(df[column]):
                raise TypeError(f"Column '{column}' must be numeric for this computation.")
            
            top_values = df[column].nlargest(top_n).tolist()
            bottom_values = df[column].nsmallest(top_n).tolist()
            frequent_values = df[column].value_counts().head(top_n).index.tolist()

            print(f"\nColumn: {column}")
            print(f"Top 10 values: {top_values}")
            print(f"Bottom 10 values: {bottom_values}")
            print(f"Most frequent 10 values: {frequent_values}")
        
        except Exception as e:
            print(f"\nColumn: {column}")
            print(f"Error: {e}")

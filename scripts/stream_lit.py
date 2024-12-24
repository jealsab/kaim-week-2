import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import os

# Add the path to the script containing the loading function
# sys.path.append(os.path.abspath(os.path.join('..', 'scripts')))

# Import the function to load data from PostgreSQL
from data_load import load_data_from_postgres

# Set up the Streamlit page configuration (must be the first Streamlit command)
st.set_page_config(page_title="User Scores Dashboard", layout="wide")

# SQL query to load data from user_scores table
query = "SELECT * FROM user_scores"
df = load_data_from_postgres(query)

if df is not None:
    df = df.dropna()  # Clean the data by dropping rows with missing values
    st.write("Successfully loaded the data")
    st.write(df.head())  # Display the first few rows of the DataFrame
else:
    st.write("Failed to load the data")

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Select a page:", ["User Overview Analysis", "User Engagement Analysis", "Experience Analysis", "Satisfaction Analysis"])

import matplotlib.pyplot as plt
import seaborn as sns

def plot_engagement_score():
    # Aggregating the data by 'MSISDN/Number' and calculating the mean engagement score
    engagement_data = df.groupby('MSISDN/Number')['Engagement Score'].mean().reset_index()
    
    # Optional: Sampling the aggregated data to reduce the number of points if necessary
    df_sampled = engagement_data.sample(n=1000)  # Sample 1000 random rows for faster processing
    
    # Plotting with the sampled and aggregated data
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Plotting the data
    sns.barplot(
        x="MSISDN/Number", 
        y="Engagement Score", 
        data=df_sampled, 
        hue="MSISDN/Number", 
        palette="viridis", 
        legend=False, 
        ax=ax
    )
    ax.set_title("User Engagement Score")
    ax.set_xlabel("User")
    ax.set_ylabel("Engagement Score")

    # Displaying the plot in Streamlit
    st.pyplot(fig)

def plot_experience_score():
    # Aggregating the data by 'MSISDN/Number' and calculating the mean Experience score
    experience_data = df.groupby('MSISDN/Number')['Experience Score'].mean().reset_index()
    
    # Optional: Sampling the aggregated data to reduce the number of points if necessary
    df_sampled = experience_data.sample(n=1000)  # Sample 1000 random rows for faster processing
    
    # Plotting with the sampled and aggregated data
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Plotting the data
    sns.barplot(
        x="MSISDN/Number", 
        y="Experience Score", 
        data=df_sampled, 
        hue="MSISDN/Number", 
        palette="magma", 
        legend=False, 
        ax=ax
    )
    ax.set_title("User Experience Score")
    ax.set_xlabel("User")
    ax.set_ylabel("Experience Score")

    # Displaying the plot in Streamlit
    st.pyplot(fig)


def plot_satisfaction_score():
    # Aggregating the data by 'MSISDN/Number' and calculating the mean Satisfaction score
    satisfaction_data = df.groupby('MSISDN/Number')['Satisfaction Score'].mean().reset_index()
    
    # Optional: Sampling the aggregated data to reduce the number of points if necessary
    df_sampled = satisfaction_data.sample(n=1000)  # Sample 1000 random rows for faster processing
    
    # Plotting with the sampled and aggregated data
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Plotting the data
    sns.barplot(
        x="MSISDN/Number", 
        y="Satisfaction Score", 
        data=df_sampled, 
        hue="MSISDN/Number", 
        palette="magma", 
        legend=False, 
        ax=ax
    )
    ax.set_title("User Satisfaction Score")
    ax.set_xlabel("User")
    ax.set_ylabel("Satisfaction Score")

    # Displaying the plot in Streamlit
    st.pyplot(fig)
    
# Function for User Overview Analysis
def user_overview():
    st.title("User Overview Analysis")
    st.write("This page displays an overview of user data, including engagement, experience, and satisfaction scores.")
    st.dataframe(df)

# Display the selected page and its corresponding plot
if page == "User Overview Analysis":
    user_overview()
elif page == "User Engagement Analysis":
    st.title("User Engagement Analysis")
    plot_engagement_score()
elif page == "Experience Analysis":
    st.title("Experience Analysis")
    plot_experience_score()
elif page == "Satisfaction Analysis":
    st.title("Satisfaction Analysis")
    plot_satisfaction_score()

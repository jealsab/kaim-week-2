# analysis_functions.py

import pandas as pd

def analyze_handset_metrics(df):
    """
    Analyze the distribution of throughput and TCP retransmission volume per handset type.
    
    Parameters:
    - df: pandas DataFrame containing the data
    
    Returns:
    - dict: A dictionary containing the analysis results
    """
    results = {}
    try:
        # Distribution of Average Throughput per Handset Type
        throughput_distribution = (
            df.groupby('Handset Type')['Avg Bearer TP DL (kbps)']
            .mean()
            .sort_values(ascending=False)
        )
        results['throughput'] = throughput_distribution
        
        # Average TCP Retransmission Volume per Handset Type
        retransmission_avg = (
            df.groupby('Handset Type')['TCP DL Retrans. Vol (Bytes)']
            .mean()
            .sort_values(ascending=False)
        )
        results['retransmission'] = retransmission_avg
        
    except Exception as e:
        print(f"Error during analysis: {e}")
    
    return results

def report_analysis_results(analysis_results):
    """
    Report the analysis results and provide interpretation.
    
    Parameters:
    - analysis_results: dict containing throughput and retransmission analysis results
    """
    if analysis_results:
        # Throughput distribution
        print("\nDistribution of Average Throughput per Handset Type:")
        print(analysis_results['throughput'])

        # Retransmission distribution
        print("\nAverage TCP Retransmission Volume per Handset Type:")
        print(analysis_results['retransmission'])

        
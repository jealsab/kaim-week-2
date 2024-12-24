import pandas as pd
import numpy as np

def handle_missing_and_outliers(df, column_name):
    """
    Replace missing values and outliers in a column with the mean (for numerical) or mode (for categorical).
    """
    if df[column_name].dtype in [np.float64, np.int64]:
        mean_value = df[column_name].mean()
        df[column_name] = df[column_name].fillna(mean_value)
        df[column_name] = np.where((df[column_name] > df[column_name].mean() + 3 * df[column_name].std()) |
                                   (df[column_name] < df[column_name].mean() - 3 * df[column_name].std()),
                                   mean_value, df[column_name])
    else:
        mode_value = df[column_name].mode()[0]
        df[column_name] = df[column_name].fillna(mode_value)
    return df

def aggregate_customer_data(df):
    """
    Aggregate the required information per customer.
    """
    df = handle_missing_and_outliers(df, 'Avg RTT DL (ms)')
    df = handle_missing_and_outliers(df, 'Avg RTT UL (ms)')
    df = handle_missing_and_outliers(df, 'Avg Bearer TP DL (kbps)')
    df = handle_missing_and_outliers(df, 'Avg Bearer TP UL (kbps)')
    df = handle_missing_and_outliers(df, 'TCP DL Retrans. Vol (Bytes)')
    df = handle_missing_and_outliers(df, 'TCP UL Retrans. Vol (Bytes)')

    # Aggregate data
    aggregated_data = df.groupby('MSISDN/Number').agg(
        Average_TCP_Retransmission=('TCP DL Retrans. Vol (Bytes)', 'mean'),
        Average_RTT=('Avg RTT DL (ms)', 'mean'),
        Handset_Type=('Handset Type', lambda x: x.mode()[0] if not x.mode().empty else None),
        Average_Throughput=('Avg Bearer TP DL (kbps)', 'mean')
    ).reset_index()
    
    return aggregated_data

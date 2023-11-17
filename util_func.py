# time_series_utils.py

import pandas as pd
import numpy as np


import pandas as pd

def replace_negative_with_mean(df, cols):
    for col in cols:
        # Calculate mean excluding values less than or equal to 0
        mean_value = df[df[col] > 0][col].mean()
        
        # Replace values less than or equal to 0 with the calculated mean
        df[col] = df[col].apply(lambda x: mean_value if x <= 0 else x)
    
    return df



# time_series_utils.py

import pandas as pd

def preprocess_time_series(df, date_column='ds', value_column='y', target_frequency='M', interpolation_method='linear', fillna_value=None):
    """
    Preprocess time series data with irregular time intervals.

    Parameters:
    - df: pandas DataFrame containing time series data.
    - date_column: Name of the column containing dates (default is 'ds').
    - value_column: Name of the column containing the data values (default is 'y').
    - target_frequency: Target frequency for resampling (e.g., 'D' for daily, 'W' for weekly, 'M' for monthly).
    - interpolation_method: Method to use for interpolation (default is 'linear').
    - fillna_value: Value to fill missing entries before interpolation (default is None).

    Returns:
    - Preprocessed pandas DataFrame with a fixed frequency time series.
    """
    # Convert the date_column to datetime type
    df[date_column] = pd.to_datetime(df[date_column])

    # Set the date_column as the index
    df.set_index(date_column, inplace=True)

    # Resample the time series data to the target frequency
    df_resampled = df.resample(target_frequency).sum()  # Using sum as an example, you can change it to your aggregation function

    # Fill missing values if specified
    if fillna_value is not None:
        df_resampled[value_column].fillna(fillna_value, inplace=True)

    # Interpolate missing values
    df_resampled[value_column] = df_resampled[value_column].interpolate(method=interpolation_method)

    # Reset the index to make the date_column a regular column again
    df_resampled.reset_index(inplace=True)

    return df_resampled

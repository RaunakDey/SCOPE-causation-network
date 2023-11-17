# time_series_utils.py

import pandas as pd
import numpy as np





def preprocess_time_series(df, date_column='ds', value_column='y', target_frequency='M', interpolation_method='linear', remove_negative = True, fillna_value=None):
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
    (c) Raunak Dey -- SCOPE causation network

    """
    # Convert the date_column to datetime type
    df[date_column] = pd.to_datetime(df[date_column])

    # Set the date_column as the index
    df.set_index(date_column, inplace=True)

    # remove negative values
    if remove_negative is True:
        df[value_column] = df[value_column].apply(lambda x: float("nan") if x < 0 else x)

    # Resample the time series data to the target frequency
    df_resampled = df.resample(target_frequency).mean()  # Using sum as an example, you can change it to your aggregation function

    # Fill missing values if specified
    if fillna_value is None:
        df_resampled[value_column].fillna(float("NaN"), inplace=True)

    # Interpolate missing values
    df_resampled[value_column] = df_resampled[value_column].interpolate(method=interpolation_method)

    # Reset the index to make the date_column a regular column again
    df_resampled.reset_index(inplace=True)

    return df_resampled



def replace_negative_with_mean(df, cols):
    """
    Replace the zeros and negative data of the frame with means of the non-zero elements

    Parameters:
    -- df: pandas DataFrame containing time series data.
    -- cols: list of the columns in the dataframe for which the operation is performed
    
    Returns:
    - Processed pandas DataFrame with a greater than zero time series

    (c) Raunak Dey -- SCOPE causation network

    """

    for col in cols:
        # Calculate mean excluding values less than or equal to 0
        mean_value = df[df[col] > 0][col].mean()
        
        # Replace values less than or equal to 0 with the calculated mean
        df[col] = df[col].apply(lambda x: mean_value if x <= 0 else x)
    
    return df



def time_series_equalfreq(df, date_column='ds', value_column='y'):
    '''
    Resample the time series so that the final time series becomes uni -- frequency, by upscaling.

    Parameters:  
    - df: pandas dataframe on which the operation is performed
    - date_column : for which the dates are setected to be performed upon
    - value_column: the column which is upscaled

    Returns:
    - df_processed : final dataframe with processed time series. 
    '''
    
    #upsampled = df.resample('D')
    #interpolated = upsampled.interpolate(method='spline', order=2)

    return 0


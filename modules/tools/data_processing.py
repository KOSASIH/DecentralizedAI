import pandas as pd
import numpy as np

def process_dataframe(df: pd.DataFrame, operations: dict) -> pd.DataFrame:
    """
    Apply data processing operations on a given dataframe.

    Args:
    df (pd.DataFrame): The input dataframe.
    operations (dict): A dictionary of data processing operations,
        where the keys are the column names and the values are the
        operations as functions.

    Returns:
    pd.DataFrame: The processed dataframe.
    """

    for column, operation in operations.items():
        if column not in df.columns:
            raise KeyError(f"Column '{column}' does not exist in the dataframe.")

        df[column] = operation(df[column])

    return df

def apply_imputation(series: pd.Series) -> pd.Series:
    """
    Apply mean imputation on a given series.

    Args:
    series (pd.Series): The input series.

    Returns:
    pd.Series: The processed series.
    """

    mean = series.mean()

    return series.fillna(mean)

def apply_standardization(series: pd.Series) -> pd.Series:
    """
    Apply standardization on a given series.

    Args:
    series (pd.Series): The input series.

    Returns:
    pd.Series: The processed series.
    """

    mean = series.mean()
    std = series.std()

    return (series - mean) / std

if __name__ == "__main__":
    # Example usage

    data = {
        "A": [1, 2, 3, np.nan, 5],
        "B": [np.nan, 2, 3, 4, 5],
        "C": [1, 2, 3, 4, 5],
    }

    df = pd.DataFrame(data)

    operations = {
        "A": apply_imputation,
        "B": apply_imputation,
        "C": apply_standardization,
    }

    df_processed = process_dataframe(df, operations)

    print(df_processed)

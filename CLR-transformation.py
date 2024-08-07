import numpy as np
import pandas as pd

def clr_transformation(df):
    # Ensure no zero values in the DataFrame to prevent issues with log
    if (df <= 0).any().any():
        raise ValueError("All values in the DataFrame must be positive for CLR transformation.")

    # Calculate geometric mean for each row
    geometric_means = np.exp(np.mean(np.log(df.values), axis=1))

    # Perform CLR transformation
    clr_values = np.log(df.values / geometric_means[:, np.newaxis])

    # Create a new DataFrame with CLR transformed values
    clr_df = pd.DataFrame(clr_values, columns=[f"{col}-CLR" for col in df.columns])

    return clr_df

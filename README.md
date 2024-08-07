# CLR Transformation Function

This repository contains a Python function for performing **Centered Log-Ratio (CLR) Transformation** on a DataFrame. The CLR transformation is commonly used in compositional data analysis to normalize and handle data that represent parts of a whole.

## Function Overview

The `clr_transformation` function computes the CLR transformation for each row in a DataFrame. This is particularly useful for analyzing compositional data, where each row represents a composition and the values are proportions or counts.

### Function Definition

```python
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
```

## Parameters

   * df (pd.DataFrame): A DataFrame containing positive numerical values. Each row in the DataFrame represents a composition, and each column represents a component of the composition.

## Returns

   * pd.DataFrame: A new DataFrame with the CLR-transformed values. The columns of the returned DataFrame are named using the original column names appended with -CLR.

## Requirements

    * numpy: Version 1.18.0 or later
    * pandas: Version 1.0.0 or later

### Example Usage

Here's an example of how to use the `clr_transformation` function:

```python
import pandas as pd
import numpy as np

# Define a sample DataFrame with positive numerical values
data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
}

df = pd.DataFrame(data)

# Print the original DataFrame
print("Original DataFrame:")
print(df)

# Perform CLR transformation
clr_df = clr_transformation(df)

# Show transformed DataFrame
clr_df

```

### Error Handling

The `clr_transformation` function raises a `ValueError` if any value in the DataFrame is zero or negative. This is because the CLR transformation requires all input values to be strictly positive. Ensure that your DataFrame contains only positive numerical values before calling the function to avoid this error.

## License

This project is licensed under the MIT License. See the [LICENSE](https://opensource.org/license/mit) file for details.

## Contributing

Contributions are welcome! If you have suggestions for improvements or bug fixes, please follow these steps to contribute:

1. **Fork the Repository:** Click the "Fork" button at the top right of the repository page to create your own copy of the project.
2. **Create a Branch:** Create a new branch in your forked repository for your changes.
3. **Make Changes:** Implement your improvements or fixes on the new branch.
4. **Submit a Pull Request:** Push your changes to your fork and open a pull request to merge your changes into the main repository.

Please make sure to include a clear description of the changes you made and any relevant context. 

## Contact

For any questions, issues, or feedback, please contact my social media:

You can also open an issue on GitHub to ask questions or report problems with the project.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def visualize_data(data: pd.DataFrame) -> None:
    """
    Visualize the given dataframe using various plots.

    Args:
    data (pd.DataFrame): The input dataframe.

    Returns:
    None
    """

    # Plot a correlation matrix using Seaborn
    sns.heatmap(data.corr(), annot=True, cmap="coolwarm")
    plt.show()

    # Plot a histogram for each column
    data.hist()
    plt.show()

    # Plot a pairplot for the dataframe
    sns.pairplot(data)
    plt.show()

    # Plot a boxplot for each column
    data.boxplot()
    plt.show()

    # Plot a line plot for a selected column
    data["column_name"].plot()
    plt.show()

if __name__ == "__main__":
    # Example usage

    data = pd.read_csv("data.csv")

    visualize_data(data)

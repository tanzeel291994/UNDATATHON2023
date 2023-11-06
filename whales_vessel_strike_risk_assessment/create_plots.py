import os, sys
from os.path import dirname as up

sys.path.append(os.path.abspath(os.path.join(up(__file__), os.pardir)))

from utils import *


class DataPlotter:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def create_corr_matrix_plot(self):
        corr = self.df.corr()

        # Set up the matplotlib figure
        f, ax = plt.subplots(figsize=(5, 5))

        # Draw the heatmap with the mask and correct aspect ratio
        sns.heatmap(corr, annot=True, ax=ax)

        # Show the plot
        plt.show()

    def plot_continuous_pairs(self, continuous_vars=None):
        if continuous_vars is None:
            continuous_vars = self.df.select_dtypes(
                include=["float64", "int64"]
            ).columns.tolist()

        pair_plot = sns.pairplot(self.df[continuous_vars])
        pair_plot.fig.suptitle("Pair Plot of Continuous Variables", y=1.02)
        plt.tight_layout()
        plt.show()

    def plot_relationships(self, continuous_vars, categorical_vars):
        for cont_var in continuous_vars:
            for cat_var in categorical_vars:
                if pd.api.types.is_numeric_dtype(self.df[cont_var]):
                    plt.figure(figsize=(10, 6))
                    sns.boxplot(x=cat_var, y=cont_var, data=self.df)
                    plt.title(f"Relationship between {cat_var} and {cont_var}")
                    plt.xticks(rotation=45)
                    plt.tight_layout()
                    plt.show()
                else:
                    print(f"{cont_var} is not a continuous variable.")

import os, sys
from os.path import dirname as up

sys.path.append(os.path.abspath(os.path.join(up(__file__), os.pardir)))

from utils import *


class DataReader:
    def __init__(self):
        pass  # No initialization needed if we're not storing any state

    def read_from_gdb(self, gdb_path: str, layer_name=None) -> gpd.GeoDataFrame:
        """
        Loads a layer from a GeoDatabase.

        :param gdb_path: Path to the GeoDatabase.
        :param layer_name: Optional name of the layer to load. If None, the first layer found is loaded.
        :return: A GeoDataFrame of the loaded layer.
        """

        # List all layers within the GeoDatabase
        print("Loading GeoDatabase...")
        layers = fiona.listlayers(gdb_path)
        print("Layers found:", layers)

        # Load a specific layer
        if layer_name is None:
            layer_name = layers[0]  # Default to the first layer if no name is provided

        with fiona.Env(METHOD="ONLY_CCW"):
            gdf = gpd.read_file(gdb_path, layer=layer_name)

        print("Loading completed.")
        return gdf

    def read_csv(self, path: str, **kwargs) -> pd.DataFrame:
        """
        Read a CSV file and return a pandas DataFrame.

        :param path: The path to the CSV file.
        :param kwargs: Additional keyword arguments to pass to the `pd.read_csv` function.
        :return: The DataFrame containing the data from the CSV file.
        """
        print("Reading CSV file.")
        return pd.read_csv(path, **kwargs)

    def transform_to_geodataframe(
        self, data: Union[pd.DataFrame, gpd.GeoDataFrame] = None, **kwargs
    ) -> gpd.GeoDataFrame:
        print("Transforming to GeoDataFrame.")
        # Create a GeoDataFrame, using the longitude and latitude columns to create Point geometries
        return gpd.GeoDataFrame(data, **kwargs)

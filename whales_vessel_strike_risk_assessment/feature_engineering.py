import os, sys
from os.path import dirname as up

sys.path.append(os.path.abspath(os.path.join(up(__file__), os.pardir)))

from utils import *


def calculate_portion_not_recorded(duty_cycle):
    on_time, off_time = map(
        float, duty_cycle.replace("on", "").replace("off", "").split("/")
    )
    return off_time / (on_time + off_time)


def calculate_bounding_box_with_margin(coordinates, margin=0.01):
    """
    Calculate the bounding box with a margin from a list of (latitude, longitude) tuples.

    :param coordinates: List of (latitude, longitude) tuples
    :param margin: Margin to add to each side of the bounding box, in degrees
    :return: Tuple representing the bounding box with margin (min_lat, max_lat, min_lon, max_lon)
    """
    min_lat = min(coordinates, key=lambda x: x[0])[0] - margin
    max_lat = max(coordinates, key=lambda x: x[0])[0] + margin
    min_lon = min(coordinates, key=lambda x: x[1])[1] - margin
    max_lon = max(coordinates, key=lambda x: x[1])[1] + margin

    return min_lat, max_lat, min_lon, max_lon


# Assuming merged_df is a GeoDataFrame and "geometry" column contains geometries to which you want to calculate distances.
def calculate_distance(row):
    # Create a point from the current row's longitude and latitude
    buoy_point = Point(row["Long-Bouy"], row["Lat-Bouy"])
    # Return the distance from the buoy point to the geometry in this row
    return row["geometry"].distance(buoy_point)


def categorize_time_of_day(df, datetime_column):
    def get_time_of_day(time):
        if 5 <= time.hour < 12:
            return "Morning"
        elif 12 <= time.hour < 17:
            return "Afternoon"
        elif 17 <= time.hour < 21:
            return "Evening"
        else:
            return "Night"

    # Ensure the column is in datetime format
    df[datetime_column] = pd.to_datetime(df[datetime_column])

    # Apply the categorization function to the datetime column
    df["time_of_day"] = df[datetime_column].apply(lambda x: get_time_of_day(x))

    return df

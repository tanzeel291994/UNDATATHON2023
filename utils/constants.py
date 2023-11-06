import os, sys
from os.path import dirname as up

sys.path.append(os.path.abspath(os.path.join(up(__file__), os.pardir)))

from utils.helper import *

# DIRECTORY PATHS
ROOT_DIR = os.getcwd()
RAW_DATA_DIR = os.path.join(ROOT_DIR, "data", "raw")
PROCESSED_DATA_DIR = os.path.join(ROOT_DIR, "data", "processed")

# DATASET PATHS
GEAODATA_DATASET_PATH = os.path.join(RAW_DATA_DIR, "GeoData")
MEXICO_VESSEL_TRACKLINES_2011_GDB_PATH = os.path.join(
    GEAODATA_DATASET_PATH, "GulfofMexicoVesselTracklines2011/GulfofMexicoVesselTracklines2011.gdb"
)
SITE_MASTER_FILE_PATH = os.path.join(
    RAW_DATA_DIR,
    "cornell_products_detections_data_GoMexSpermWhale-Sites-Dates.csv",
)
WHALEPRESENCE_DATA_PATH = os.path.join(
    RAW_DATA_DIR,
    "cornell_products_detections_data_GoMexSpermWhalePresence-2010-2012.csv",
)
WHALEPRESENCE_COMPARE_DATA_PATH = os.path.join(
    RAW_DATA_DIR,
    "cornell_products_detections_data_GoMexSpermWhalePresence-2010-2012_CompareYear.csv",
)
SITE_MASTER_GEO_PATH = os.path.join(PROCESSED_DATA_DIR, "df_site_master_geo.geojson")
VESSEL_TRACKS_BOUNDED_GDF_PATH = os.path.join(
    PROCESSED_DATA_DIR, "vessel_tracks_bounded_gdf.geojson"
)
TRAIN_DATASET_PATH = os.path.join(PROCESSED_DATA_DIR, "train.csv")

# Define the coordinate reference systems
CRS_DEGREE = 'EPSG:4269'  # WGS84 Latitude/Longitude
CRS_METER = 'EPSG:3857'  # Web Mercator, uses meters #check this one

VESSEL_TYPE_MAPPING = {
    1: 'Reserved',
    2: 'Wing In Ground',
    3: 'Special Category',
    4: 'High-Speed Craft',
    5: 'Special Category',
    6: 'Passenger',
    7: 'Cargo',
    8: 'Tanker',
    9: 'Other',
    0: 'Cargo'
}

if __name__ == "__main__":
    paths = [
        ROOT_DIR,
        RAW_DATA_DIR,
        PROCESSED_DATA_DIR,
        GEAODATA_DATASET_PATH,
        MEXICO_VESSEL_TRACKLINES_2011_GDB_PATH,
        SITE_MASTER_FILE_PATH,
        WHALEPRESENCE_DATA_PATH,
    ]
    for path in paths:
        if os.path.exists(path):
            print("Path exists")
        else:
            print("Path does not exist")

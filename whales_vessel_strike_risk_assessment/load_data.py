import os, sys
from os.path import dirname as up

sys.path.append(os.path.abspath(os.path.join(up(__file__), os.pardir)))

from utils import *
from whales_vessel_strike_risk_assessment.data_reader import *

datareader = DataReader()

print("Loading datasets...")
mexico_vessel_tracklines_2011_gdf = datareader.read_from_gdb(
    MEXICO_VESSEL_TRACKLINES_2011_GDB_PATH
)

df_site_master = datareader.read_csv(SITE_MASTER_FILE_PATH)
df_whalepresence_data = datareader.read_csv(WHALEPRESENCE_DATA_PATH)
df_whalepresence_compare_data = datareader.read_csv(WHALEPRESENCE_COMPARE_DATA_PATH)

print("Loading datasets completed.")

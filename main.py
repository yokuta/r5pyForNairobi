import geopandas as gpd
from shapely.geometry import Point
import r5py
import datetime

#1 -1.289840, 36.788049
#2 -1.283096, 36.828749 50 min from 1
#3 -1.294131, 36.844353 40 min from 1
#4 -1.251295, 36.695004 78 min from 1
#5 -1.3803840, 36.6848173 113 min from 1

 

origin_coords = {"id": [1], "lat": [-1.289840], "lon": [36.788049]} 
destination_coords = {"id": [2], "lat": [-1.283096], "lon": [36.828749]}  

# Create GeoDataFrames for the origin and destination
origin = gpd.GeoDataFrame(
    origin_coords,
    geometry=[Point(lon, lat) for lon, lat in zip(origin_coords["lon"], origin_coords["lat"])],
    crs="EPSG:4326",
)

destination = gpd.GeoDataFrame(
    destination_coords,
    geometry=[Point(lon, lat) for lon, lat in zip(destination_coords["lon"], destination_coords["lat"])],
    crs="EPSG:4326",
)

# File paths for OSM and GTFS (update paths)
osm_file = "Data//nairobi.osm.pbf"
gtfs_files = [
    r"Data//gtfs.zip"
]

# Create the transport network
transport_network = r5py.TransportNetwork(osm_file, gtfs_files)

# Compute travel time
travel_time_matrix = r5py.TravelTimeMatrixComputer(
    transport_network,
    origins=origin,
    destinations=destination,
    departure=datetime.datetime(2020, 2, 11, 10, 30),  # Example: Departure time
    transport_modes=[r5py.TransportMode.TRANSIT, r5py.TransportMode.WALK],
).compute_travel_times()

# Print the travel time result
print("Estimated travel time (minutes):", travel_time_matrix.iloc[0]["travel_time"])
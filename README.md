# Wasabi Cloud Tutorial
This repository contains a Python script (main.py) that calculates travel times between two points in Nairobi, Kenya, using the r5py library. The script leverages OpenStreetMap (OSM) data and GTFS (General Transit Feed Specification) data to compute travel times via public transit and walking.

## Table of Contents

- [Introduction](#Introduction)
- [Requirements](#Requirements)
- [Installation](#Installation)
- [Usage](#Usage)
- [Data Sources](#Data_sources)


## Introduction
The script calculates the travel time between two geographic coordinates in Nairobi using the r5py library. It uses OSM data for the road network and GTFS data for public transit schedules. The example provided calculates the travel time between two points in Nairobi.

## Requirements
To run this script, you need the following:
  - Python 3.7 or higher
  - Required Python libraries:
      - r5py
      - geopandas
      - shapely
## Installation
1. Clone this repository:
  - `git clone https://github.com/yokuta/r5pyForNairobi.git`
  - `cd r5pyForNairobi`
2. Install the required Python libraries:
  - `pip install r5py geopandas shapely`
3. Download the necessary data files:
  - OSM data for Nairobi: Download OSM PBF [nairobi.osm.pbf](./Data/nairobi.osm.pbf)
  - GTFS data for Nairobi: Download GTFS (replace with the actual GTFS link) [gtfs.zip](./Data/gtfs.zip)
Place the downloaded files in the Data folder.


## Usage
1. Update the osm_file and gtfs_files paths in main.py to point to your OSM and GTFS files.
2. Modify the origin_coords and destination_coords dictionaries to specify your desired origin and destination coordinates.
3. Run the script:
  - python main.py
**Example Output**
The script will output the estimated travel time in minutes between the origin and destination points:
  - Estimated travel time (minutes): 50
## Data Sources
- OSM Data: Geofabrik Kenya [Download OSM PBF](https://download.geofabrik.de/africa/kenya.html)
  To create the osm file for Nairobi check this [repository](https://github.com/openstreetmap/osmosis/releases/tag/0.49.2) and this [webpage](https://wiki.openstreetmap.org/wiki/Osmosis/Quick_Install_(Windows)) to understand how to cut it. Also   you can download the one I uploaded, which is already cut.
- GTFS Data: Replace this with the actual source of your GTFS data. [GTDS Nairobi](https://hub.tumidata.org/dataset/gtfs-nairobi) 


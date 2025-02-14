# r5pyForNairobi
This repository contains a Python script (`main.py`) that calculates travel times between two points in Nairobi, Kenya, using the **r5py** library. The script leverages OpenStreetMap (OSM) data and GTFS (General Transit Feed Specification) data to compute travel times via public transit and walking. Also, it includes a Jupyter notebook (`matrixOriginDestination.ipynb`) that demonstrates how to perform an origin-destination matrix analysis using various Python libraries such as `geopandas`, `shapely`, `r5py`, and `datetime`. The notebook covers the following key steps:

## Table of Contents

- [Introduction](#Introduction)
- [Requirements](#Requirements)
- [Jupyter Notebook](#Jupyter-notebook)
- [main.py](#main.py)
  - [Installation](#Installation)
  - [Usage](#Usage)
  - [Data Sources](#Data_sources)


## Introduction
The script `main.py` calculates the travel time between two geographic coordinates in Nairobi using the r5py library. It uses OSM data for the road network and GTFS data for public transit schedules. The example provided calculates the travel time between two points in Nairobi, you have to introduce them with the coordiantes in the vairables origin_coords and destination_coords. The Jupyter notebook using coordinates, calculate the travel time between an origin and five destinations. Both the origin and the destinations will be selected by the person running the code through a dropdown map. Additionally, within the code, the user will be able to simulate the journey at different times and days, thus being able to test the variability of public transport efficiency, not only between different areas of the city but also according to the day of the week or the time of day. For the code, we have used the r5py library, which allows us to calculate the travel time between two coordinate points. This code can be used through a Jupyter notebook matrizOrigenr5py.ipynb. 


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

**Example Output:**

The script will output the estimated travel time in minutes between the origin and destination points:
  - Estimated travel time (minutes): 50
## Data Sources
- OSM Data: Geofabrik Kenya [Download OSM PBF](https://download.geofabrik.de/africa/kenya.html)
  To create the osm file for Nairobi check this [repository](https://github.com/openstreetmap/osmosis/releases/tag/0.49.2) and this [webpage](https://wiki.openstreetmap.org/wiki/Osmosis/Quick_Install_(Windows)) to understand how to cut it. Also   you can download the one I uploaded, which is already cut.
- GTFS Data: Replace this with the actual source of your GTFS data. [GTDS Nairobi](https://hub.tumidata.org/dataset/gtfs-nairobi) 


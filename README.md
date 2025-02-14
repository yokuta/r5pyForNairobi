# r5pyForNairobi
This repository contains a Python script (`main.py`) that calculates travel times between two points in Nairobi, Kenya, using the **r5py** library. The script leverages OpenStreetMap (OSM) data and GTFS (General Transit Feed Specification) data to compute travel times via public transit and walking. Also, it includes a Jupyter notebook (`matrixOriginDestination.ipynb`) that demonstrates how to perform an origin-destination matrix analysis using various Python libraries such as `geopandas`, `shapely`, `r5py`, and `datetime`. The notebook covers the following key steps:

## Table of Contents

- [Introduction](#Introduction)
- [Jupyter Notebook](#Jupyter-notebook)
- [main.py](#main-py)
  - [Requirements](#Requirements)
  - [Installation](#Installation)
  - [Usage](#Usage)
- [Data Sources](#Data-sources)


## Introduction
The script `main.py` calculates the travel time between two geographic coordinates in Nairobi using the r5py library. It uses OSM data for the road network and GTFS data for public transit schedules. The example provided calculates the travel time between two points in Nairobi, you have to introduce them with the coordiantes in the vairables origin_coords and destination_coords. The Jupyter notebook using coordinates, calculate the travel time between an origin and five destinations. Both the origin and the destinations will be selected by the person running the code through a dropdown map. Additionally, within the code, the user will be able to simulate the journey at different times and days, thus being able to test the variability of public transport efficiency, not only between different areas of the city but also according to the day of the week or the time of day. For the code, we have used the r5py library, which allows us to calculate the travel time between two coordinate points. This code can be used through a Jupyter notebook matrizOrigenr5py.ipynb. 

## Jupyter notebook
1. **First cell:** The first cell contains the libraries we need to install for our project:
2. **Second cell:** The second cell creates an interactive interface in Jupyter Notebook using Dash, and displays a map where the user can click to select origin and destination coordinates. In this case, the first coordinate we select will be the origin coordinate, from which all trips will start, and the rest of the coordinates will be the destinations of our trips. Thus, we will have one origin and five destinations. Finally, it saves the selected coordinates in a file called coords.txt. Once we have selected the 6 places, a message will appear indicating you can not select more destinations. This number can be changed in the code.
3. **Third cell:** The third cell is responsible for loading the selected coordinates from coord.txt and configuring the transport network for Nairobi using an osm.pbf file and GTFS data (gtfs.zip). It also calculates the travel times between the origin and the destinations using r5py.TravelTimeMatrixComputer and finally saves the results in a file called travel_timess.csv. We obtained the GTFS files from the Tumi Data website, where we can get the GTFS for Nairobi's public transport.
4. **Fourth cell:** In this cell, we load the travel_timess.csv file and sort the data by departure time. Finally, we generate a line graph showing how travel times vary according to the time and day on which the trip is made. With this cell, we wanted to demonstrate how arrival times at destinations vary depending on the time public transport is taken. The graph is [Imagenr5py](Imagenr5py.png). 
5. **Fifth cell:** In this cell, we created a boxplot of travel times for each destination, grouping them by destination rather than by hours or days. We found it interesting to see the variability of time between each destination.
6. **Sixth cell:** In this cell, we created a GIF image of the line graph we previously created. We simply animated the graph and saved it in GIF format within the same repository. The Gif created is [animation](animation.gif).
7. **Seventh cell:** The last cell contains code to visualize the points we selected for the work and the order in which we selected them.

## main.py
### Requirements
To run this script, you need the following:
  - Python 3.7 or higher
  - Required Python libraries:
      - r5py
      - geopandas
      - shapely
### Installation
1. Clone this repository:
  - `git clone https://github.com/yokuta/r5pyForNairobi.git`
  - `cd r5pyForNairobi`
2. Install the required Python libraries:
  - `pip install r5py geopandas shapely`
3. Download the necessary data files:
  - OSM data for Nairobi: Download OSM PBF [nairobi.osm.pbf](./Data/nairobi.osm.pbf)
  - GTFS data for Nairobi: Download GTFS (replace with the actual GTFS link) [gtfs.zip](./Data/gtfs.zip)
Place the downloaded files in the Data folder.


### Usage
1. Update the osm_file and gtfs_files paths in main.py to point to your OSM and GTFS files.
2. Modify the origin_coords and destination_coords dictionaries to specify your desired origin and destination coordinates.
3. Run the script:
  - python main.py

**Example Output:**

The script will output the estimated travel time in minutes between the origin and destination points:
  - Estimated travel time (minutes): 50

    
## Data Sources
- OSM Data: Geofabrik Kenya [Download OSM PBF](https://download.geofabrik.de/africa/kenya.html)
  To create the osm file for Nairobi check this [repository](https://github.com/openstreetmap/osmosis/releases/tag/0.49.2) and this [webpage](https://wiki.openstreetmap.org/wiki/Osmosis/Quick_Install_(Windows)) to understand how to cut it. Also   you can download the one I uploaded, which is already cut. Command I used with osmosis to cut the osm file:
    `osmosis --read-pbf kenya-latest.osm.pbf --bounding-box left=36.10 right=38.10 top=-1.00 bottom=-1.60 --write-pbf nairobi.osm.pbf`
- GTFS Data: Replace this with the actual source of your GTFS data. [GTDS Nairobi](https://hub.tumidata.org/dataset/gtfs-nairobi) 


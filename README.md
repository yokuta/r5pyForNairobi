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
Install the required Python libraries:

bash
Copy
pip install r5py geopandas shapely
Download the necessary data files:

OSM data for Nairobi: Download OSM PBF

GTFS data for Nairobi: Download GTFS (replace with the actual GTFS link)

Place the downloaded files in the Data folder.

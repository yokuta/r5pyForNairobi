import sys
import r5py

def create_transport_network(road_path, gtfs_files, message):
    result = r5py.TransportNetwork(road_path, gtfs_files)
    message.write('Info: Transport network created ', True)
    return result



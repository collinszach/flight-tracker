import pandas as pd
import requests
import csv
import datetime
import time
from opensky_api import OpenSkyApi

"""
https://github.com/openskynetwork/opensky-api/blob/master/python/opensky_api.py

"""

# api = OpenSkyApi()
# Airlines = pd.read_csv("./Data/Airlines.csv", names=["Airline ID", "Name", "Alias", "IATA", "ICAO", "Callsign", "Country", "Active"])
# Airports = pd.read_csv("./Data/Airports.csv", names=["Airport ID", "Name", "City", "Country", "IATA", "ICAO", "Latitude", "Longitude", "Altitude", "Timezone", "DST", "Tz database Timezone", "Type", "Source"])
# Countries = pd.read_csv("./Data/Countries.csv", names=["Name", "ISO_code", "dafif_code"])
# Planes = pd.read_csv("./Data/Planes.csv", names=["Name", "IATA", "ICAO"])
# Routes = pd.read_csv("./Data/Routes.csv", names=["Airline", "Airline ID", "Source Airport", "Source Airport ID", "Destination Ariport", "Destination Airport ID", "Codeshare", "Stops", "Equipment"])
# begin = datetime.datetime.now()
# end = begin + datetime.timedelta(hours=24)
# begin = begin.timestamp()
# end = end.timestamp()

# search_ICAO = Airports["ICAO"].loc[Airports["IATA"] == "IAD"].values
# print(api.get_arrivals_by_airport(airport=search_ICAO, begin=begin, end=end))

def getFlightData():

    Airlines = pd.read_csv("./Data/Airlines.csv", names=["Airline ID", "Name", "Alias", "IATA", "ICAO", "Callsign", "Country", "Active"]).to_dict("dict")
    Airports = pd.read_csv("./Data/Airports.csv", names=["Airport ID", "Name", "City", "Country", "IATA", "ICAO", "Latitude", "Longitude", "Altitude", "Timezone", "DST", "Tz database Timezone", "Type", "Source"]).to_dict("dict")
    Countries = pd.read_csv("./Data/Countries.csv", names=["Name", "ISO_code", "dafif_code"]).to_dict("dict")
    Planes = pd.read_csv("./Data/Planes.csv", names=["Name", "IATA", "ICAO"]).to_dict("dict")
    Routes = pd.read_csv("./Data/Routes.csv", names=["Airline", "Airline ID", "Source Airport", "Source Airport ID", "Destination Ariport", "Destination Airport ID", "Codeshare", "Stops", "Equipment"]).to_dict("dict")


    response = requests.get("https://opensky-network.org/api/states/all")
    if response.status_code == 200:
        data = response.json()
        
        states = data['states']

        flights = []

        for state in states:
            """
            https://openskynetwork.github.io/opensky-api/rest.html
            
            """
            flight = {
                "callsign": state[1],
                "origin_country": state[2],
                "time_position": state[3],
                "last_contact": state[4],
                "longitude": state[5],
                "latitude": state[6],
                "baro_altitude": state[7],
                "on_ground": state[8],
                "velocity": state[9],
                "true_track": state[10],
                "vertical_rate": state[11],
                "sensors": state[12],
                "geo_altitude": state[13],
                "squak": state[14],
                "spi": state[15],
                "position_source": state[16],
                "category": state[17]
            }
            flights.append(flight)
        
        df = pd.DataFrame(flights)
        print(f"Flight data:\n{df.head(1)}")



if __name__ == "__main__":
    getFlightData()

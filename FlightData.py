import pandas as pd
import requests
import csv
import datetime
import time
from opensky_api import OpenSkyApi

"""
https://github.com/openskynetwork/opensky-api/blob/master/python/opensky_api.py

"""

api = OpenSkyApi()
Airlines = pd.read_csv("./Data/Airlines.csv", names=["Airline ID", "Name", "Alias", "IATA", "ICAO", "Callsign", "Country", "Active"])
Airports = pd.read_csv("./Data/Airports.csv", names=["Airport ID", "Name", "City", "Country", "IATA", "ICAO", "Latitude", "Longitude", "Altitude", "Timezone", "DST", "Tz database Timezone", "Type", "Source"])
Countries = pd.read_csv("./Data/Countries.csv", names=["Name", "ISO_code", "dafif_code"])
Planes = pd.read_csv("./Data/Planes.csv", names=["Name", "IATA", "ICAO"])
Routes = pd.read_csv("./Data/Routes.csv", names=["Airline", "Airline ID", "Source Airport", "Source Airport ID", "Destination Ariport", "Destination Airport ID", "Codeshare", "Stops", "Equipment"])
begin = datetime.datetime.now()
end = begin + datetime.timedelta(hours=24)
begin = begin.timestamp()
end = end.timestamp()

search_ICAO = Airports["ICAO"].loc[Airports["IATA"] == "IAD"].values
print(api.get_arrivals_by_airport(airport=search_ICAO, begin=begin, end=end))

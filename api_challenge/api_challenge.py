#!/usr/bin/python3


import requests
import datetime
import reverse_geocoder as rg

URL = "http://api.open-notify.org/iss-now.json" 

def main():
    resp = requests.get(URL)

    respjson = resp.json()
    
    longtitude = respjson["iss_position"]["longitude"]
    latitude = respjson["iss_position"]["latitude"]
    epoch_time = respjson["timestamp"]
    date_time = datetime.datetime.fromtimestamp(epoch_time)
    location_tuple = (latitude, longtitude)
    location_data = rg.search(location_tuple)
    city = location_data[0]['name']
    country = location_data[0]['cc']
    #print(location_data)
    #print(location)
    #print(longtitude)
    #print(respjson)
    print("CURRENT LOCATION OF THE ISS:")
    print(f"Timestamp: {date_time}")
    print(f"Lon: {longtitude} ")
    print(f"Lat: {latitude}")
    print(f"City/Country: {city}, {country}")

if __name__ == "__main__" :
    main()

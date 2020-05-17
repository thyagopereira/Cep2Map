#coding: utf-8 
import pycep_correios
import googlemaps
import folium 
from IPython.display import display
gmaps_key = googlemaps.Client(key = "AIzaSyDuxEcCmAeZnCimhP-VZ7r4rco1CgXfe4k")

def main(cep):
    
    adress = pycep_correios.get_address_from_cep(cep)
    adress = format_adress(adress)
    print(adress)
    geocode_result  =  gmaps_key.geocode(adress)

    lat = geocode_result[0]["geometry"]["location"]["lat"]
    lng = geocode_result[0]["geometry"]["location"]["lng"]

    lat_long = [lat,lng]
    print(lat_long)
    geo_map = folium.Map(location= lat_long ,zoom_start= 600)
    folium.Marker(location= lat_long , popup= "location",tooltip="Go to Location").add_to(geo_map)
    display(geo_map)


def format_adress(adress):
    return  adress["logradouro"] + " - " + adress["bairro"] + " - " + adress["cidade"] + " - " + adress["uf"]



# print(str(lat) + str(lng))









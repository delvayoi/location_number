#pip install phonenumbers
import phonenumbers
import opencage
import folium
from myphone import number

from phonenumbers import geocoder

pepnumber=phonenumbers.parse(number)
location=geocoder.description_for_number(pepnumber, "en")
print(location)

from phonenumbers import carrier
service_pro=phonenumbers.parse(number)
print(carrier.name_for_number(service_pro, "en") )

#pip install opencage
from opencage.geocoder import OpenCageGeocode

key='b8f02251b27845769f839ec280714ac9'

geocoder=OpenCageGeocode(key)
query=str(location)
results=geocoder.geocode(query)
print(results)

lat=results[0]['geometry']['lat']
lng=results[0]['geometry']['lng']
print(lat,lng)

print(lat,lng)
#pip install folium

myMap=folium.Map(location=[lat, lng], zoom_start=8)
folium.Marker([lat, lng], popup=location).add_to(myMap)

myMap.save("mylocation.html")
import phonenumbers
from phonenumbers import geocoder
import folium
from opencage.geocoder import OpenCageGeocode
from phonenumbers import carrier

number = "[PHONE_NUMBER]"

pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber,"en")
print(location)


service_pro = phonenumbers.parse(number)
print(carrier.name_for_number(service_pro, "en"))

key = "[API_KEY]"

geocoder = OpenCageGeocode(key)
query = str(location)
result = geocoder.geocode(query)
# print(result)

lat = result[0]['geometry']['lat']
lng = result[0]['geometry']['lng']
print(lat,lng)

myMap = folium.Map(location = [lat,lng], zoom_start=9)
folium.Marker([lat,lng],popup=location).add_to(myMap)

myMap.save("myLocation.html")
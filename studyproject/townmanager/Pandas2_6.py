import googlemaps
import pandas as pd

my_key = "AIzaSyDy81EbO46BRSnX1DOgg_F84bhsdbku2z4"

maps = googlemaps.Client(key=my_key)

lat = []
lng = []

places = ['금천구청']

i = 0
for place in places:
    i = i + 1
    try:
        print(i, place)
        geo_location = maps.geocode(place)[0].get('geometry')
        lat.append(geo_location['location']['lat'])
        lng.append(geo_location['location']['lng'])
    except:
        lat.append('')
        lng.append('')
        print(i)

df = pd.DataFrame({'위도':lat, '경도': lng}, index = places)
print('\n')
print(df)
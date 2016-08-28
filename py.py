from googleplaces import GooglePlaces, types, lang
google_places = GooglePlaces('AIzaSyACV7BI2piZaMy-L-OHW2vpeEen1LP0QH8')

def get_places(lat_lng, types):
    ns = google_places.nearby_search(lat_lng=lat_lng, radius=500, types=types)
    return ns

lat_lng = {'lat': 12.90, 'lng': 77.54}
# lat_lng = {'lat': 12.9756947, 'lng': 77.6026579999999}

for i in [['restaurant'], ['school', 'university'], ['bank', 'atm']]:
    ns = get_places(lat_lng, i)
    print(i, len(ns.places))
    # for i in ns.places:
    #     print(i)

    print('\n'*3)

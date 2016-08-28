from django.shortcuts import render
from django.http import HttpResponse
from luminous.models import Location, User, LocationUser
from googleplaces import GooglePlaces, types, lang
import json
import random
# import math

def get_left_top(lat, lng):
    lat = round(float(lat), 2)
    lng = round(float(lng), 2)
    return lat, lng

def get_resources(lat, lng):
    google_places = GooglePlaces('AIzaSyACV7BI2piZaMy-L-OHW2vpeEen1LP0QH8')
    resources = {}
    ns = google_places.nearby_search(lat_lng={'lat': lat, 'lng': lng}, radius=500, types=['restaurant'])
    resources['food'] = int(len(ns.places) * round(random.random(), 1) * 10)
    ns = google_places.nearby_search(lat_lng={'lat': lat, 'lng': lng}, radius=500, types=['bank', 'atm'])
    resources['money'] = int(len(ns.places) * round(random.random(), 1) * 10)
    ns = google_places.nearby_search(lat_lng={'lat': lat, 'lng': lng}, radius=500, types=['school', 'university'])
    resources['skill'] = int(len(ns.places) * round(random.random(), 1) * 10)
    return json.dumps(resources)

def index(request):
    return HttpResponse("Hello, world. You're at the polls index!")

def get_owner(request):
    a = User.objects.all()
    for i in a:
        print(i.id)
    return HttpResponse(str({1: 2, 3: 4}))

def err(code):
    return json.dumps({'error': True, 'code': code})

def get_location(request):
    lat = request.GET['lat']
    lng = request.GET['lng']
    lat, lng = get_left_top(lat, lng)
    lt = str(lat) + ',' + str(lng)
    location = Location.objects.all().filter(left_top=lt)
    if len(location) == 0:
        location = Location(left_top=lt, resources=get_resources(lat, lng))
        location.save()
    else:
        location = location[0]
    return location

def get_user(request):
    userid = request.GET['userid']
    user = User.objects.all().filter(userid=userid)
    if len(user) == 0:
        user = User(userid=userid, resources=json.dumps({'skill':0, 'food':0, 'money': 0}))
        user.save()
    else:
        user = user[0]
    return user

def get_cost(location):
    resources = json.loads(location.resources)
    cost = {
        'skill': resources['skill'] / 2,
        'food': resources['food'] / 2,
        'money': resources['money'] / 2,
    }
    return cost

def isMine(request):
    location = get_location(request)
    user = get_user(request)
    location_user = LocationUser.objects.all().filter(location=location)
    if len(location_user) == 1:
        if len(location_user.filter(user=user)) == 1:
            k = json.dumps({'status': 'yours'})
        else:
            k = json.dumps({'status': 'occupied'})
    else:
        k = json.dumps({'status': 'unoccupied'})
    return HttpResponse(k)

def update_user_cost(user, cost):
    resources = json.loads(user.resources)
    resources['skill'] -= cost['skill']
    resources['money'] -= cost['money']
    resources['food'] -= cost['food']
    user.resources = json.dumps(resources)
    user.save()

def take_square(request):
    location = get_location(request)
    lat, lng = location.left_top.split(',')
    user = get_user(request)
    cost = get_cost(location)
    update_user_cost(user, cost)
    location_user = LocationUser(location=location, user=user)
    print(location_user)
    location_user.save()
    return HttpResponse(json.dumps({"lat": lat, "lng": lng}))

def mark_home(request):
    location = get_location(request)
    lat, lng = location.left_top.split(',')
    user = get_user(request)
    location_user = LocationUser(location=location, user=user)
    print(location_user)
    location_user.save()
    return HttpResponse(json.dumps({"lat": lat, "lng": lng}))

def get_can_buy(user, cost):
    resources = json.loads(user.resources)
    if resources['skill'] < cost['skill']:
        return False
    elif resources['food'] < cost['food']:
        return False
    elif resources['money'] < cost['money']:
        return False
    else:
        return True

def desc_square(request):
    location = get_location(request)
    user = get_user(request)
    cost = get_cost(location)
    can_buy = get_can_buy(user, cost)
    return HttpResponse(json.dumps({'resources': location.resources, 'cost': cost, 'can_buy': can_buy}))

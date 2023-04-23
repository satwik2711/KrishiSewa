from django.shortcuts import render
import googlemaps
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def calculate_transport_cost(request):
    origin = request.GET.get('origin')
    quantity = request.GET.get('quantity')
    destination_districts = settings.DISTRICTS


    gmaps = googlemaps.Client(key=settings.GOOGLE_MAPS_API_KEY)

    transport_cost = []


    for destination in destination_districts:
        if origin == destination:
            continue

        result = gmaps.distance_matrix(origins=origin + ', India', destinations=destination + ', India', mode='driving')
        distance = result['rows'][0]['elements'][0]['distance']['value']

        cost = distance * 0.001 * 0.4 * quantity

        
        transport_cost.append({
            'destination': destination,
            'cost': cost
        })


    return Response({'transport_cost': transport_cost})


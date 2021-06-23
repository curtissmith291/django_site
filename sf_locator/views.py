from django.shortcuts import render
# from geopy import distance
from geopy import Nominatim

# Create your views here.

def sf_view(request):
    return render(request, 'sf_locator.html')

def sf_results_view(request):
    try:
        street = request.GET['street'].strip()
        city = request.GET['city'].strip()
        state = request.GET['state'].strip()
        zip_code = request.GET['zip_code'].strip()

        address = street + ", " + city + ", " + state + ", " + zip_code

        geolocator = Nominatim(user_agent="my_user_agent")
        location = geolocator.geocode(address)
        long_address = location
        lat = location.latitude
        long = location.longitude
        return render(request, 'sf_locator_results.html', {'long_address': long_address, 'latitude': lat, 
            'longitude': long})
        # return render(request, 'sf_locator_results.html', {"complete_address": address})
    except:
        return render(request, 'sf_locator.html')
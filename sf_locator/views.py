from django.shortcuts import render

# Create your views here.

def sf_view(request):
    return render(request, 'sf_locator.html')

def sf_results_view(request):
    street = request.GET['street'].strip()
    city = request.GET['city'].strip()
    state = request.GET['state'].strip()
    zip_code = request.GET['zip_code'].strip()

    address = street + ", " + city + ", " + state + ", " + zip_code
    return render(request, 'sf_locator_results.html', {'complete_address': address})
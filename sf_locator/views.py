from django.shortcuts import render
# from geopy import distance
from geopy import Nominatim
from geopy import distance
import pandas as pd

# State abreviations; EPA API uses abbreviations, address has whole name
state_abbrev = {'Alabama': 'AL', 'Alaska': 'AK', 'Arizona': 'AZ', 'Arkansas': 'AR', 'California': 'CA',
    'Colorado': 'CO', 'Connecticut': 'CT', 'Delaware': 'DE', 'District of Columbia': 'DC', 
    'Florida': 'FL', 'Georgia': 'GA', 'Guam': 'GU', 'Hawaii': 'HI', 'Idaho': 'ID', 'Illinois': 'IL', 
    'Indiana': 'IN', 'Iowa': 'IA', 'Kansas': 'KS', 'Kentucky': 'KY', 'Louisiana': 'LA', 'Maine': 'ME',
    'Maryland': 'MD', 'Massachusetts': 'MA', 'Michigan': 'MI', 'Minnesota': 'MN', 'Mississippi': 'MS', 
    'Missouri': 'MO', 'Montana': 'MT', 'Nebraska': 'NE', 'Nevada': 'NV', 'New Hampshire': 'NH', 
    'New Jersey': 'NJ', 'New Mexico': 'NM', 'New York': 'NY', 'North Carolina': 'NC', 'North Dakota': 'ND',
    'Ohio': 'OH', 'Oklahoma': 'OK', 'Oregon': 'OR', 'Pennsylvania': 'PA', 'Puerto Rico': 'PR', 
    'Rhode Island': 'RI', 'South Carolina': 'SC', 'South Dakota': 'SD', 'Tennessee': 'TN', 'Texas': 'TX', 
    'Utah': 'UT', 'Vermont': 'VT', 'Virginia': 'VA', 'Washington': 'WA', 'West Virginia': 'WV', 
    'Wisconsin': 'WI', 'Wyoming': 'WY'
}

def distance_calc(row):
    '''
    This function returns the distance in miles between the address lat/long and the Superfund Site lat/long
    '''
    address_coords = (lat, long) 
    coord2 = (row['LATITUDE'], row['LONGITUDE'])
    return distance.distance(address_coords, coord2).miles

# Create your views here.

def sf_view(request):
    return render(request, 'sf_locator.html')

def sf_results_view(request):
    
    # sets the distacne to check to sites
    dist = 50
    global lat
    global long

    try:
        street = request.GET['street'].strip()
        city = request.GET['city'].strip()
        state = request.GET['state'].strip()
        zip_code = request.GET['zip_code'].strip()

        # Combines address parts into variable readable by geopy
        address = street + ", " + city + ", " + state + ", " + zip_code

        # Gets lat and long from input address
        geolocator = Nominatim(user_agent="my_user_agent")
        location = geolocator.geocode(address)
        lat = location.latitude
        long = location.longitude

        # converts long-form state to state abbreviation
        if state in state_abbrev.keys():
            state = state_abbrev[state]

        # opens csv of superfund site locations
        sf_df = pd.read_csv('resources/sf_sites_cleaned.csv')

        # Reduces df to only states matching user input
        sf_df = sf_df[sf_df["SITE_STATE"] == state]

        # Creates a new column with the distance in miles between the address and Superfund Sites
        # adding temp Dataframe prevents false positive SettingWithCopyWarning
        sf_sites_temp = sf_df.copy()
        sf_sites_temp['SITE_DISTANCE'] = sf_df.apply(distance_calc, axis=1)
        sf_df = sf_sites_temp.copy()

        # Creates new DataFrame with Superfund Sites within the specified distance from the address
        sf_sites_near = sf_df.loc[(sf_df['SITE_DISTANCE'] <= dist)]
        sf_sites_near = sf_sites_near.sort_values(by = ['SITE_DISTANCE'])

        # Adds sites within distance to a list
        site_list = sf_sites_near.loc[:, 'SITE_NAME'].tolist()
        # Adds URLs to list
        url_list = sf_sites_near.loc[:, 'SITE_URL'].tolist()
        # Adds distances to list; rounds to 1 decimal place
        distance_list = round(sf_sites_near.loc[:, 'SITE_DISTANCE'], 1).tolist()
        print(url_list)
        # Adjusts urls to be readable by html
        # link_class = 'sf_links'
        # for url in url_list:
        #     url_links = 'class="{}" href="{}">'.format(link_class, url)


        # Count of items sites
        count = len(site_list)

        context = {"list_of_sites": site_list, "count": count, "distance":dist, "url_list": url_list,
            "distance_list": distance_list}

        return render(request, 'sf_locator_results.html', context)

    except NameError as e:
        print(e)
        # make new html page for requests that don't work?
        return render(request, 'sf_locator.html')
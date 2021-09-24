from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Beers, Results
import plotly.express as px
import pandas as pd

# Create your views here.

def histogram():
    df = pd.DataFrame(list(Results.objects.all().values()))
    df.sort_values("rating", inplace=True, ascending=False)
    fig = px.histogram(df, x="rating")
    graph_2 = fig.to_html(full_html=False, default_height=600, default_width=1000)
    return(graph_2)

def main_view(request):

    df = pd.DataFrame(list(Results.objects.all().values()))

    # generate figure
    try:
        fig_df = pd.read_csv('assets/df_for_sunburst.csv')
    except:
        fig_df = pd.read_csv('/home/csmith/mysite/assets/df_for_sunburst.csv')

    fig = px.sunburst(fig_df, path=['total','main_class', 'subclass'], values='beer_count')

    graph_1 = fig.to_html(full_html=False, default_height=600, default_width=1000)


    graph_2 = histogram()

    context = {
        "graph_1": graph_1,
        "graph_2": graph_2
    }

    return render(request, 'beer_rec.html', context)

def search_results(request):
    if request.is_ajax():
        res = None
        beer = request.POST.get('beer')
        if(len(beer) >2):
            qs = Beers.objects.filter(beer_name__icontains=beer)
            if len(qs) > 0 and len(beer) > 0:
                data = []
                for pos in qs:
                    item = {
                        "pk":pos.pk,
                        "beer_name": pos.beer_name,
                        "brewery": pos.brewery
                    }
                    data.append(item)
                res = data
            else:
                res = 'No beers found...'

            return JsonResponse({'data': res})
        else:
            res = 'Keep typing...'
            return JsonResponse({'data': res})
    return JsonResponse({})

# def beer_detail_view(request):
#     # input_beer = request.GET['input_beer'].strip()
#     input_beer = request.GET['test_field'].strip()
#     working = False
#     if len(input_beer):
#         working = True
#     context = {"working":working, "input_beer":input_beer} 
#     return render(request, 'beer_rec_results.html', context)

def beer_detail_view(request, pk):
    obj = get_object_or_404(Beers, pk=pk)

    # Number of beers to recommend
    number_to_recommend = 10

    # Get variables for search
    search_name = obj.beer_name
    search_name_lower = search_name.lower()
    search_brewery = obj.brewery

    query_set = Results.objects.filter(beer_name__exact=search_name).filter(brewery__exact=search_brewery)
    for item in query_set:
        main_class = item.main_class
        subclass = item.subclass

    df = pd.DataFrame(list(Results.objects.all().values()))
    # Get dataframe of beers in same class and subclass
    df = df[(df["main_class"] == main_class) & (df["subclass"] == subclass)]
    df.sort_values("rating", inplace=True, ascending=False)
    recommended_beers = df.beer_name.to_list()
    recommended_brewery = df.brewery.to_list()

    df["beer_name_lower"] = df.beer_name.apply(lambda x: x.lower())

    in_abv = df.loc[
        (df["beer_name_lower"] == search_name_lower) & 
        (df["brewery"] == search_brewery)]["abv"].item()
    in_astringency = df.loc[
        (df["beer_name_lower"] == search_name_lower) & 
        (df["brewery"] == search_brewery)]["astringency"].item()
    in_body = df.loc[
        (df["beer_name_lower"] == search_name_lower) & 
        (df["brewery"] == search_brewery)]["body"].item()
    in_bitter = df.loc[
        (df["beer_name_lower"] == search_name_lower) & 
        (df["brewery"] == search_brewery)]["bitter"].item()
    in_sweet = df.loc[
        (df["beer_name_lower"] == search_name_lower) & 
        (df["brewery"] == search_brewery)]["sweet"].item()
    in_sour = df.loc[
        (df["beer_name_lower"] == search_name_lower) & 
        (df["brewery"] == search_brewery)]["sour"].item()
    in_fruits = df.loc[
        (df["beer_name_lower"] == search_name_lower) & 
        (df["brewery"] == search_brewery)]["fruits"].item()
    in_hoppy = df.loc[
        (df["beer_name_lower"] == search_name_lower) & 
        (df["brewery"] == search_brewery)]["hoppy"].item()
    in_spices = df.loc[
        (df["beer_name_lower"] == search_name_lower) & 
        (df["brewery"] == search_brewery)]["spices"].item()
    in_malty = df.loc[
        (df["beer_name_lower"] == search_name_lower) & 
        (df["brewery"] == search_brewery)]["malty"].item()
    in_salty = df.loc[
        (df["beer_name_lower"] == search_name_lower) & 
        (df["brewery"] == search_brewery)]["salty"].item()
    in_alcohol = df.loc[
        (df["beer_name_lower"] == search_name_lower) & 
        (df["brewery"] == search_brewery)]["alcohol"].item()

    def calc_differences(abv, astringency, body, bitter, sweet, sour, fruits, hoppy, spices, malty, salty, alcohol):
        value = (abv - in_abv) + (astringency - in_astringency) + (body - in_body) + (bitter - in_bitter) + (sweet - in_sweet) + (sour - in_sour) + (fruits - in_fruits) + (hoppy - in_hoppy) + (spices - in_spices) + (malty - in_malty)+ (salty - in_salty) + (alcohol - in_alcohol)
        value = abs(value)
        return value

    similar_results = []

    df["difference"] = df.apply(lambda row: calc_differences(row['abv'],
                row['astringency'], row['body'], row['bitter'],
                row['sweet'], row['sour'], row['fruits'], row['hoppy'],
                row['spices'], row['malty'], row['salty'], row['alcohol']), axis = 1)
    df.sort_values("difference", inplace=True, ascending=True)
    recommended_beers = df.beer_name.to_list()
    recommended_brewery = df.brewery.to_list()
    recommended_difference = df.difference.to_list()
    recommended_rating = df.rating.to_list()
    recommended_style = df.beer_style.to_list()

    if len(recommended_beers) > number_to_recommend:
        iterations = 10
    else: 
        iterations = len(recommended_beers)

    for index in range(0,iterations+1):
        if recommended_beers[index].lower() != search_name_lower:
            similar_results.append({
                "recommended_beers":recommended_beers[index],
                "recommended_brewery":recommended_brewery[index],
                "recommended_rating":recommended_rating[index],
                "recommended_style":recommended_style[index]
            })



    # generate figures
    # sunburst
    try:
        fig_df = pd.read_csv('assets/df_for_sunburst.csv')
    except:
        fig_df = pd.read_csv('/home/csmith/mysite/assets/df_for_sunburst.csv')

    fig = px.sunburst(fig_df, path=['total','main_class', 'subclass'], values='beer_count')

    graph_1 = fig.to_html(full_html=False, default_height=600, default_width=1000)

    graph_2 = histogram()


    context = {
        "beer_name": search_name,
        "brewery": search_brewery,
        "main_class": main_class,
        "subclass": subclass,
        "similar_results": similar_results,
        "iterations": iterations,
        "graph_1": graph_1,
        "graph_2": graph_2
    }

    return render(request, "beer_detail.html", {"context":context})
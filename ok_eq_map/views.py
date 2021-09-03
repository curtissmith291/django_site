from django.shortcuts import render
from plotly.offline import plot
from plotly.graph_objs import Scatter
import plotly.graph_objects as go
import pandas as pd

# def ok_eq(request):
#     x_data = [0,1,2,3]
#     y_data = [x**2 for x in x_data]
#     plot_div = plot([Scatter(x=x_data, y=y_data,
#                         mode='lines', name='test',
#                         opacity=0.8, marker_color='green')],
#                output_type='div')
#     return render(request, "ok_eq.html", context={'plot_div': plot_div})


def ok_eq(request):
    eq_df = pd.read_csv('assets/eq_for_figs.csv')

    eq_2006 = eq_df[eq_df["year"] == 2006]
    eq_2007 = eq_df[eq_df["year"] == 2007]
    eq_2008 = eq_df[eq_df["year"] == 2008]
    eq_2009 = eq_df[eq_df["year"] == 2009]
    eq_2010 = eq_df[eq_df["year"] == 2010]
    eq_2011 = eq_df[eq_df["year"] == 2011]
    eq_2012 = eq_df[eq_df["year"] == 2012]
    eq_2013 = eq_df[eq_df["year"] == 2013]
    eq_2014 = eq_df[eq_df["year"] == 2014]
    eq_2015 = eq_df[eq_df["year"] == 2015]
    eq_2016 = eq_df[eq_df["year"] == 2016]
    eq_2017 = eq_df[eq_df["year"] == 2017]
    eq_2018 = eq_df[eq_df["year"] == 2018]
    eq_2019 = eq_df[eq_df["year"] == 2019]
    eq_2020 = eq_df[eq_df["year"] == 2020]
    eq_2021 = eq_df[eq_df["year"] == 2021]

    fig=go.Figure()

    fig.add_trace(go.Scattermapbox(
        lat=eq_2006.latitude, 
        lon=eq_2006.longitude,
        name = "2006",
        text = eq_2006['place'],
        visible = True,
        mode = 'markers',
        hovertemplate = "Magnitude: %{marker.color} </b><br>" + "Location: %{text}<br>",
        marker = dict(
            size = eq_2006.mag**2.2,
            opacity = 0.8,
            colorscale = 'jet',
            color = eq_2006.mag,
            cmin = 3,
            cmax = 6,
            colorbar_title="Magnitude"
        )))

    fig.add_trace(go.Scattermapbox(
        lat=eq_2007.latitude, 
        lon=eq_2007.longitude,
        name = "2007",
        text = eq_2007['place'],
        visible = False,
        mode = 'markers',
        hovertemplate = "Magnitude: %{marker.color} </b><br>" + "Location: %{text}<br>",
        marker = dict(
            size = eq_2007.mag**2.2,
            opacity = 0.8,
            colorscale = 'jet',
            color = eq_2007.mag,
            cmin = 3,
            cmax = 6,
            colorbar_title="Magnitude"
        )))

    fig.add_trace(go.Scattermapbox(
        lat=eq_2008.latitude, 
        lon=eq_2008.longitude,
        name = "2008",
        text = eq_2008['place'],
        visible = False,
        mode = 'markers',
        hovertemplate = "Magnitude: %{marker.color} </b><br>" + "Location: %{text}<br>",
        marker = dict(
            size = eq_2008.mag**2.2,
            opacity = 0.8,
            colorscale = 'jet',
            color = eq_2008.mag,
            cmin = 3,
            cmax = 6,
            colorbar_title="Magnitude"
        )))

    fig.add_trace(go.Scattermapbox(
        lat=eq_2009.latitude, 
        lon=eq_2009.longitude,
        name = "2009",
        text = eq_2009['place'],
        visible = False,
        mode = 'markers',
        hovertemplate = "Magnitude: %{marker.color} </b><br>" + "Location: %{text}<br>",
        marker = dict(
            size = eq_2009.mag**2.2,
            opacity = 0.8,
            colorscale = 'jet',
            color = eq_2009.mag,
            cmin = 3,
            cmax = 6,
            colorbar_title="Magnitude"
        )))

    fig.add_trace(go.Scattermapbox(
        lat=eq_2010.latitude, 
        lon=eq_2010.longitude,
        name = "2010",
        text = eq_2010['place'],
        visible = False,
        mode = 'markers',
        hovertemplate = "Magnitude: %{marker.color} </b><br>" + "Location: %{text}<br>",
        marker = dict(
            size = eq_2010.mag**2.2,
            opacity = 0.8,
            colorscale = 'jet',
            color = eq_2010.mag,
            cmin = 3,
            cmax = 6,
            colorbar_title="Magnitude"
        )))

    fig.add_trace(go.Scattermapbox(
        lat=eq_2011.latitude, 
        lon=eq_2011.longitude,
        name = "2011",
        text = eq_2011['place'],
        visible = False,
        mode = 'markers',
        hovertemplate = "Magnitude: %{marker.color} </b><br>" + "Location: %{text}<br>",
        marker = dict(
            size = eq_2011.mag**2.2,
            opacity = 0.8,
            colorscale = 'jet',
            color = eq_2011.mag,
            cmin = 3,
            cmax = 6,
            colorbar_title="Magnitude"
        )))

    fig.add_trace(go.Scattermapbox(
        lat=eq_2012.latitude, 
        lon=eq_2012.longitude,
        name = "2012",
        text = eq_2012['place'],
        visible = False,
        mode = 'markers',
        hovertemplate = "Magnitude: %{marker.color} </b><br>" + "Location: %{text}<br>",
        marker = dict(
            size = eq_2012.mag**2.2,
            opacity = 0.8,
            colorscale = 'jet',
            color = eq_2012.mag,
            cmin = 3,
            cmax = 6,
            colorbar_title="Magnitude"
        )))

    fig.add_trace(go.Scattermapbox(
        lat=eq_2013.latitude, 
        lon=eq_2013.longitude,
        name = "2013",
        text = eq_2013['place'],
        visible = False,
        mode = 'markers',
        hovertemplate = "Magnitude: %{marker.color} </b><br>" + "Location: %{text}<br>",
        marker = dict(
            size = eq_2013.mag**2.2,
            opacity = 0.8,
            colorscale = 'jet',
            color = eq_2013.mag,
            cmin = 3,
            cmax = 6,
            colorbar_title="Magnitude"
        )))

    fig.add_trace(go.Scattermapbox(
        lat=eq_2014.latitude, 
        lon=eq_2014.longitude,
        name = "2014",
        text = eq_2014['place'],
        visible = False,
        mode = 'markers',
        hovertemplate = "Magnitude: %{marker.color} </b><br>" + "Location: %{text}<br>",
        marker = dict(
            size = eq_2014.mag**2.2,
            opacity = 0.8,
            colorscale = 'jet',
            color = eq_2014.mag,
            cmin = 3,
            cmax = 6,
            colorbar_title="Magnitude"
        )))

    fig.add_trace(go.Scattermapbox(
        lat=eq_2015.latitude, 
        lon=eq_2015.longitude,
        name = "2015",
        text = eq_2015['place'],
        visible = False,
        mode = 'markers',
        hovertemplate = "Magnitude: %{marker.color} </b><br>" + "Location: %{text}<br>",
        marker = dict(
            size = eq_2015.mag**2.2,
            opacity = 0.8,
            colorscale = 'jet',
            color = eq_2015.mag,
            cmin = 3,
            cmax = 6,
            colorbar_title="Magnitude"
        )))

    fig.add_trace(go.Scattermapbox(
        lat=eq_2016.latitude, 
        lon=eq_2016.longitude,
        name = "2016",
        text = eq_2016['place'],
        visible = False,
        mode = 'markers',
        hovertemplate = "Magnitude: %{marker.color} </b><br>" + "Location: %{text}<br>",
        marker = dict(
            size = eq_2016.mag**2.2,
            opacity = 0.8,
            colorscale = 'jet',
            color = eq_2016.mag,
            cmin = 3,
            cmax = 6,
            colorbar_title="Magnitude"
        )))

    fig.add_trace(go.Scattermapbox(
        lat=eq_2017.latitude, 
        lon=eq_2017.longitude,
        name = "2017",
        text = eq_2017['place'],
        visible = False,
        mode = 'markers',
        hovertemplate = "Magnitude: %{marker.color} </b><br>" + "Location: %{text}<br>",
        marker = dict(
            size = eq_2017.mag**2.2,
            opacity = 0.8,
            colorscale = 'jet',
            color = eq_2017.mag,
            cmin = 3,
            cmax = 6,
            colorbar_title="Magnitude"
        )))

    fig.add_trace(go.Scattermapbox(
        lat=eq_2018.latitude, 
        lon=eq_2018.longitude,
        name = "2018",
        text = eq_2018['place'],
        visible = False,
        mode = 'markers',
        hovertemplate = "Magnitude: %{marker.color} </b><br>" + "Location: %{text}<br>",
        marker = dict(
            size = eq_2018.mag**2.2,
            opacity = 0.8,
            colorscale = 'jet',
            color = eq_2018.mag,
            cmin = 3,
            cmax = 6,
            colorbar_title="Magnitude"
        )))

    fig.add_trace(go.Scattermapbox(
        lat=eq_2019.latitude, 
        lon=eq_2019.longitude,
        name = "2019",
        text = eq_2019['place'],
        visible = False,
        mode = 'markers',
        hovertemplate = "Magnitude: %{marker.color} </b><br>" + "Location: %{text}<br>",
        marker = dict(
            size = eq_2019.mag**2.2,
            opacity = 0.8,
            colorscale = 'jet',
            color = eq_2019.mag,
            cmin = 3,
            cmax = 6,
            colorbar_title="Magnitude"
        )))

    fig.add_trace(go.Scattermapbox(
        lat=eq_2020.latitude, 
        lon=eq_2020.longitude,
        name = "2020",
        text = eq_2020['place'],
        visible = False,
        mode = 'markers',
        hovertemplate = "Magnitude: %{marker.color} </b><br>" + "Location: %{text}<br>",
        marker = dict(
            size = eq_2020.mag**2.2,
            opacity = 0.8,
            colorscale = 'jet',
            color = eq_2020.mag,
            cmin = 3,
            cmax = 6,
            colorbar_title="Magnitude"
        )))

    fig.add_trace(go.Scattermapbox(
        lat=eq_2021.latitude, 
        lon=eq_2021.longitude,
        name = "2021 (Through July)",
        text = eq_2020['place'],
        visible = False,
        mode = 'markers',
        hovertemplate = "Magnitude: %{marker.color} </b><br>" + "Location: %{text}<br>",
        marker = dict(
            size = eq_2021.mag**2.2,
            opacity = 0.8,
            colorscale = 'jet',
            color = eq_2021.mag,
            cmin = 3,
            cmax = 6,
            colorbar_title="Magnitude"
        )))

    fig.update_layout(
        updatemenus=[
            dict(
                buttons=list([
                    dict(
                        args=[{"visible": [True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]}],
                        label="2006",
                        method="update"
                    ),
                    dict(
                        args=[{"visible": [False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False]}],
                        label="2007",
                        method="update"
                    ),
                    dict(
                        args=[{"visible": [False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False]}],
                        label="2008",
                        method="update"
                    ),
                    dict(
                        args=[{"visible": [False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False]}],
                        label="2009",
                        method="update"
                    ),
                    dict(
                        args=[{"visible": [False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False]}],
                        label="2010",
                        method="update"
                    ),
                    dict(
                        args=[{"visible": [False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False]}],
                        label="2011",
                        method="update"
                    ),
                    dict(
                        args=[{"visible": [False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False]}],
                        label="2012",
                        method="update"
                    ),
                    dict(
                        args=[{"visible": [False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False]}],
                        label="2013",
                        method="update"
                    ),
                    dict(
                        args=[{"visible": [False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False]}],
                        label="2014",
                        method="update"
                    ),
                    dict(
                        args=[{"visible": [False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False]}],
                        label="2015",
                        method="update"
                    ),
                    dict(
                        args=[{"visible": [False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False]}],
                        label="2016",
                        method="update"
                    ),
                    dict(
                        args=[{"visible": [False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False]}],
                        label="2017",
                        method="update"
                    ),
                    dict(
                        args=[{"visible": [False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False]}],
                        label="2018",
                        method="update"
                    ),
                    dict(
                        args=[{"visible": [False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False]}],
                        label="2019",
                        method="update"
                    ),
                    dict(
                        args=[{"visible": [False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False]}],
                        label="2020",
                        method="update"
                    ),
                    dict(
                        args=[{"visible": [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True]}],
                        label="2021",
                        method="update"
                    ),
                ]),
                direction="down",

            )])

    fig.update_layout(
        title = 'M>3 Earthquakes in Oklahoma',
        mapbox = {
            'style': "carto-positron", 
            'zoom': 5.5,
            'center':dict(lat=35.5, lon=-97.4)
        },
        legend=dict(
            x=0,
            y=1,
            traceorder="normal",
            orientation="h",
            font=dict(
                family="sans-serif",
                size=12,
                color="black",
            ))),

    graph = fig.to_html(full_html=False, default_height=600, default_width=1000)
    context = {'graph': graph}
    # response = render(request, 'ok_eq.html', context)
    return render(request, 'ok_eq.html', context)
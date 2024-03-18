#Ghana Map Representaion Region Locations
import folium
import pandas as pd


data = pd.read_csv("ghana.txt")
latitude = list(data['Lat'])
longitude = list(data['Long'])
region = list(data['Regions'])


def Regioncolors(regionColors):
    if regionColors == "Ahafo Region":
        return 'green'
    if regionColors == "Ashanti Region":
        return 'blue'
    if regionColors == "Bono East Region":
        return 'black'
    if regionColors == "Bono Region":
        return 'lightblue'
    if regionColors == "Central Region":
        return 'purple'
    if regionColors == "Eastern Region":
        return 'orange'
    if regionColors == "Greater Accra Region":
        return 'lightred'
    if regionColors == "North East Region":
        return 'darkblue'
    if regionColors == "Northern Region":
        return 'lightgreen'
    if regionColors == "Oti Region":
        return 'gray'
    if regionColors == "Savannah Region":
        return 'darkgreen'
    if regionColors == "Upper West Region":
        return 'cadetblue'
    if regionColors == "Volta Region":
        return 'lightgray'
    if regionColors == "Western North Region":
        return 'red'    
    if regionColors == "Western Region":
        return 'darkpurple'
        
         


#assigning folium.Map to mapObj to create mapObj Object 
#titles= 'Mapbox Bright',attr= '<a href="https://github.com/kananep">GhanaMap</a> contributors'
mapObj = folium.Map(location=[6.916885199407648,-2.5350966], zoom_start=6.4,
                    titles = 'Stamen Toner',attr= '<a href="https://github.com/kananep">GhanaMap</a> contributors')


fg_location = folium.FeatureGroup(name='Ghana Map')

#for locationCordinates in [[6.694764 ,-1.631116],[9.400580, -0.836342]]:
for lt,ln,reg in zip(latitude,longitude,region):    
    fg_location.add_child(folium.Marker(location=[lt, ln], popup=reg,icon=folium.Icon(color=Regioncolors(reg))))
    #fg.add_child(folium.Marker(location=[lt, ln],popup=reg))
#fg.add_child(folium.Marker(location=[lt,ln],popup= reg, icon=folium.Icon(color=Regioncolors(reg))) )


fg_population = folium.FeatureGroup(name='Population')
fg_population.add_child(folium.GeoJson(data=open('world.json', 'r',encoding='utf-8-sig').read(),
                            style_function=lambda x: {'fillColor':'yellow' if x['properties']['POP2005'] <= 2253501 
                                                      else "green" if 2253501 <= x['properties']['POP2005'] < 10000000 else'red'}))
    


mapObj.add_child(fg_location)
mapObj.add_child(fg_population)
mapObj.add_child(folium.LayerControl())

mapObj.save('GhanaMap.html')
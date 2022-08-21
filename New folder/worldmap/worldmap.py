# pip install folium
import folium


phone_map = folium.Map()

# top five smart phone companies in the market location
companies = [
    {'loc':[37.4970, 127.0266], 'label': 'Samsung:22%'},
    {'loc':[22.5431, 114.0579], 'label': 'Huawei:14%'},
    {'loc':[39.9600, 116.2983], 'label': 'Xiaomi:13%'},
    {'loc':[37.3318, -122.0311], 'label': 'Apple:11%'},
    {'loc':[23.0207, 113.7518], 'label': 'Oppo:11%'}
    ] 


# adding markers to the Map
for company in companies:
    marker = folium.Marker(location=company['loc'], popup=company['label'])
    marker.add_to(phone_map)
    
# main map variable
phone_map
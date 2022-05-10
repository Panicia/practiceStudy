import shapefile
import json

sf = shapefile.Reader('ne_10m_admin_0_map_units.shp')
geoj = sf.__geo_interface__['type']
print(geoj)
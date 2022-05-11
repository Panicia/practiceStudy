import shapefile
import json


#myshp = open("ne_10m_admin_0_map_units.shp", "rb")
#mydbf = open("ne_10m_admin_0_map_units.dbf", "rb")
#sf = shapefile.Reader(shp=myshp,dbf=mydbf)

#sf = shapefile.Reader(shp = 'ne_10m_admin_0_map_units.shp', dbf = 'ne_10m_admin_0_map_units.dbf',encoding = "utf-8")
#with shapefile.Reader('ne_10m_admin_0_map_units',encoding = "utf-8") as shp:
#with shapefile.Reader(shp = 'ne_10m_admin_0_map_units', dbf = 'ne_10m_admin_0_map_units',encoding = "utf-8") as shp:
with shapefile.Reader('ne_10m_admin_0_map_units') as shp:
    data = shp.shapes()
    fields = shp.fields
    for i in range(shp.numRecords):
        print(shp.record(i))
    pass
#geoj = sf.__geo_interface__.shp
#sf.__geo_interface__['type']#
#print(geoj)
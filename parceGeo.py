import re
class myGeom():
    def __init__(self, path = 'fileGeom_from_Points_adm0_a3.txt'):
        self._path = path
    def parceAll(self):
        features = []
        self.counties = {
                            'type': 'FeatureCollection',
                            'features': features
                        }
        with open(self._path, 'r', encoding = 'utf-8') as f:
            count = 0
            for line in f:
                pieces = line.split('=')
                name = pieces[0]
                coordinates = pieces[1]
                coordinates_array = []
                k1 = 0 # 0 - nothing wr, 1 - globalpoly wr, 2 - multipoly wr, 3 - investedpoly wr, 4 - point wr, 5 - coord wr
                coord = ''
                point = []
                inv_poly = []
                multi_poly = []
                for i in coordinates:
                    if i == '[' and k1 == 0:
                        k1 = 1
                    elif i == '[' and k1 == 1:
                        k1 = 2
                    elif i == '[' and k1 == 2:
                        k1 = 3
                    elif i == '<':
                        k1 = 4
                    elif i == '>' and k1 == 4:
                        k1 = 3
                        inv_poly.append(point)
                        point = []
                    elif i == ']' and k1 == 3:
                        k1 = 2
                        multi_poly.append(inv_poly)
                        inv_poly = []
                    elif i == ']' and k1 == 2:
                        k1 = 1
                        coordinates_array.append(multi_poly)
                        multi_poly = []
                    elif i == ']' and k1 == 1:
                        k1 = 0
                        break
                    elif re.fullmatch(r'\d|-|\.', i) and k1 == 4:
                        k1 = 5
                        coord += i
                    elif re.fullmatch(r'\d|-|\.', i) and k1 == 5:
                        coord += i
                    elif not re.fullmatch(r'\d|-|\.', i) and k1 == 5:
                        k1 = 4 
                        point.append(float(coord))
                        coord = ''
                    
                new_feature = {
                                'type': 'Feature',
                                'properties': {
                                                'NAME': name,
                                                'attribute': None
                                              },
                                'geometry': {
                                                'type': 'MultiPolygon',
                                                'coordinates': coordinates_array
                                            },
                                'id': name
                              }
                features.append(new_feature)
                count += 1
                print(count)

#pg = myGeom()
#pg.parceAll()

#print(pg.counties['features'][10]['geometry']['coordinates'][0])
#print(len(pg.counties['features'][10]['geometry']['coordinates']))
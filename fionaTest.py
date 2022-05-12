import fiona
import pandas as pd
class fionaTests():
    def __init__(self, path = 'ne_10m_admin_0_map_units.dbf'):
        features = []
        self.counties = {
                            'type': 'FeatureCollection',
                            'features': features
                        }
        with fiona.open("ne_10m_admin_0_map_units.dbf") as f:
            for line in f:
                features.append(line)
        '''for i in features:
            if i['properties']['adm0_a3'] == 'ZWE':
                print(i)'''
    def getData(self):
        return self.counties
    def findDubles(self):
        doubles = []
        for i in self.counties['features']:
            for j in doubles:
                if i['properties']['adm0_a3'] == j['name']:

                    j["id"].append(int(i['id']))
                    j["numDoubs"] += 1
                    break
            else:
                new_lib = {
                            'name': i['properties']['adm0_a3'],
                            'id': [int(i["id"])],
                            'numDoubs': 1
                            }
                doubles.append(new_lib)

        res = [i for i in doubles if i["numDoubs"] > 1]
        return res

#df = fionaTests()
#print(pd.DataFrame(data = df.findDubles()))
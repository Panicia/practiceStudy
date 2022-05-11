import fiona
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
        for i in features:
            print(i['id'], i['properties']['admin'], i['properties']['adm0_a3'])
    def getData(self):
        return self.counties

df = fionaTests()
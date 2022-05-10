from parceVac import parceVac as pV
from parceGeo import myGeom as pG

pv = pV()
pv.parceAll()
pg = pG('fileGeom_adm0_a3.txt')
pg.parceAll()

names = pv.getDatalistFromAll('iso_code', 'start')

print('location ' + str(len(names)))
print('names ' + str(len(pg.features['features'])))
count = 0
didnt_find = []
for i in range(0, len(names) - 1):
    for j in range(0, len(pg.features['features']) - 1):
        if names[i] == pg.features['features'][j]['properties']['NAME']:
            count += 1
            break
        elif j == len(pg.features['features']) - 2:
            didnt_find.append(names[i])
print('number of overlaps: ' + str(count))


import math
import pandas as pd
df = pd.read_csv
class parceVac():
    def __init__(self, path = 'country_vaccinations.csv') -> None:
        self.path = path
        self.data = pd.read_csv(path)
    def getDataListPerCountry(self, location, name):
        datalist = []
        for i in range(0, len(self.data[name]) - 1):
            if self.data['country'][i] == location:
                datalist.append(self.data[name][i])
        return datalist

    def getDatalistFromAll(self, name, point = 'start', find_data_if_none = True):
        datalist = []
        if name == 'country' or name == 'iso_code':
            for i in range(0, len(self.data[name])):
                if i != 0:
                        if self.data['country'][i - 1] != self.data['country'][i]:
                            if self.data[name][i] == 'SSD':
                                datalist.append('SDS')
                            else:
                                datalist.append(self.data[name][i])
                else:
                    datalist.append(self.data[name][i])
        else:   
            for i in range(0, len(self.data[name])):
                if point == 'start':
                    if i != 0:
                        if self.data['country'][i - 1] != self.data['country'][i]:
                            if find_data_if_none:
                                if not math.isnan(self.data[name][i]):
                                    datalist.append(self.data[name][i])
                                else:
                                    k = 1
                                    while self.data['country'][i + k] == self.data['country'][i]:
                                        if not math.isnan(self.data[name][i + k]):
                                            datalist.append(self.data[name][i + k])
                                            break
                                        if i + k == len(self.data[name]) - 1:
                                            datalist.append(None)
                                            break
                                        k += 1
                            else:
                                datalist.append(self.data[name][i])
                    else:
                        if find_data_if_none:
                            if not math.isnan(self.data[name][i]):
                                    datalist.append(self.data[name][i])
                            else:
                                k = 1
                                while self.data['country'][i + k] == self.data['country'][i]:
                                    if not math.isnan(self.data[name][i + k]):
                                        datalist.append(self.data[name][i + k])
                                        break
                                    if i + k == len(self.data[name]) - 1:
                                        datalist.append(None)
                                        break
                                    k += 1
                        else:
                            datalist.append(self.data[name][i])
                elif point == 'end':
                    if i != len(self.data[name]) - 1:
                        if self.data['country'][i + 1] != self.data['country'][i]:
                            if find_data_if_none:
                                if not math.isnan(self.data[name][i]):
                                    datalist.append(self.data[name][i])
                                else:
                                    k = 1
                                    while self.data['country'][i - k] == self.data['country'][i]:
                                        if not math.isnan(self.data[name][i - k]):
                                            datalist.append(self.data[name][i - k])
                                            break
                                        if i + k == len(self.data[name]) - 1:
                                            datalist.append(None)
                                            break
                                        k += 1
                            else:
                                datalist.append(self.data[name][i])
                    else:
                        if find_data_if_none:
                            if not math.isnan(self.data[name][i]):
                                    datalist.append(self.data[name][i])
                            else:
                                k = 1
                                while self.data['country'][i - k] == self.data['country'][i]:
                                    if not math.isnan(self.data[name][i - k]):
                                        datalist.append(self.data[name][i - k])
                                        break
                                    if i + k == len(self.data[name]) - 1:
                                        datalist.append(None)
                                        break
                                    k += 1
                        else:
                            datalist.append(self.data[name][i])
        return datalist

#parser = parceVac('vaccinations.txt')
#print(parser.getDatalistFromAll('location', 'end'))
'''for i in parser.getDatalistFromAll('iso_code', 'end'):
    if i == 'NOR':
        print('wow')'''

    
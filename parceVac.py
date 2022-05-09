import re

class parseVac():
    def __init__(self, path) -> None:
        self.path = path
    def parseAll(self):
        self.location = []
        self.iso_code = []
        self.date = []
        self.total_vaccinations = []
        self.people_vaccinated = []
        self.people_fully_vaccinated = []
        self.total_boosters = []
        self.daily_vaccinations_raw = []
        self.daily_vaccinations = []
        self.total_vaccinations_per_hundred = []
        self.people_vaccinated_per_hundred = []
        self.people_fully_vaccinated_per_hundred = []
        self.total_boosters_per_hundred = []
        self.daily_vaccinations_per_million = []
        self.daily_people_vaccinated = []
        self.daily_people_vaccinated_per_hundred = []

        self.data = {
                     'location': self.location, 'iso_code': self.iso_code, 'date': self.date,
                     'total_vaccinations': self.total_vaccinations, 'people_vaccinated': self.people_vaccinated,
                     'people_fully_vaccinated': self.people_fully_vaccinated, 'total_boosters': self.total_boosters,
                     'daily_vaccinations_raw': self.daily_vaccinations_raw, 'daily_vaccinations': self.daily_vaccinations,
                     'total_vaccinations_per_hundred': self.total_vaccinations_per_hundred, 'people_vaccinated_per_hundred': self.people_vaccinated_per_hundred,
                     'people_fully_vaccinated_per_hundred': self.people_fully_vaccinated_per_hundred, 'total_boosters_per_hundred': self.total_boosters_per_hundred,
                     'daily_vaccinations_per_million': self.daily_vaccinations_per_million, 'daily_people_vaccinated': self.daily_people_vaccinated,
                     'daily_people_vaccinated_per_hundred': self.daily_people_vaccinated_per_hundred
                    }

        with open(self.path, 'r', encoding = 'utf-8') as f:
            i = 0
            for line in f:
                if i != 0:
                    pieces = re.split(r',|\n', line)
                    k = 0
                    for j in self.data:
                        if j != 'location' and j != 'iso_code' and j != 'date':
                            if pieces[k] == '':
                                self.data[j].append(None)
                            else:
                                self.data[j].append(float(pieces[k]))
                        else:
                            self.data[j].append(pieces[k])
                        k += 1
                i += 1
    def getDataListPerCountry(self, location, name):
        datalist = []
        for i in range(0, len(self.data[name]) - 1):
            if self.data['location'][i] == location:
                datalist.append(self.data[name][i])
        return datalist

    def getDatalistFromAll(self, name, point = 'start', find_data_if_none = True):
        datalist = []
        for i in range(0, len(self.data[name]) - 1):
            if point == 'start':
                if i != 0:
                    if self.data['location'][i - 1] != self.data['location'][i]:
                        if find_data_if_none:
                            if not self.data[name][i] is None:
                                datalist.append(self.data[name][i])
                            else:
                                k = 1
                                while self.data['location'][i + k] == self.data['location'][i]:
                                    if not self.data[name][i + k] is None:
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
                        if not self.data[name][i] is None:
                                datalist.append(self.data[name][i])
                        else:
                            k = 1
                            while self.data['location'][i + k] == self.data['location'][i]:
                                if not self.data[name][i + k] is None:
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
                    if self.data['location'][i + 1] != self.data['location'][i]:
                        if find_data_if_none:
                            if not self.data[name][i] is None:
                                datalist.append(self.data[name][i])
                            else:
                                k = 1
                                while self.data['location'][i - k] == self.data['location'][i]:
                                    if not self.data[name][i - k] is None:
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
                        if not self.data[name][i] is None:
                                datalist.append(self.data[name][i])
                        else:
                            k = 1
                            while self.data['location'][i - k] == self.data['location'][i]:
                                if not self.data[name][i - k] is None:
                                    datalist.append(self.data[name][i - k])
                                    break
                                if i + k == len(self.data[name]) - 1:
                                    datalist.append(None)
                                    break
                                k += 1
                    else:
                        datalist.append(self.data[name][i])
        return datalist
'''
parser = parseVac('vaccinations.txt')
parser.parseAll()
print(parser.getDatalist('total_vaccinations', 'end'))'''
    
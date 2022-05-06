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
        self.people_vaccinations_per_hundred = []
        self.people_fully_vaccinated_per_hundred = []
        self.total_boosters_per_hundred = []
        self.daily_vaccinations_per_million = []
        self.daily_people_vaccinated = []
        self.daily_people_vaccinated_per_hundred = []

        self.data = [
                     self.location, self.iso_code, self.date,
                     self.total_vaccinations, self.people_vaccinated,
                     self.people_fully_vaccinated, self.total_boosters,
                     self.daily_vaccinations_raw, self.daily_vaccinations,
                     self.total_vaccinations_per_hundred, self.people_vaccinations_per_hundred,
                     self.people_fully_vaccinated_per_hundred, self.total_boosters_per_hundred,
                     self.daily_vaccinations_per_million, self.daily_people_vaccinated,
                     self.daily_people_vaccinated_per_hundred
                    ]

        with open(self.path, 'r', encoding = 'utf-8') as f:
            i = 0
            for line in f:
                if i != 0:
                    pieces = re.split(r',|\n', line)
                    for j in range(len(self.data)):
                        self.data[j].append(pieces[j])
                i += 1


#parser = parseVac('vaccinations.txt')
#parser.parseAll()
#print(parser.location)
    
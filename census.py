from documents import Message

class DecadalCountyPopulationMsg(Message):
    """DecadalCountyPopulationMsg class."""

    def __init__(self, county, year, population):
        self.county = county
        self.year = year
        self.population = population

    def __repr__(self):
        return "DecadalCountyPopulationMsg({}, {})".format(self.county,
                                                           self.year,
                                                           self.population)


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

class DecadalCountyPopulation(Message):

    def __init__(self, data, message=DecadalCountyPopulationMsg):
        self.data = data
        self.message = message

    def getMessage(self, limits):
            self.data.execute("""SELECT pop FROM countyPopulation WHERE county=? AND year=?;""",
                              (limits['county'], limits['year']))
            population = self.data.fetchone()

            return self.message(limits['county'], limits['year'],
                                population)


class PopulationDecreaseMsg(Message):
    """Population Decrease Message"""
    def __init__(self, start_year, end_year, start_pop, end_pop):
        self.start_year = start_year
        self.end_year = end_year
        self.start_pop = start_pop
        self.end_pop = end_pop
        self.population_decrease = None

        if self.end_pop < self.start_pop:
            self.population_decrease = self.start_pop - self.end_pop
        else:
            self.population_decrease = None

    def __repr__(self):
        if self.population_decrease is not None:
            return "PopulationDecreaseMessage({}, {}, {})}".format(self.start_year, self.stop_year, self.population_decrease)
        else:
            return None


class PopulationDecrease(Message):

    def __init__(self, data, message=PopulationDecreaseMsg):
        self.data = data
        self.message = message
        self.start_pop = None
        self.end_pop = None
        self.pop_decrease = None

    def getMessage(self, limits):
            # self.data.execute("""SELECT pop FROM countyPopulation WHERE county=? AND year=?;""",
            #                   (limits['county'], limits['start_year']))
            # self.start_pop = self.data.fetchone()
            #
            # self.data.execute("""SELECT pop FROM countyPopulation WHERE county=? AND year=?;""",
            #                   (limits['county'], limits['end_year']))
            #
            # self.end_pop = self.data.fetchone()
            #
            # self.pop_decrease = self.start_pop - self.end_pop

            self.pop_decrease =self.data.execute("""SELECT
                                (SELECT pop FROM countyPopulation WHERE county={0} AND year={1}) - (SELECT pop FROM countyPopulation WHERE county={0} AND year={2}));""",
                                (limits['county'], limits['start_year'], limits['end_year']))


            return self.message(limits['county'], limits['start_year'], limits['end_year'],
                                self.pop_decrease)




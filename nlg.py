import documents
import weather
import data

def nlg(k, c, u, d):
    """k - knowledge source
       c - communicative goal
       u - user model (ex: farmers vs mariners pg45)
       d - discourse history

    """
    pass


def getAllMessages(message, data, limits=None):
    pass

if __name__ == '__main__':

    census_data = data.get_data()

    # weather_data = data.get_data()
    #
    # ### pg 118-119 docplan
    # temp = documents.RelativeVariation(1, documents.Measurement('degreesCentigrade', 2))
    # monthly_temp = weather.MonthlyTemperature.getMessage(weather_data,
    #                                                      limits={'month': 'March'})
    #
    # rain = documents.RelativeVariation(0, documents.Measurement('day', 0))
    # monthly_rain = weather.MonthlyRainfallMsg('March', temp)
    # cs = documents.ConstituentSet('sequence', [monthly_temp, monthly_rain])
    # docplan1 = documents.DocumentPlan(cs)
    # rain_events = weather.RainEvents.getAllMessages(weather_data,
    #                                                 limits={'month': 'March'})
    # cs2 = documents.ConstituentSet('narrativeSequence', rain_events)
    # docplan2 = documents.DocumentPlan(cs)
    #
    # overall_cs = documents.ConstituentSet('sequence', [docplan1, docplan2])
    # overall_docplan = documents.DocumentPlan(overall_cs)
    print "I got here atleast"

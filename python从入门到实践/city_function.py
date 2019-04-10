def get_city_country(city, country, population=0):
    if population:
        return city + ', ' + country + ' - population ' + str(population)
    else:
        return city + ', ' + country


class AnonymouseSurvey(object):
    def __init__(self, question):
        self.question = question
        self.responses = []

    def show_question(self):
        print self.question

    def store_response(self, new_response):
        self.responses.append(new_response)

    def show_results(self):
        print "survey results:"
        for res in self.responses:
            print '-' + res

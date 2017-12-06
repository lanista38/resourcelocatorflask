from flask import jsonify
from handler.resourceRequest import RequestHandler

class DashboardHandler:
    def getDailyStatisticsByRequests(self,days,Region):
        dict = {'Rid': '123', 'Rprice': 55, 'Qty': 20}
        #if days == NIL
            #days = 1
        #if Region == NIL
            #Region = "Any"

        #function filters data
        return jsonify(dict)
    def getDailyStatisticsByAnnouncements(self,days,Region):
        dict = {'Rid': '123', 'Rprice': 55, 'Qty': 20}
        #if days == NIL
            #days = 1
        #if Region == NIL
            #Region = "Any"

        #function filters data
        return jsonify(dict)
    def getDailyStatisticsByMatches(self,days,Region):
        dict = {'Rid': '123', 'Rprice': 55, 'Qty': 20}
        #if days == NIL
            #days = 1
        #if Region == NIL
            #Region = "Any"
        #Match = natural inner join of requests and announcements
        return jsonify(dict)

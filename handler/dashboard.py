from flask import jsonify

class DashboardHandler:
    def getDailyStatisticsByRequests(self,days,Region):
        #if days == NIL
            #days = 1
        #if Region == NIL
            #Region = "Any"
        Request = RequestHandler.getAllRequests()
        #function filters data
        return 0
    def getDailyStatisticsByAnnouncements(self,days,Region):
        #if days == NIL
            #days = 1
        #if Region == NIL
            #Region = "Any"
        Announcement = AnnouncementHandler().getAllAnnouncements
        #function filters data
        return 0
    def getDailyStatisticsByMatches(self,days,Region):
        #if days == NIL
            #days = 1
        #if Region == NIL
            #Region = "Any"
        #Match = natural inner join of requests and announcements
        return 0

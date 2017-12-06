from flask import jsonify

class AnnouncementHandler:
    def build_announcement_dict(self,row):
        dict = {'Pid':'324','Rid':'324','ADate':'hoy','APqty':'1'}
        return dict

    def getAllAnnouncements(self):
        result = self.build_announcement_dict()
        return jsonify(result)

    def AnnounceResource(self,Rname):
        result = self.build_announcement_dict()
        return jsonify(result)

    def getAnnouncementByResource(self,Rname):
        result = self.build_announcement_dict()
        return jsonify(result)

from flask import jsonify

class AnnouncementHandler:
    def build_announcement_dict(self):
        result = {}
        result["Pid"] = row[0]
        result["Rid"] = row[1]
        result["Adate"] = row[2]
        result["Apqty"] = row[3]
        result["region"] = row[4]
        result["Aprice"] = row[5]
        return result

    def getAllAnnouncements(self):
        result = self.build_announcement_dict()
        return jsonify(result)

    def AnnounceResource(self,Rname):
        result = self.build_announcement_dict()
        return jsonify(result)

    def getAnnouncementByResource(self,Rname):
        result = self.build_announcement_dict()
        return jsonify(result)

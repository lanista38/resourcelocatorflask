from flask import jsonify
from dao.announcement import AnnouncementDAO

class AnnouncementHandler:
    def build_announcement_dict(self, row):
        result = {}
        result["Aid"] = row[0]
        result["adate"] = row[1]
        result["aqty"] = row[2]
        result["aprice"] = row[3]
        result["tid"] = row[4]
        result["rid"] = row[5]
        result["sid"] = row[6]
        return result

    def build_announcement_supplier_dict(self, row):
        result = {}
        result["Aid"] = row[0]
        result["adate"] = row[1]
        result["aqty"] = row[2]
        result["aprice"] = row[3]
        result["tid"] = row[4]
        result["rid"] = row[5]
        result["sid"] = row[6]
        result["name"] = row[7]
        result["lastname"] = row[8]
        return result

    def getAllAnnouncements(self):
        dao = AnnouncementDAO()
        announcement_list = dao.getAllAnnouncements()
        result_list = []
        for row in announcement_list:
            result = self.build_announcement_dict(row)
            result_list.append(result)
        return jsonify(AllAnnouncementsBySupplier=result_list)
        #to-do
    def AnnounceResource(self,Rname):
        result = self.build_announcement_dict()
        return jsonify(result)

    def getAnnouncementByResource(self,Rname):
        dao = AnnouncementDAO()
        announcement_list = dao.getAnnouncementByResource(Rname)
        result_list = []
        for row in announcement_list:
            result = self.build_resource_dict(row)
            result_list.append(result)
        return jsonify(Announcements=result_list)

    def getAnnouncementBySname(self, Sname):
        dao = AnnouncementDAO()
        announcement_list = dao.getAnnouncementBySupplier(Sname)
        result_list = []
        for row in announcement_list:
            result = self.build_announcement_supplier_dict(row)
            result_list.append(result)
        return jsonify(AnnouncementsBySupplier=result_list)

    def getAnnouncementBySid(self, Sid):
        dao = AnnouncementDAO()
        announcement_list = dao.getAnnouncementBySid(Sid)
        result_list = []
        for row in announcement_list:
            result = self.build_announcement_supplier_dict(row)
            result_list.append(result)
        return jsonify(AnnouncementsBySupplier=result_list)

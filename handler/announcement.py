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

    def build_announcement_dict_insert(self, aid, sid, rid, aqty, aprice, tid):
        result = {}
        result["aid"] = aid
        result["aqty"] = aqty
        result["aprice"] = aprice
        result["tid"] = tid
        result["rid"] = rid
        result["sid"] = sid
        return result
    def build_announcement_dict_update(self, aid, aqty, aprice, tid):
        result = {}
        result["aid"] = aid
        result["aqty"] = aqty
        result["aprice"] = aprice
        result["tid"] = tid
        return result

    def insertAnnouncement(self, form):
        if len(form) != 5:
            return jsonify(Error = "Bad post request "), 400
        else:
            sid = form['sid']
            rid = form['rid']
            aqty = form['aqty']
            aprice = form['aprice']
            tid = form['tid']
            if sid and rid and aqty and aprice and tid:
                dao = AnnouncementDAO()
                aid = dao.insertAnnouncement(sid, rid, aqty, aprice, tid)
                result = self.build_announcement_dict_insert(aid, sid, rid, aqty, aprice, tid)
                return jsonify(Announcement=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def deleteAnnouncement(self, aid):
        dao = AnnouncementDAO()
        if not dao.getAnnouncementByAid(aid):
            return jsonify(Error = "Part not found."), 404
        else:
            dao.deleteAnnouncement(aid)
            return jsonify(DeleteStatus = "OK"), 200

    def updateAnnouncement(self, aid, form):
        dao = AnnouncementDAO()
        if not dao.getAnnouncementByAid(aid):
            return jsonify(Error = "Part not found."), 404
        else:
            if len(form) != 3:
                return jsonify(Error="Malformed update request"), 400
            else:
                aqty = form['aqty']
                aprice = form['aprice']
                tid = form['tid']
                if rname and rprice and rstock and cid:
                    dao.updateResource(aqty, aprice, tid)
                    result = self.build_announcement_dict_update(aid, aqty, aprice, tid)
                    return jsonify(Announcement=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400

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

    def getAnnouncementByResourceName(self,Rname):
        dao = AnnouncementDAO()
        announcement_list = dao.getAnnouncementByResourceName(Rname)
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

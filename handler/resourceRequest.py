from flask import jsonify
from dao.resourceRequest import ResourceRequestDAO
class RequestHandler:


    def build_request_dict(self, row):
        result = {}
        result['cid'] = row[0]
        result['rid'] = row[1]
        result['rrqty'] = row[2]
        result['rrdate'] = row[3]
        result['tid'] = row[4]
        return result
    def build_request_dict_insert(self, rid, cid, rrqty, tid):
        result = {}
        result['cid'] = cid
        result['rid'] = rid
        result['rrqty'] = rrqty
        result['tid'] = tid
        return result

    def build_request_dict_update(self, rrqty, tid):
        result = {}
        result['rid'] = rid
        result['rrqty'] = rrqty
        result['tid'] = tid
        return result

    def insertRequest(self, form):
        if len(form) != 4:
            return jsonify(Error = "Bad post request "), 400
        else:
            cid = form['cid']
            rid = form['rid']
            rrqty = form['rrqty']
            tid = form['tid']
            if cid and rid and rrqty and tid:
                dao = ResourceRequestDAO()
                rid = dao.insertRequest(cid, rid, rrqty, tid)
                result = self.build_request_dict_insert(rid, cid, rrqty, tid)
                return jsonify(Request=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    #potentially bad, only uses Rid as key
    def deleteRequest(self, cid, rid):
        dao = ResourceRequestDAO()
        if not dao.getRequestByRid(rid):
            return jsonify(Error = "Part not found."), 404
        else:
            dao.deleteRequest(cid, rid)
            return jsonify(DeleteStatus = "OK"), 200

    def updateRequest(self, rid, form):
        dao = ResourceRequestDAO()
        if not dao.getRequestByRid(rid):
            return jsonify(Error = "Part not found."), 404
        else:
            if len(form) != 2:
                return jsonify(Error="Malformed update request"), 400
            else:
                rrqty = form['rrqty']
                tid = form['tid']

                if rrqty and tid :
                    dao.updateRequest(rrqty, tid)
                    result = self.build_resource_dict_instert( rid, rrqty, tid)
                    return jsonify(Resource=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400

    def getAllRequests(self):
        dao = ResourceRequestDAO()
        request_list = dao.getAllRequests()
        result_list = []
        for row in request_list:
            result = self.build_request_dict(row)
            result_list.append(result)
        return jsonify(Requests=result_list)

    def getRequestByRid(self, Rid):
        dao = ResourceRequestDAO()
        request_list = dao.getRequestByRid(Rid)
        result_list = []
        for row in request_list:
            result = self.build_request_dict(row)
            result_list.append(result)
        return jsonify(Requests=result_list)

    def getRequestByResource(self,Rname):
        dao = ResourceRequestDAO()
        request_list = dao.getRequestByResource(Rname)
        result_list = []
        for row in request_list:
            result = self.build_request_dict(row)
            result_list.append(result)
        return jsonify(Requests=result_list)

    #to-do
    def getRequestByTown(self, town):
        dao = ResourceRequestDAO()
        request_list = dao.getRequestByResource(Rname)
        result_list = []
        for row in request_list:
            result = self.build_request_dict(row)
            result_list.append(result)
        return jsonify(Requests=result_list)

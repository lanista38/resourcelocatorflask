from flask import jsonify

class RequestHandler:

    #Dictionary to be revised
    def build_request_dict(self):
        result = {}
        result['Cid'] = row[0]
        result['Rid'] = row[1]
        result['RRqty'] = row[2]
        result['RRdate'] = row[3]
        result['tid'] = row[4]
        result['sid'] = row[5]
        return result

    def getAllRequests(self):
        dao = ResourceDAO()
        request_list = dao.getAllRequests()
        result_list = []
        for row in request_list:
            result = self.build_request_dict(row)
            result_list.append(result)
        return jsonify(Requests=result_list)

    def getRequestByRid(self, Rid):
        dao = ResourceDAO()
        request_list = dao.getRequestByRid(Rid)
        result_list = []
        for row in request_list:
            result = self.build_request_dict(row)
            result_list.append(result)
        return jsonify(Requests=result_list)

    def getRequestByResource(self,Rname):
        dao = ResourceDAO()
        request_list = dao.getRequestByResource(Rname)
        result_list = []
        for row in request_list:
            result = self.build_request_dict(row)
            result_list.append(result)
        return jsonify(Requests=result_list)

    #to-do
    def getRequestByTown(self, town):
        dao = ResourceDAO()
        request_list = dao.getRequestByResource(Rname)
        result_list = []
        for row in request_list:
            result = self.build_request_dict(row)
            result_list.append(result)
        return jsonify(Requests=result_list)

from flask import jsonify

class RequestHandler:
    #Dictionary to be revised
    def build_request_dict(self, row):
        result = {}
        result['Rid'] = row[0]
        result['Rdate'] = row[1]
        return result

    def getAllRequests(self):
        return result

    def getRequestByRPid(self, RPid):
        return 0

    def getRequestByRid(self, Rid):
        return 0

from flask import jsonify

class RequestHandler:
    def build_request_dict(self, row):
        result = {}
        result['Rid'] = row[0]
        result['Rdate'] = row[1]
        return result

    def getAllRequests(self):
        return 0
    def getResourceByRname(self,Rname):
        return 0

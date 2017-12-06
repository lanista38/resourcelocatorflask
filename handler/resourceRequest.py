from flask import jsonify

class RequestHandler:

    #Dictionary to be revised
    def build_request_dict(self):
        dict = {'Rid': '123', 'Rdate': 2017}
        #result = {}
        #result['Rid'] = row[0]
        #result['Rdate'] = row[1]
        return dict

    def getAllRequests(self):
<<<<<<< HEAD

        res = self.build_request_dict()
        return jsonify(res)

    def getRequestByRPid(self, RPid):
    
        res = self.build_request_dict()
        return jsonify(res)

    def getRequestByRid(self, Rid):

        res = self.build_request_dict()
        return jsonify(res)
=======
        return 0
    def getResourceByRname(self,Rname):
        return 0
    def getRequestByResource(self,Rname):
        return 0
>>>>>>> branch-alfredo-jorge

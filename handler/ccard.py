from flask import jsonify
from dao.ccard import CcardDAO

class CcardHandler:
    #Dictionary to be revised

    def build_Ccard_dict(self, row):
        result = {}
        result['ccid'] = row[0]
        result['number'] = row[1]
        result['cvv'] = row[2]
        result['name'] = row[3]
        result['expiration'] = row[4]
        result['cid'] = row[5]
        return result
    
    def build_Ccard_dict_instert(self, ccid, number, cvv, name, expiration, cid):
        result = {}
        result['ccid'] = ccid
        result['number'] = number
        result['cvv'] = cvv
        result['name'] = name
        result['expiration'] = expiration
        result['cid'] = cid
        return result

    def insertCcard(self, form):
        if len(form) != 5:
            print(form['number'])
            return jsonify(Error = "Bad post request "), 400
        else:
            number = form['number']
            cvv = form['cvv']
            name = form['name']
            expiration = form['expiration']
            cid = form['cid']
            if number and expiration and cvv and cid:
                dao = CcardDAO()
                ccid = dao.insertCcard(number, cvv, name, expiration,cid)
                result = self.build_Ccard_dict_instert(ccid, number, cvv, name, expiration,cid)
                return jsonify(Ccard=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def deleteCcard(self, ccid):
        dao = CcardDAO()
        if not dao.getCcardByccid(ccid):
            return jsonify(Error = "Part not found."), 404
        else:
            dao.deleteCcard(ccid)
            return jsonify(DeleteStatus = "OK"), 200

    def updateCcard(self, ccid, form):
        dao = CcardDAO()
        if not dao.getCcardByccid(ccid):
            return jsonify(Error = "Part not found."), 404
        else:
            if len(form) != 5:
                return jsonify(Error="Malformed update request"), 400
            else:
                number = form['number']
                cvv = form['cvv']
                name = form['name']
                expiration = form['expiration']
                cid = form['cid']
                if number and cvv and name and expiration and cid:
                    dao.updateCcard(ccid, number, cvv, name, expiration,cid)
                    result = self.build_Ccard_dict_instert(ccid, number, cvv, name, expiration,cid)
                    return jsonify(Ccard=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400

    def getAllCcards(self):
        dao = CcardDAO()
        Ccard_list = dao.getAllCcards()
        result_list = []
        for row in Ccard_list:
            result = self.build_Ccard_dict(row)
            result_list.append(result)
        return jsonify(Ccards=result_list)

    def getCcardByccid(self, ccid):
        dao = CcardDAO()
        row = dao.getCcardByccid(ccid)
        if not row:
            return jsonify(Error = "Ccard Not Found"), 404
        result = self.build_Ccard_dict(row)
        return jsonify(result)
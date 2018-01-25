from flask import jsonify
from dao.reserve import ReserveDAO

class ReserveHandler:
    #Dictionary to be revised

    def build_reserve_dict(self, row):
        result = {}
        result['rsid'] = row[0]
        result['rsdate'] = row[1]
        result['rsqty'] = row[2]
        result['cid'] = row[3]
        result['rid'] = row[4]
        result['sid'] = row[5]
        result['tid'] = row[6]
        return result
    def build_reserve_dict_instert(self, rsid ,rsqty, cid, rid, sid, tid):
        result = {}
        result['rsid'] = rsid
        result['rsqty'] = rsqty
        result['cid'] = cid
        result['rid'] = rid
        result['sid'] = sid
        result['tid'] = tid
        return result

    def reserveResource(self, form):
        if len(form) != 5:
            return jsonify(Error = "Bad post request "), 400
        else:
            rsqty = form['rsqty']
            cid = form['cid']
            rid = form['rid']
            sid = form['sid']
            tid = form['tid']
            if rsqty and cid and rid and sid and tid:
                dao = ReserveDAO()
                rsid = dao.reserveResource(rsqty, cid, rid, sid, tid)
                result = self.build_reserve_dict_instert(rsid ,rsqty, cid, rid, sid, tid)
                return jsonify(Reserve=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def getAllReserve(self):
        dao = ReserveDAO()
        resource_list = dao.getAllReservations()
        result_list = []
        for row in resource_list:
            result = self.build_reserve_dict(row)
            result_list.append(result)
        return jsonify(Reserve=result_list)

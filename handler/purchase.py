from flask import jsonify
from dao.purchase import PurchaseDAO

class PurchaseHandler:
    #Dictionary to be revised

    def build_purchase_dict(self,row):
        result = {}
        result['pid'] = row[0]
        result['pdate'] = row[1]
        result['pqty'] = row[2]
        result['pprice'] = row[3]
        result['cid'] = row[4]
        result['rid'] = row[5]
        result['sid'] = row[6]
        return result

    def build_purchase_dict_insert(self, pid, pdate, pqty, pprice, cid, rid, sid):
        result = {}
        result['pid'] = pid
        result['pqty'] = pqty
        result['pprice'] = pprice
        result['cid'] = cid
        result['rid'] = rid
        result['sid'] = sid
        return result

    def insertPurchase(self, form):
        if len(form) != 5:
            return jsonify(Error = "Bad post request "), 400
        else:
            pqty = form['pqty']
            pprice = form['pprice']
            cid = form['cid']
            rid = form['rid']
            sid = form['sid']
            if pqty and pprice and cid and rid and sid:
                dao = ResourceRequestDAO()
                pid = dao.insertRequest( pqty, pprice, cid, rid, sid)
                result = self.build_purchase_dict_insert(pid, pqty, pprice, cid, rid, sid)
                return jsonify(Request=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def getAllPurchases(self):
        dao = PurchaseDAO()
        purchase_list = dao.getAllPurchases()
        result_list = []
        for row in purchase_list:
            result = self.build_purchase_dict(row)
            result_list.append(result)
        return jsonify(Purchase=result_list)

    def getPurchaseByRid(self, Rid):
        dao = PurchaseDAO()
        row = dao.getPurchaseByPid(Rid)
        if not row:
            return jsonify(Error = "Resource Not Found"), 404
        result = self.build_purchase_dict(row)
        return jsonify(result)

    def getPurchaseByResource(self, Rid):
        dao = PurchaseDAO()
        purchase_list = dao.getPurchaseByResource(Rid)
        result_list = []
        for row in purchase_list:
            result = self.build_purchase_dict(row)
            result_list.append(result)
        return jsonify(result_list)

    def getPurchaseBySupplier(self, Rid):
        dao = PurchaseDAO()
        purchase_list = dao.getPurchaseBySupplier(Rid)
        result_list = []
        for row in purchase_list:
            result = self.build_purchase_dict(row)
            result_list.append(result)
        return jsonify(result_list)

    def getPurchaseByCustomer(self, Cid):
        dao = PurchaseDAO()
        purchase_list = dao.getPurchaseByCustomer(Cid)
        result_list = []
        for row in purchase_list:
            result = self.build_purchase_dict(row)
            result_list.append(result)
        return jsonify(result_list)

    def search(self, args):
        dao = PurchaseDAO()
        parts_list = []
        parts_list = dao.getSearch(args)
        result_list = []
        for row in parts_list:
            result = self.build_purchase_dict(row)
            result_list.append(result)
        return jsonify(result_list)

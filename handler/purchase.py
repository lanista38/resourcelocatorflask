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
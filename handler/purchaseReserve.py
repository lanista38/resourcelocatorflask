from flask import jsonify

class PurchaseHandler:
    #Dictionary to be revised

    def build_purchase_dict(self):
        dict = {'Rid': '123', 'date': 2017, 'Qty': 5, 'price' : 55}
        #result = {}
        #result['Pid'] = row[0]
        #result['Purchasedate'] = row[1]
        return dict

    def getAllPurchases(self):
        res = self.build_purchase_dict()
        return jsonify(res)

    def getPurchaseByRid(self, Rid):
        res = self.build_purchase_dict()
        return jsonify(res)

    def getPurchaseByRPid(self, RPid):
        res = self.build_purchase_dict()
        return jsonify(res)

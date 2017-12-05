from flask import jsonify

class PurchaseHandler:
    #Dictionary to be revised

    def build_purchase_dict(self, row):
        result = {}
        result['Pid'] = row[0]
        result['Purchasedate'] = row[1]

    def getAllPurchases(self):
        return result

    def getPurchaseByRid(self, Rid):
        return 0

    def getPurchaseByRPid(self, RPid):
        return 0

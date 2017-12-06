from flask import jsonify
#from dao.supplier import SupplierDAO


class SupplierHandler:
    def build_supplier_dict(self):
        dict = {'Rid': '123', 'date': 2017, 'Qty': 5, 'price' : 55}
        return dict

    def getAllSuppliers(self):
        res = self.build_supplier_dict()
        return jsonify(res)

    def getSupplierById(self, sid):
        res = self.build_supplier_dict()
        return jsonify(res)

    def getPartsBySupplierId(self, sid):
        res = self.build_supplier_dict()
        return jsonify(res)

    def searchSuppliers(self, args):
        res= self.build_supplier_dict()
        return jsonify(res)

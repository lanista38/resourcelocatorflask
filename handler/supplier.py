from flask import jsonify
#from dao.supplier import SupplierDAO


class SupplierHandler:
    def build_supplier_dict(self):
<<<<<<< HEAD
        dict = {'Pid': '123', 'Name': 'Juan', 'lastName': 'Cruz', 'Company' : 'Microsoft'}

        #result = {}
        #result['sid'] = row[0]
        #result['sname'] = row[1]
        #result['scity'] = row[2]
        #result['sphone'] = row[3]
=======
        dict = {'Rid': '123', 'date': 2017, 'Qty': 5, 'price' : 55}
>>>>>>> 1dcd8c005d1b2accb8f033f5de0cc89a0945da68
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

from flask import jsonify
#from dao.supplier import SupplierDAO


class SupplierHandler:
    def build_supplier_dict(self):
        dict = {'Rid': '123', 'date': 2017, 'Qty': 5, 'price' : 55}

        #result = {}
        #result['sid'] = row[0]
        #result['sname'] = row[1]
        #result['scity'] = row[2]
        #result['sphone'] = row[3]
        return dict

    def getAllSuppliers(self):
        res = self.build_supplier_dict()
        #dao = SupplierDAO()
        #suppliers_list = dao.getAllSuppliers()
        #result_list = []
        #for row in suppliers_list:
        #    result = self.build_supplier_dict(row)
        #    result_list.append(result)
        return jsonify(res)

    def getSupplierById(self, sid):
        res = self.build_supplier_dict()
        #dao = SupplierDAO()

        #row = dao.getSupplierById(sid)
        #if not row:
        #    return jsonify(Error="Supplier Not Found"), 404
        #else:
        #    part = self.build_supplier_dict(row)
        return jsonify(res)

    def getPartsBySupplierId(self, sid):
        res = self.build_supplier_dict()
        #dao = SupplierDAO()
        #if not dao.getSupplierById(sid):
        #    return jsonify(Error="Supplier Not Found"), 404
        #parts_list = dao.getPartsBySupplierId(sid)
        #result_list = []
        #for row in parts_list:
        #    result = self.build_part_dict(row)
        #    result_list.append(result)
        return jsonify(res)

    def searchSuppliers(self, args):
        res= self.build_supplier_dict()
        #if len(args) > 1:
        #    return jsonify(Error = "Malformed search string."), 400
        #else:
        #    city = args.get("city")
        #    if city:
        #        dao = SupplierDAO()
        #        supplier_list = dao.getSuppliersByCity(city)
        #        result_list = []
        #        for row in supplier_list:
        #            result = self.build_supplier_dict(row)
        #            result_list.append(row)
        #        return jsonify(Suppliers=result_list)
        #    else:
        #        return jsonify(Error="Malformed search string."), 400
        return jsonify(res)

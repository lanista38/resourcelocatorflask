from flask import jsonify
from dao.supplier import SupplierDAO


class SupplierHandler:

    def build_part_attributes(self, sid, name, lastname, company, gpsy, gpsx, address, tid):
        result = {}
        result['sid'] = sid
        result['name'] = name
        result['lastname'] = lastname
        result['company'] = company
        result['gpsy'] = gpsy
        result['gpsx'] = gpsx
        result['address'] = address
        result['tid'] = tid
        return result

    def build_supplier_dict(self, row):
        result = {}
        result['sid'] = row[0]
        result['name'] = row[1]
        result['lastname'] = row[2]
        result['company'] = row[3]
        result['gpsy'] = row[4]
        result['gpsx'] = row[5]
        result['address'] = row[6]
        result['tid'] = row[7]
        return result

    def build_supplier_town_dict(self, row):
        result = {}
        result['sid'] = row[0]
        result['name'] = row[1]
        result['lastname'] = row[2]
        result['company'] = row[3]
        result['gpsy'] = row[4]
        result['gpsx'] = row[5]
        result['address'] = row[6]
        result['tname'] = row[8]
        result['tid'] = row[9]
        return result

    def getAllSuppliers(self):
        dao = SupplierDAO()
        supplier_list = dao.getAllSuppliers()
        result_list = []
        for row in supplier_list:
            result = self.build_supplier_dict(row)
            result_list.append(result)
        return jsonify(Suppliers=result_list)

    def getSupplierById(self, Sid):
        dao = SupplierDAO()
        supplier_list = dao.getSupplierById(Sid)
        result_list = []
        for row in supplier_list:
            result = self.build_supplier_dict(row)
            result_list.append(result)
        return jsonify(Suppliers=result_list)

    def getSuppliersByTown(self, tname):
        dao = SupplierDAO()
        supplier_list = dao.getSuppliersByTown(tname)
        result_list = []
        for row in supplier_list:
            result = self.build_supplier_dict(row)
            result_list.append(result)
        return jsonify(Suppliers=result_list)

    def getSuppliersByResourceName(self,rname):
        dao = SupplierDAO()
        supplier_list = dao.getSuppliersByResourceName(rname)
        result_list = []
        for row in supplier_list:
            result = self.build_supplier_dict(row)
            result_list.append(result)
        return jsonify(Suppliers=result_list)

    def getSuppliersByResourceID(self,rid):
        dao = SupplierDAO()
        supplier_list = dao.getSuppliersByResourceID(rid)
        result_list = []
        for row in supplier_list:
            result = self.build_supplier_dict(row)
            result_list.append(result)
        return jsonify(Suppliers=result_list)

    def searchSuppliers(self, args):
        town = args.get("town")
        material = args.get("company")
        dao = SupplierDAO()
        parts_list = []
        if (len(args) == 2) and town and company:
            parts_list = dao.getSuppliersByTownAndCompany(town, company)
        elif (len(args) == 1) and town:
            parts_list = dao.getSuppliersByTown(town)
        elif (len(args) == 1) and company:
            parts_list = dao.getSuppliersByCompany(company)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        if town:
            for row in part_list:
                result = build_supplier_town_dict(row)
                result_list.append(result)
        else:
            for row in parts_list:
                result = self.build_part_dict(row)
                result_list.append(result)
        return jsonify(Parts=result_list)

    def registerSupplier(self, form):
        print(form)
        if len(form) != 7:
            return jsonify(Error = "Bad post request "), 400
        else:
            name = form['name']
            lastname = form['lastname']
            company = form['company']
            gpsy = form.get('gpsy') or None
            gpsx = form.get('gpsx') or None
            address = form['address']
            tid = form['tid']
            if name and company and lastname and address and tid:
                dao = SupplierDAO()
                cid = dao.registerSupplier(name, lastname, company, gpsy, gpsx, address, tid)
                result = self.build_part_attributes(cid, name, lastname, company, gpsy, gpsx, address, tid)
                return jsonify(Supplier=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400
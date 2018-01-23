from flask import jsonify
from dao.resource import ResourceDAO

class ResourceHandler:
    #Dictionary to be revised

    def build_resource_dict(self, row):
        result = {}
        result['Rid'] = row[0]
        result['Rname'] = row[1]
        result['rstock'] = row[2]
        result['cid'] = row[3]
        result['rprice'] = row[4]
        return result

<<<<<<< HEAD

=======
    def build_resource_dict_instert(self, rid, rname, rstock, cid, rprice):
        result = {}
        result['Rid'] = rid
        result['Rname'] = rname
        result['rstock'] = rstock
        result['rprice'] = cid
        result['cid'] = cid
        return result

    def insertResource(self, form):
        if len(form) != 4:
            return jsonify(Error = "Bad post request "), 400
        else:
            rname = form['rname']
            rprice = form['rprice']
            rstock = form['rstock']
            cid = form['cid']
            if rname and rprice and rstock and cid:
                dao = ResourceDAO()
                rid = dao.insertResource(rname, rstock, cid, rprice)
                result = self.build_resource_dict_instert(rid, rname, rstock, cid, rprice)
                return jsonify(Resource=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def deleteResource(self, rid):
        dao = ResourceDAO()
        if not dao.getResourceByRid(rid):
            return jsonify(Error = "Part not found."), 404
        else:
            dao.deleteResource(rid)
            return jsonify(DeleteStatus = "OK"), 200

    def updateResource(self, rid, form):
        dao = ResourceDAO()
        if not dao.getResourceByRid(rid):
            return jsonify(Error = "Part not found."), 404
        else:
            if len(form) != 4:
                return jsonify(Error="Malformed update request"), 400
            else:
                rname = form['rname']
                rprice = form['rprice']
                rstock = form['rstock']
                cid = form['cid']
                if rname and rprice and rstock and cid:
                    dao.updateResource(rid, pname, pcolor, pmaterial, pprice)
                    result = self.build_resource_dict(rid, rname, rstock, cid, rprice)
                    return jsonify(Resource=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400
>>>>>>> Phase2(In-Progress)

    def getAllResources(self):
        dao = ResourceDAO()
        resource_list = dao.getAllResources()
        result_list = []
        for row in resource_list:
            result = self.build_resource_dict(row)
            result_list.append(result)
        return jsonify(Resources=result_list)
<<<<<<< HEAD
=======

        #operation 8 --> Resources Available
    def getAllResourcesInStock(self):
            dao = ResourceDAO()
            parts_list = dao.getAllResourcesInStock()
            result_list = []
            for row in parts_list:
                result = self.build_resource_dict(row)
                result_list.append(result)
            return jsonify(Resource=result_list)
    def getResourceInStockByName(self, rname):
            dao = ResourceDAO()
            #name = args.get("rname")
            parts_list = dao.getResourceInStockByName(rname)
            result_list = []
            for row in parts_list:
                result = self.build_resource_dict(row)
                result_list.append(result)
            return jsonify(Resource=result_list)
>>>>>>> Phase2(In-Progress)

    def getResourceByRid(self, Rid):
        dao = ResourceDAO()
        row = dao.getResourceByRid(Rid)
        if not row:
            return jsonify(Error = "Resource Not Found"), 404
<<<<<<< HEAD
        else:
            resource = self.build_resource_dict(row)
            return jsonify(Resource = resource)

    def getResourceByName(self, Rname):
        dao = ResourceDAO()
        resource_list = dao.getResourceByName(Rname)
        result_list = []
        for row in resource_list:
            result = self.build_resource_dict(row)
            result_list.append(result)
        return jsonify(Resources=result_list)

    def getResourcesByCategoryId(self, Cid):
        dao = ResourceDAO()
        resource_list = dao.getResourceByCid(Cid)
        result_list = []
        for row in resource_list:
            result = self.build_resource_dict(row)
            result_list.append(result)
        return jsonify(Resources=result_list)

    def getResourcesByCategoryName(self, Cname):
        dao = ResourceDAO()
        resource_list = dao.getAllResources()
        result_list = []
        for row in resource_list:
            result = self.build_resource_dict(row)
            result_list.append(result)
        return jsonify(Resources=result_list)
=======
        result = self.build_resource_dict(row)
        return jsonify(result)

    def getResourceByName(self, Rname):
        dao = ResourceDAO()
        parts_list = dao.getResourceByRname(Rname)
        result_list = []
        for row in parts_list:
            result = self.build_resource_dict(row)
            result_list.append(result)
        return jsonify(Resource=result_list)

    def getResourcesByCid(self, Cid):
        dao = ResourceDAO()
        parts_list = dao.getResourceByCid(Cid)
        result_list = []
        for row in parts_list:
            result = self.build_resource_dict(row)
            result_list.append(result)
        return jsonify(Resource=result_list)

    # Operation 14
    def getResourceBySupplier(self, Rid,Sid):
        dao = ResourceDAO()
        parts_list = dao.getResourceBySupplier(Rid,Sid)
        result_list = []
        for row in parts_list:
            result = self.build_resource_dictt(row)
            result_list.append(result)
        return jsonify(Resource=result_list)

    def getResourceByCategoryName(self, Cname):
        dao = ResourceDAO()
        parts_list = dao.getResourceByCategoryName(Cname)
        result_list = []
        for row in parts_list:
            result = self.build_resource_dict(row)
            result_list.append(result)
        return jsonify(Resource=result_list)
>>>>>>> Phase2(In-Progress)

    def getResourceByIdRegion(self, Rid, Tid):
        dao = ResourceDAO()
        parts_list = dao.getResourceByIdRegion(Rid,Tid)
        result_list = []
        for row in parts_list:
            result = self.build_resource_dict(row)
            result_list.append(result)
        return jsonify(Resource=result_list)



# To-Do, should also add by name and instock/out of stock
    def search(self, args):
        dao = ResourceDAO()
<<<<<<< HEAD
        resource_list = dao.getResourceByCategoryName(Cname)
=======
>>>>>>> Phase2(In-Progress)
        price = args.get("price")
        category = args.get("category")
        dao=ResourceDAO()
        parts_list = []
        if (len(args) == 2) and price and category:
            parts_list = dao.getResourceByPriceCid(price,category)
        elif (len(args) == 1) and price:
            parts_list = dao.getResourceByPrice(price)
        elif (len(args) == 1) and category:
            parts_list = dao.getResourceByCid(category)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
<<<<<<< HEAD
        result_list=self.build_resource_dict(row)
=======
        for row in parts_list:
            result = self.build_resource_dict(row)
            result_list.append(result)
>>>>>>> Phase2(In-Progress)
        return jsonify(result_list)

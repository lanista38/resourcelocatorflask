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

    def build_resource_dictt(self, row):
        result = {}
        result['Rid'] = row[0]
        result['Rname'] = row[1]
        result['rstock'] = row[2]
        result['town'] = row[3]
        return result

    def getAllResources(self):
        dao = ResourceDAO()
        resource_list = dao.getAllResources()
        result_list = []
        for row in resource_list:
            result = self.build_resource_dict(row)
            result_list.append(result)
        return jsonify(Resources=result_list)

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

    def getResourceByRid(self, Rid):
        dao = ResourceDAO()
        row = dao.getResourceByRid(Rid)
        if not row:
            return jsonify(Error = "Resource Not Found"), 404
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
        for row in parts_list:
            result = self.build_resource_dict(row)
            result_list.append(result)
        return jsonify(result_list)

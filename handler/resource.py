from flask import jsonify
from dao.resource import ResourceDAO

class ResourceHandler:
    #Dictionary to be revised

    def build_resource_dict(self, row):
        result = {}
        result['Rid'] = row[0]
        result['Rname'] = row[1]
        result['Cid'] = row[2]
        result['Sid'] = row[3]
        result['Rprice'] = row[4]
        result['Rqty'] = row[5]
        result['Rregion'] = row[6]
        return result



    def getAllResources(self):
        dao = ResourceDAO()
        resource_list = dao.getAllResources()
        result_list = []
        for row in resource_list:
            result = self.build_resource_dict(row)
            result_list.append(result)
        return jsonify(Resources=result_list)

    def getResourceByRid(self, Rid):
        dao = ResourceDAO()
        row = dao.getResourceByRid(Rid)
        if not row:
            return jsonify(Error = "Resource Not Found"), 404
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

    def search(self, args):
        dao = ResourceDAO()
        resource_list = dao.getResourceByCategoryName(Cname)
        price = args.get("price")
        region = args.get("region")
        category = args.get("category")
        parts_list = []
        if (len(args) == 2) and price and region:
            parts_list = self.getAllResources()
        elif (len(args) == 1) and price:
            parts_list = self.getAllResources()
        elif (len(args) == 1) and region:
            parts_list = self.getAllResources()
        elif (len(args) == 1) and category:
            parts_list = self.getAllResources()
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        result_list=self.build_resource_dict(row)
        return jsonify(result_list)

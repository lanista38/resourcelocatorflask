from flask import jsonify

class ResourceHandler:
    #Dictionary to be revised

    def build_resource_dict(self, row):
        result = {}
        result['Rid'] = row[0]
        result['Rname'] = row[1]
        result['Rprice'] = row[2]
        result['Rqty'] = row[3]
        result['Rregion'] = row[4]

    def build_resource_dict(self):
        dict = [{'Rid': '123', 'Rname': 2017,'Rprice': 4,'Rqty':15,'Rregion':'Oeste'},
                {'Rid': '542', 'Rname': 2017,'Rprice': 4,'Rqty':15,'Rregion':'Oeste'},
                {'Rid': '458', 'Rname': 2017, 'Rprice': 4, 'Rqty': 15, 'Rregion': 'Oeste'},
                {'Rid': '785', 'Rname': 2017, 'Rprice': 4, 'Rqty': 15, 'Rregion': 'Oeste'},
                {'Rid': '785', 'Rname': 2017, 'Rprice': 4, 'Rqty': 15, 'Rregion': 'Oeste'}]
        return dict

    def getAllResources(self):
        result=self.build_resource_dict()
        return jsonify(result)

    def getResourceByRid(self, Rid):
        result=self.build_resource_dict()
        return jsonify(result)

    def getResourceByName(self, Rname):
        result=self.build_resource_dict()
        return jsonify(result)

    def getResourcesByCategoryId(self, Rid):
        result=self.build_resource_dict()
        return jsonify(result)

    def getResourcesByCategoryName(self, Rname):
        result=self.build_resource_dict()
        return jsonify(result)

    def search(self, args):
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
        result_list=self.build_resource_dict()
        return jsonify(result_list)

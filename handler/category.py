from flask import jsonify

class CategoryHandler:
    #Dictionary to be revised

    def build_category_dict(self, row):
        result = {}
        result['Cid'] = row[0]
        result['Cname'] = row[1]

    def build_resource_dict(self):
        dict = [{'Cid': '123', 'Cname': 2017},
                {'Cid': '456', 'Cname': 2017},
                {'Cid': '845', 'Cname': 2017},
                {'Cid': '875', 'Cname': 2017},
                {'Cid': '845', 'Cname': 2017},]
        return dict

    def getAllCategories(self):
        result=self.build_resource_dict()
        return jsonify(result)

    def getCategoryByCid(self, Cid):
        result=self.build_resource_dict()
        return jsonify(result)

    def getCategoryByCname(self, Cname):
        result=self.build_resource_dict()
        return jsonify(result)

    def getAllResourcesByCategoryId(self, Cid):
        result=self.build_resource_dict()
        return jsonify(result)

    def getAllResourcesByCategoryName(self, name):
        result=self.build_resource_dict()
        return jsonify(result)
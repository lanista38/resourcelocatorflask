from flask import jsonify
from dao.category import CategoryDAO
class CategoryHandler:
    #Dictionary to be revised

    def build_category_dict(self, row):
        result = {}
        result['Cid'] = row[0]
        result['Cname'] = row[1]
        return result

    def build_resource_dict(self):
        dict = [{'Cid': '123', 'Cname': 2017},
                {'Cid': '456', 'Cname': 2017},
                {'Cid': '845', 'Cname': 2017},
                {'Cid': '875', 'Cname': 2017},
                {'Cid': '845', 'Cname': 2017},]
        return dict

    def getAllCategories(self):
        dao = CategoryDAO()
        parts_list = dao.getAllCategories()
        result_list = []
        for row in parts_list:
            result = self.build_category_dict(row)
            result_list.append(result)
        return jsonify(Parts=result_list)

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

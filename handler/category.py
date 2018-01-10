from flask import jsonify
from dao.category import CategoryDAO
class CategoryHandler:
    #Dictionary to be revised

    def build_category_dict(self, row):
        result = {}
        result['Cid'] = row[0]
        result['Cname'] = row[1]
        return result

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

    def build_resource_dict(self):
        dict = [{'Cid': '123', 'Cname': 2017},
                {'Cid': '456', 'Cname': 2017},
                {'Cid': '845', 'Cname': 2017},
                {'Cid': '875', 'Cname': 2017},
                {'Cid': '845', 'Cname': 2017},]
        return dict

    def getAllCategories(self):
        dao = CategoryDAO()
        category_list = dao.getAllCategories()
        result_list = []
        for row in category_list:
            result = self.build_category_dict(row)
            result_list.append(result)
        return jsonify(Parts=result_list)

    def getCategoryByCid(self, Cid):
        dao = CategoryDAO()
        category_list = dao.getCategoryByCid(Cid)
        result_list = []
        for row in category_list:
            result = self.build_category_dict(row)
            result_list.append(result)
        return jsonify(Parts=result_list)

    def getCategoryByCname(self, Cname):
        result=self.build_resource_dict()
        return jsonify(result)

    def getAllResourcesByCategoryId(self, Cid):
        dao = CategoryDAO()
        resource_list = dao.getAllResourcesByCategoryId()
        result_list = []
        for row in category_list:
            result = self.build_resource_dict(row)
            result_list.append(result)
        return jsonify(Parts=result_list)

    def getAllResourcesByCategoryName(self, Cname):
        dao = CategoryDAO()
        resource_list = dao.getAllResourcesByCategoryName()
        result_list = []
        for row in category_list:
            result = self.build_resource_dict(row)
            result_list.append(result)
        return jsonify(Parts=result_list)

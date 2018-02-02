from flask import jsonify
from dao.customer import CustomerDAO
from dao.user import UserDAO

class CustomerHandler:

    def build_part_attributes(self, cid, name, lastname, gpsy, gpsx, address, tid):
        result = {}
        result['cid'] = cid
        result['name'] = name
        result['lastname'] = lastname
        result['gpsy'] = gpsy
        result['gpsx'] = gpsx
        result['address'] = address
        result['tid'] = tid
        return result

    def build_part_attributesUser(self, puid ,username, password, cid, sid):
        result = {}
        result['puid'] = puid
        result['username'] = username
        result['password'] = password
        result['cid'] = cid
        result['sid'] = sid
        return result

    def build_Customer_dict(self, row):
        result = {}
        result['cid'] = row[0]
        result['name'] = row[1]
        result['lastname'] = row[2]
        result['gpsy'] = row[3]
        result['gpsx'] = row[4]
        result['address'] = row[5]
        result['tid'] = row[6]
        return result

    def registerCustomer(self, form):
        print(form)
        if len(form) != 6:
            return jsonify(Error = "Bad post request "), 400
        else:
            name = form['name']
            lastname = form['lastname']
            gpsy = form.get('gpsy') or None
            gpsx = form.get('gpsx') or None
            address = form['address']
            tid = form['tid']
            if name and lastname and address and tid:
                dao = CustomerDAO()
                cid = dao.registerCustomer(name, lastname, gpsy, gpsx, address, tid)
                result = self.build_part_attributes(cid, name, lastname, gpsy, gpsx, address, tid)
                return jsonify(Customer=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def getAllCustomers(self):
        dao = CustomerDAO()
        user_list = dao.getAllCustomers()
        result_list = []
        for row in user_list:
            result = self.build_Customer_dict(row)
            result_list.append(result)
        return jsonify(Customers=result_list)

    def registerCustomerUser(self, form):
        print(form)
        if len(form) != 8:
            return jsonify(Error = "Bad post request "), 400
        else:
            name = form['name']
            lastname = form['lastname']
            gpsy = form.get('gpsy') or None
            gpsx = form.get('gpsx') or None
            address = form['address']
            tid = form['tid']
            username = form['username']
            password = form['password']
            if name and lastname and address and tid:
                dao = CustomerDAO()
                cid = dao.registerCustomer(name, lastname, gpsy, gpsx, address, tid)
                result = self.build_part_attributes(cid, name, lastname, gpsy, gpsx, address, tid)
                if username and password and cid:
                    dao = UserDAO()
                    puid = dao.registerUser(username, password, cid, None)
                    result1 = self.build_part_attributesUser(puid, username, password, cid, None)
                return jsonify({"Customer": result,"User": result1}), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400


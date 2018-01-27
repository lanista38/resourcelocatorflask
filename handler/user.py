from flask import jsonify
from dao.user import UserDAO


class UserHandler:

    def build_part_attributes(self, username, password, cid, sid):
        result = {}
        result['username'] = username
        result['password'] = password
        result['cid'] = cid
        result['sid'] = sid
        return result

    def registerUser(self, form):
        print(form)
        if len(form) != 3:
            return jsonify(Error = "Bad post request "), 400
        else:
            username = form['username']
            password = form['password']
            cid = form.get('cid') or None
            sid = form.get('sid') or None
            if username and password and (cid or sid):
                dao = UserDAO()
                rid = dao.registerUser(username, password, cid, sid)
                result = self.build_part_attributes(username, password, cid, sid)
                return jsonify(Part=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400


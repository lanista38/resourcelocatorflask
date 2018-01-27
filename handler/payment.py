from flask import jsonify
from dao.payment import PaymentDAO


class PaymentHandler:

    def build_part_attributes(self, tipo, ccid, pid):
        result = {}
        result['tipo'] = tipo
        result['ccid'] = ccid
        result['pid'] = pid
        return result

    def registerPayment(self, form):
        print(form)
        if len(form) != 3:
            return jsonify(Error = "Bad post request "), 400
        else:
            tipo = form['tipo']
            ccid = form['ccid']
            pid = form['pid']
            if tipo and ccid and pid:
                dao = PaymentDAO()
                rid = dao.registerPayment(tipo, ccid, pid)
                result = self.build_part_attributes(tipo, ccid, pid)
                return jsonify(Part=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400


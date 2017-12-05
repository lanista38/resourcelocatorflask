from flask import Flask, jsonify, request
from handler.supplier import SupplierHandler
from handler.resourceRequest import RequestHandler
from handler.purchaseReserve import PurchaseHandler



app = Flask(__name__)

@app.route('/')
def greeting():
    return 'Hello, this is the parts DB App!'


@app.route('/PartApp/suppliers')
def getAllSuppliers():
    if not request.args:
        return SupplierHandler().getAllSuppliers()
    else:
        return SupplierHandler().searchSuppliers(request.args)

@app.route('/PartApp/suppliers/<int:sid>')
def getSupplierById(sid):
    return SupplierHandler().getSupplierById(sid)


# Resource Requests routes
@app.route('/PartApp/requests')
def getAllRequests():
    return RequestHandler().getAllRequests()

@app.route('/PartApp/requests/<int:Rid>')
def getRequestById(Rid):
    return RequestHandler().getRequestByRid(Rid)

@app.route('/PartApp/requests/<int:RPid>')
def getRequestByRPId(RPid):
    return RequestHandler().getRequestByRPId(RPid)


#Reserve/Purchase routes

@app.route('/PartApp/purchases')
def getAllPurchases():
    return PurchaseHandler().getAllPurchases()

@app.route('/PartApp/purchases/<int:Rid>')
def getPurchaseByRid(Rid):
    return PurchaseHandler().getPurchaseByRid(Rid)

@app.route('/PartApp/purchases/<int:RPid>')
def getPurchaseByRPid(RPid):
    return PurchaseHandler().getPurchaseByRPid(RPid)


if __name__ == '__main__':
    app.run()

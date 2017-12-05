from flask import Flask, jsonify, request
from handler.parts import PartHandler
from handler.supplier import SupplierHandler



app = Flask(__name__)

@app.route('/')
def greeting():
    return 'Welcome to Disaster Relief Web-App!'

@app.route('/registerAdmin')
    return RegistrationHandler().registerAdmin()

@app.route('/registerSupplier')
    return RegistrationHandler().registerSupplier()

@app.route('/registerRequester')
    return RegistrationHandler().registerRequester()

@app.route('/ResourceRequest/Resource/<string:Rname>')
def getAllRequests():
    return RequestHandler().getResourceByRname(Rname)

@app.route('/AnnounceResource/Resource/<string:Rname>')
def getAllAnnouncements():
    return AnnouncementHandler().AnnounceResource(Rname)


#Hasta aqui son nuestras rutas por ahora



@app.route('/registerAdmin')
def getAllParts():
    if not request.args:
        return RegistrationHandler().registerAdmin()
    else:
        return PartHandler().searchParts(request.args)


@app.route('/PartApp/parts/<int:pid>')
def getPartById(pid):
    return PartHandler().getPartById(pid)

@app.route('/PartApp/parts/<int:pid>/suppliers')
def getSuppliersByPartId(pid):
    return PartHandler().getSuppliersByPartId(pid)

@app.route('/PartApp/suppliers')
def getAllSuppliers():
    if not request.args:
        return SupplierHandler().getAllSuppliers()
    else:
        return SupplierHandler().searchSuppliers(request.args)

@app.route('/PartApp/suppliers/<int:sid>')
def getSupplierById(sid):
    return SupplierHandler().getSupplierById(sid)

@app.route('/PartApp/suppliers/<int:sid>/parts')
def getPartsBySuplierId(sid):
    return SupplierHandler().getPartsBySupplierId(sid)

@app.route('/PartApp/requests')
def getAllRequests():
    return 0


if __name__ == '__main__':
    app.run()

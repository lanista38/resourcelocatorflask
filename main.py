from flask import Flask, jsonify, request
<<<<<<< HEAD
from handler.supplier import SupplierHandler
from handler.resourceRequest import RequestHandler
from handler.purchaseReserve import PurchaseHandler

=======
from handler.registration import RegistrationHandler
from handler.ResourceRequest import RequestHandler
from handler.dashboard import DashboardHandler
from handler.announcement import AnnouncementHandler
>>>>>>> branch-alfredo-jorge


app = Flask(__name__)

@app.route('/')
def greeting():
<<<<<<< HEAD
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
=======
    return 'Welcome to Disaster Relief Web-App!'

@app.route('/registerAdmin')
def registerAdmin():
    return RegistrationHandler().registerAdmin()

@app.route('/registerSupplier')
def registerSupplier():
    return RegistrationHandler().registerSupplier()

@app.route('/registerRequester')
def registerRequester():
    return RegistrationHandler().registerRequester()

@app.route('/ResourceRequest/Resource/<string:Rname>')
def getAllRequests():
    return RequestHandler().getResourceByRname(Rname)

@app.route('/AnnounceResource/Resource/<string:Rname>')
def getAllAnnouncements():
    return AnnouncementHandler().AnnounceResource(Rname)

@app.route('/BrowseAnnouncements/')
def getAllAnnouncements():
    return AnnouncementHandler().getAllAnnouncements()

@app.route('/BrowseRequests/')
def getAllRequests():
    return RequestHandler().getAllRequests()

@app.route('/SearchRequests/Resource/<string:Rname>')
def getAllRequests():
    return RequestHandler().getRequestByResource(Rname)

@app.route('/SearchAnnounce/Resource/<string:Rname>')
def getAllAnnouncements():
    return AnnouncementHandler().getAnnouncementByResource(Rname)

@app.route('/ShowDashRequests/days/<int:days>/Region/<string:Region>')
    return DashboardHandler().getDailyStatisticsByRequests(days,Region)

@app.route('/ShowDashAnnouncements/days/<int:days>/Region/<string:Region>')
    return DashboardHandler().getDailyStatisticsByAnnouncements(days,Region)

@app.route('/ShowDashByMatches/days/<int:days>/Region/<string:Region>')
    return DashboardHandler().getDailyStatisticsByMatches(days,Region)
>>>>>>> branch-alfredo-jorge

#Hasta aqui son nuestras rutas por ahora

if __name__ == '__main__':
    app.run()

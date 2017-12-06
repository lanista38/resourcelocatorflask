from flask import Flask, jsonify, request
from handler.supplier import SupplierHandler
from handler.resourceRequest import RequestHandler
from handler.purchaseReserve import PurchaseHandler
from handler.registration import RegistrationHandler
from handler.dashboard import DashboardHandler
from handler.announcement import AnnouncementHandler



app = Flask(__name__)

@app.route('/')
def greeting():
    return 'Hello, this is the parts DB App!'


@app.route('/ResourceLocator/suppliers')
def getAllSuppliers():
    if not request.args:
        return SupplierHandler().getAllSuppliers()
    else:
        return SupplierHandler().searchSuppliers(request.args)

@app.route('/ResourceLocator/suppliers/<int:sid>')
def getSupplierById(sid):
    return SupplierHandler().getSupplierById(sid)


# Resource Requests routes

@app.route('/ResourceLocator/requests/<int:Rid>')
def getRequestById(Rid):
    return RequestHandler().getRequestByRid(Rid)

@app.route('/ResourceLocator/requests/<int:RPid>')
def getRequestByRPId(RPid):
    return RequestHandler().getRequestByRPId(RPid)


#Reserve/Purchase routes

@app.route('/ResourceLocator/purchases')
def getAllPurchases():
    return PurchaseHandler().getAllPurchases()

@app.route('/ResourceLocator/purchases/<int:Rid>')
def getPurchaseByRid(Rid):
    return PurchaseHandler().getPurchaseByRid(Rid)

@app.route('/ResourceLocator/purchases/<int:RPid>')
def getPurchaseByRPid(RPid):
    return PurchaseHandler().getPurchaseByRPid(RPid)


# Register endpoints
@app.route('/ResourceLocator/registerAdmin')
def registerAdmin():
    return RegistrationHandler().registerAdmin()

@app.route('/ResourceLocator/registerSupplier')
def registerSupplier():
    return RegistrationHandler().registerSupplier()

@app.route('/ResourceLocator/registerRequester')
def registerRequester():
    return RegistrationHandler().registerRequester()


@app.route('/ResourceLocator/ResourceRequest/Resource/<string:Rname>')
def postRequest(Rname):
    return RequestHandler().getRequestByResource(Rname)

@app.route('/ResourceLocator/AnnounceResource/Resource/<string:Rname>')
def postAnnouncement(Rname):
    return AnnouncementHandler().AnnounceResource(Rname)

@app.route('/ResourceLocator/BrowseAnnouncements/')
def getAllAnnouncements():
    return AnnouncementHandler().getAllAnnouncements()

@app.route('/ResourceLocator/BrowseRequests/')
def getAllRequests():
    return RequestHandler().getAllRequests()


#SEARCH endpoints
@app.route('/ResourceLocator/SearchRequests/Resource/<string:Rname>')
def searchRequests(Rname):
    return RequestHandler().getRequestByResource(Rname)

@app.route('/ResourceLocator/SearchAnnounce/Resource/<string:Rname>')
def searchAnnouncements(Rname):
    return AnnouncementHandler().getAnnouncementByResource(Rname)

#DASHBOARD endpoints
@app.route('/ResourceLocator/ShowDashRequests/days/<int:days>/Region/<string:Region>')
def ShowDashRequests(days, Region):
    return DashboardHandler().getDailyStatisticsByRequests(days,Region)

@app.route('/ResourceLocator/ShowDashAnnouncements/days/<int:days>/Region/<string:Region>')
def ShowDashAnnouncements(days, Region):
    return DashboardHandler().getDailyStatisticsByAnnouncements(days,Region)

@app.route('/ResourceLocator/ShowDashByMatches/days/<int:days>/Region/<string:Region>')
def ShowDashByMatches(days, Region):
    return DashboardHandler().getDailyStatisticsByMatches(days,Region)


#Hasta aqui son nuestras rutas por ahora

if __name__ == '__main__':
    app.run()

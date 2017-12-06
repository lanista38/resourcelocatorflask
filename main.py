from flask import Flask, jsonify, request
from handler.supplier import SupplierHandler
from handler.resourceRequest import RequestHandler
from handler.purchaseReserve import PurchaseHandler
from handler.registration import RegistrationHandler
from handler.dashboard import DashboardHandler
from handler.announcement import AnnouncementHandler

paragraph = '/ResourceLocator/suppliers'
para = '/ResourceLocator/suppliers/<int:sid>'
para1 = '/ResourceLocator/requests/<int:Rid> '
paragraph1 = '/ResourceLocator/requests/<int:RPid>'
parag1 = '/ResourceLocator/purchases'
parag2 = '/ResourceLocator/purchases/<int:Rid>'
paragraph2 = '/ResourceLocator/purchases/<int:RPid>'
paragr1 = '/ResourceLocator/registerAdmin'
paragr2 = '/ResourceLocator/registerSupplier'
paragraph3 = '/ResourceLocator/registerRequester'
paragra1 = '/ResourceLocator/ResourceRequest/Resource/<string:Rname>'
paragraph4 = '/ResourceLocator/AnnounceResource/Resource/<string:Rname>'
paragra2 = '/ResourceLocator/BrowseAnnouncements/'
paragraph5 = '/ResourceLocator/BrowseRequests/'
paragrap1 = '/ResourceLocator/SearchRequests/Resource/<string:Rname>'
paragrap2 = '/ResourceLocator/SearchAnnounce/Resource/<string:Rname>'
paragraph6 = '/ResourceLocator/ShowDashRequests/days/<int:days>/Region/<string:Region>'
paragraph7 = '/ResourceLocator/ShowDashAnnouncements/days/<int:days>/Region/<string:Region>'
paragraph8 = '/ResourceLocator/ShowDashByMatches/days/<int:days>/Region/<string:Region>'

app = Flask(__name__)

@app.route('/')
def greeting():
    return 'List of routes:'+ paragraph + para + para1 + paragraph1 + parag1+parag2+ paragraph2+paragr1+paragr2 + paragraph3+paragra1 + paragraph4+paragra2 + paragraph5+paragrap1+paragrap2 + paragraph6 +paragraph7+paragraph8


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


if __name__ == '__main__':
    app.run()

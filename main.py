from flask import Flask, jsonify, request

from handler.resource import ResourceHandler
from handler.supplier import SupplierHandler
from handler.resourceRequest import RequestHandler
from handler.purchase import PurchaseHandler
from handler.registration import RegistrationHandler
from handler.dashboard import DashboardHandler
from handler.announcement import AnnouncementHandler
from handler.reserve import ReserveHandler
from handler.category import CategoryHandler




app = Flask(__name__)

@app.route('/')
def greeting():
    return ' Welcome to Resource locator app'


@app.route('/ResourceLocator/suppliers')
def getAllSuppliers():
    if not request.args:
        return SupplierHandler().getAllSuppliers()
    else:
        return SupplierHandler().searchSuppliers(request.args)


@app.route('/ResourceLocator/suppliers/<int:sid>')
def getSupplierById(sid):
    return SupplierHandler().getSupplierById(sid)

@app.route('/ResourceLocator/suppliers/<string:company>/town/<string:tname>')
def getSuppliersByTownAndCompany(tname, company):
    return SupplierHandler().searchSuppliers(tname, company)

# Resource Requests routes
@app.route('/ResourceLocator/BrowseRequests/', methods=['GET', 'POST'])
def getAllRequests():
        if request.method == 'POST':
            form = {}
            form['cid'] = request.args.get('cid')
            form['rid'] = request.args.get('rid')
            form['rrqty'] = request.args.get('rrqty')
            form['tid'] = request.args.get('tid')
            return RequestHandler().insertRequest(form)
        else:
            if not request.args:
                return RequestHandler().getAllRequests()

@app.route('/ResourceLocator/requests/<int:rid>', methods=['GET', 'PUT', 'DELETE'])
def getRequestById(rid):
    if request.method == 'GET':
        return RequestHandler().getRequestByRid(Rid)
    elif request.method == 'PUT':
        form = {}
        form['rrqty'] = request.args.get('rrqty')
        form['tid'] = request.args.get('tid')
        return RequestHandler().updateRequest(rid, form)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/ResourceLocator/requests/<int:RPid>')
def getRequestByRPId(Rid):
    return RequestHandler().getRequestByRid(Rid)


#Reserve/Purchase routes

@app.route('/ResourceLocator/purchase')
def getAllPurchases():
    if not request.args:
        return PurchaseHandler().getAllPurchases()
    else:
        return ResourceHandler().search(request.args)

@app.route('/ResourceLocator/purchase/<int:Pid>')
def getPurchaseByRid(Pid):
    return PurchaseHandler().getPurchaseByRid(Pid)

@app.route('/ResourceLocator/purchase/resource/<int:Rid>')
def getPurchaseByResource(Rid):
    return PurchaseHandler().getPurchaseByResource(Rid)

@app.route('/ResourceLocator/purchase/supplier/<int:Sid>')
def getPurchaseBySupplier(Sid):
    return PurchaseHandler().getPurchaseBySupplier(Sid)

@app.route('/ResourceLocator/purchase/customer/<int:Cid>')
def getPurchaseByCustomer(Cid):
    return PurchaseHandler().getPurchaseByCustomer(Cid)

@app.route('/ResourceLocator/reserve/', methods=['GET', 'POST'])
def getAllReservations():
    if request.method == 'POST':
        form = {}
        form['rsqty'] = request.args.get('rsqty')
        form['cid'] = request.args.get('cid')
        form['rid'] = request.args.get('rid')
        form['sid'] = request.args.get('sid')
        form['tid'] = request.args.get('tid')
        return ReserveHandler().reserveResource(form)
    else:
        return ReserveHandler().getAllReserve()

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

@app.route('/ResourceLocator/Announcements/' , methods=['GET', 'POST'])
def getAllAnnouncements():
    if request.method == 'POST':
        form = {}
        form['sid'] = request.args.get('sid')
        form['rid'] = request.args.get('rid')
        form['aprice'] = request.args.get('aprice')
        form['aqty'] = request.args.get('aqty')
        form['tid'] = request.args.get('tid')
        return AnnouncementHandler().insertAnnouncement(form)
    else:
        return AnnouncementHandler().getAllAnnouncements()

@app.route('/ResourceLocator/Announcements/<string:Sname>')
def getAnnouncementsBySupplierName(Sname):
    return AnnouncementHandler().getAnnouncementBySname(Sname)
@app.route('/ResourceLocator/Announcements/<int:Sid>')
def getAnnouncementsBySupplierId(Sid):
    return AnnouncementHandler().getAnnouncementBySid(Sid)


#SEARCH endpoints
#9.Operation Keyword search resources being requested, with sorting by resource name
@app.route('/ResourceLocator/SearchRequests/Resource/<string:Rname>')
def searchRequests(Rname):
    return RequestHandler().getRequestByResource(Rname)

@app.route('/ResourceLocator/SearchAnnounce/Resource/<string:Rname>')
def searchAnnouncements(Rname):
    return AnnouncementHandler().getAnnouncementByResource(Rname)
#7 Operation Browse resources being requested
@app.route('/ResourceLocator/SearchAllRequests/')
def searchRequestsAll():
        return RequestHandler().getAllRequests()
#Operation 15. Encontrar suplidores para un producto dado (e.g., diesel)
@app.route('/ResourceLocator/SearchSupplierByProduct/<string:rname>')
def searchSuppliersByResource(rname):
    return SupplierHandler().getSuppliersByResourceName(rname)



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


#Category routes

@app.route('/ResourceLocator/category')
def getAllCategories():
    return CategoryHandler().getAllCategories()

@app.route('/ResourceLocator/category/<int:Cid>')
def getCategoryByCid(Cid):
    return CategoryHandler().getCategoryByCid(Cid)

@app.route('/ResourceLocator/category/<string:name>')
def getCategoryByCName(name):
    return CategoryHandler().getCategoryByCname(name)

#Resource routes
@app.route('/ResourceLocator/resource', methods=['GET', 'POST'])
def getAllResources():

    if request.method == 'POST':
        form = {}
        form['rname'] = request.args.get('rname')
        form['rstock'] = request.args.get('rstock')
        form['cid'] = request.args.get('cid')
        form['rprice'] = request.args.get('rprice')
        return ResourceHandler().insertResource(form)
    else:
        if not request.args:
            return ResourceHandler().getAllResources()
        else:
            return ResourceHandler().search(request.args)

@app.route('/ResourceLocator/resource/instock')
def getAllResourcesInStock():
#    if not request.args:
    return ResourceHandler().getAllResourcesInStock()
#    else:
#        return ResourceHandler().getResourceInStockByName(request.args)

@app.route('/ResourceLocator/resource/instock/<string:name>')
def getResourceInStockByName(name):
    return ResourceHandler().getResourceInStockByName(name)


@app.route('/ResourceLocator/resource/<int:rid>' , methods=['GET', 'PUT', 'DELETE'])
def getResourceByRid(rid):
    if request.method == 'GET':
        return ResourceHandler().getRequestByRid(rid)
    elif request.method == 'PUT':
        form = {}
        form['rname'] = request.args.get('rname')
        form['rstock'] = request.args.get('rstock')
        form['cid'] = request.args.get('cid')
        form['rprice'] = request.args.get('rprice')
        return ResourceHandler().updateResource(rid, form)
    elif request.method == 'DELETE':
        return ResourceHandler().deleteResource(rid)
    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/ResourceLocator/resource/<string:name>')
def getResourceByName(name):
    return ResourceHandler().getResourceByName(name)

@app.route('/ResourceLocator/resource/category/<int:Rid>')
def getResourcesByCid(Rid):
    return ResourceHandler().getResourcesByCid(Rid)

@app.route('/ResourceLocator/resource/category/<string:name>')
def getResourceByCategoryName(name):
    return ResourceHandler().getResourceByCategoryName(name)

@app.route('/ResourceLocator/resource/<string:name>/supplier/<int:Sid>')
def getResourceBySupplier(name,Sid):
    return ResourceHandler().getResourceBySupplier(name,Sid)

@app.route('/ResourceLocator/resource/<int:rid>/region/<int:tid>')
def getResourceByIdRegion(rid,tid):
    return ResourceHandler().getResourceByIdRegion(rid,tid)


if __name__ == '__main__':
    app.run()

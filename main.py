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
from handler.ccard import CcardHandler
from handler.user import UserHandler
from handler.payment import PaymentHandler
from handler.customer import CustomerHandler
from handler.supplier import SupplierHandler



app = Flask(__name__)

@app.route('/')
def greeting():
    return ' Welcome to Resource locator app'

# Credit Card

@app.route('/ResourceLocator/ccard/', methods=['GET', 'POST'])
def getCcard():
        if request.method == 'POST':
            return CcardHandler().insertCcard(request.json)
        else:
            if not request.args:
                return CcardHandler().getAllCcards()

@app.route('/ResourceLocator/ccard/<int:ccid>', methods=['GET', 'PUT'])
def getCcardById(ccid):
    if request.method == 'GET':
        return CcardHandler().getCcardByccid(ccid)
    elif request.method == 'PUT':
        return CcardHandler().updateCcard(ccid, request.json)
    else:
        return jsonify(Error="Method not allowed."), 405

# Customer
@app.route('/ResourceLocator/customer/register', methods=['POST'])
def getRegisterCustomer():
    if request.method == 'POST':
        return CustomerHandler().registerCustomer(request.json)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/ResourceLocator/customer/user/register', methods=['POST'])
def getRegisterCustomerUser():
    if request.method == 'POST':
        return CustomerHandler().registerCustomerUser(request.json)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/ResourceLocator/customer/')
def getAllCustomers():
    return CustomerHandler().getAllCustomers()

# Supplier
@app.route('/ResourceLocator/supplier/register', methods=['POST'])
def getRegisterSupplier():
    if request.method == 'POST':
        return SupplierHandler().registerSupplier(request.json)
    else:
        return jsonify(Error="Method not allowed."), 405

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

@app.route('/ResourceLocator/supplier/user/register', methods=['POST'])
def getRegisterSupplierUser():
    if request.method == 'POST':
        return SupplierHandler().registerSupplierUser(request.json)
    else:
        return jsonify(Error="Method not allowed."), 405


# User
@app.route('/ResourceLocator/user/register' , methods=['POST'])
def getRegisterUser():
    if request.method == 'POST':
        return UserHandler().registerUser(request.json)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/ResourceLocator/user/')
def getAllUsers():
        return UserHandler().getAllUsers()


# Payment
@app.route('/ResourceLocator/payment/register', methods=['POST'])
def getRegisterPayment():
    if request.method == 'POST':
        return PaymentHandler().registerPayment(request.json)
    else:
        return jsonify(Error="Method not allowed."), 405

# Resource Requests routes
@app.route('/ResourceLocator/BrowseRequests/', methods=['GET', 'POST'])
def getAllRequests():
        if request.method == 'POST':
            return RequestHandler().insertRequest(request.json)
        else:
            if not request.args:
                return RequestHandler().getAllRequests()

@app.route('/ResourceLocator/requests/<int:rid>', methods=['GET', 'PUT', 'DELETE'])
def getRequestById(rid):
    if request.method == 'GET':
        return RequestHandler().getRequestByRid(rid)
    elif request.method == 'PUT':
        return RequestHandler().updateRequest(rid, request.json)
    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/ResourceLocator/requests/<int:RPid>')
def getRequestByRPId(RPid):
    return RequestHandler().getRequestByRid(RPid)

@app.route('/ResourceLocator/requests/<string:rname>')
def getRequestByRname(rname):
    return RequestHandler().getRequestByResource(rname)



#Reserve/Purchase routes

@app.route('/ResourceLocator/purchase', methods=['GET', 'POST'])
def getAllPurchases():
    if request.method == 'POST':
        return PurchaseHandler().insertPurchase(request.json)
    else:
        if not request.args:
            return PurchaseHandler().getAllPurchases()

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
        return ReserveHandler().reserveResource(request.json)
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
    return AnnouncementHandler().getAnnouncementByResourceName(Rname)

@app.route('/ResourceLocator/Announcements/' , methods=['GET', 'POST'])
def getAllAnnouncements():
    if request.method == 'POST':
        return AnnouncementHandler().insertAnnouncement(request.json)
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
    return AnnouncementHandler().getAnnouncementByResourceName(Rname)
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

@app.route('/ResourceLocator/resource', methods=['GET', 'POST'])
def getAllResources():
    if request.method == 'POST':
        return ResourceHandler().insertResource(request.json)
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
        return ResourceHandler().getResourceByRid(rid)
    elif request.method == 'PUT':
        return ResourceHandler().updateResource(rid, request.json)
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

@app.route('/ResourceLocator/resource/<int:rid>/supplier/<int:Sid>')
def getResourceBySupplier(rid,Sid):
    return ResourceHandler().getResourceBySupplier(rid,Sid)

@app.route('/ResourceLocator/resource/<int:rid>/region/<int:tid>')
def getResourceByIdRegion(rid,tid):
    return ResourceHandler().getResourceByIdRegion(rid,tid)


if __name__ == '__main__':
    app.run()

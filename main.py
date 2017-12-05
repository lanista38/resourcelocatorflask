from flask import Flask, jsonify, request
from handler.registration import RegistrationHandler
from handler.ResourceRequest import RequestHandler
from handler.dashboard import DashboardHandler
from handler.announcement import AnnouncementHandler


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

@app.route('/BrowseAnnouncements/')
def getAllAnnouncements():
    return AnnouncementHandler().getAllAnnouncements()

@app.route('/BrowseRequests/')
def getAllRequests():
    return R equestHandler().getAllRequests()

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

#Hasta aqui son nuestras rutas por ahora

if __name__ == '__main__':
    app.run()

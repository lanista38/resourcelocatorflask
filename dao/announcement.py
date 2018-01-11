from config.dbconfig import pg_config
import psycopg2

class AnnouncementDAO:
    def __init__(self):
        connection_url = "host=%s dbname=%s user=%s password=%s" % (pg_config['hostname'], pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])


        self.conn = psycopg2._connect(connection_url)


    def getAllAnnouncements(self):
        cursor = self.conn.cursor()
        query = "select * from Announcement ;"
        result = []
        cursor.execute(query)
        for row in cursor:
            result.append(row)
        return result


    def getAnnouncementBySupplier(self,Sname):
        cursor = self.conn.cursor()
        query = "select * from Announcement natural inner join Supplier where name ilike %(like)s;"
        result = []
        cursor.execute(query,dict(like= '%'+ Sname+'%'))
        for row in cursor:
            result.append(row)
        return result

    def getAnnouncementBySid(self,Sid):
        cursor = self.conn.cursor()
        query = "select * from Announcement natural inner join Supplier where Sid = %s;"
        result = []
        cursor.execute(query,(Sid,))
        for row in cursor:
            result.append(row)
        return result

    def getAnnouncementByResource(self, Rid):
        cursor = self.conn.cursor()
        query = "select * from Announcement where Rid = %s;"
        result = []
        cursor.execute(query,(Rid,))
        for row in cursor:
            result.append(row)
        return result
#Operation 8
    def getAllResourcesAnnounced(self):
        cursor = self.conn.cursor()
        query = "select * from Announcement natural inner join Resource;"
        result = []
        cursor.excecute(query)
        for row in cursor:
            result.append(row)
        return result

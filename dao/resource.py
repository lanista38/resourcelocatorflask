from config.dbconfig import pg_config
#final
import psycopg2

class ResourceDAO:
    def __init__(self):
        connection_url = "host=%s dbname=%s user=%s password=%s" % (pg_config['hostname'], pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllResources(self):
        cursor = self.conn.cursor()
        query = "select * from Resource;"
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceByRid(self, Rid):
        cursor = self.conn.cursor()
        query = "select * from Resource where Rid = %s;"
        cursor.execute(query, (Rid,))
        result = cursor.fetchone()
        return result

    def getAllResourcesByCategoryId(self, Cid):
        cursor = self.conn.cursor()
        query = "select * from Resource where Cid=%s;"
        cursor.execute(query, (Cid,))
        result = []
        for row in cursor:
            result.append(row)
        return result
    def getAllResourcesByCategoryName(self, Cname):
        cursor = self.conn.cursor()
        query = "select * from Resource natural inner join Category where Cname=%s;"
        cursor.execute(query, (Cname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    #Operation 14
    def getResourceBySupplier(self,Sid):
        cursor = self.conn.cursor()
        query = "select * from Resource natural inner join Supplier where Sid = %s;"
        cursor.execute(query,(Pid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # To-Do
    #Operation 16
    def getResourceByRegion(self,Rid,Rregion):
        cursor = self.conn.cursor()
        query ="select * from Resource natural inner join Announcement where Rid = %s and Rregion = %s;"
        cursor.execute(query,(Rid,Rregion))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # To-Do
    def geAllResourcesByRegion(self,Rregion):
        cursor = self.conn.cursor()
        query ="select * from Resource natural inner join Announcement where Rregion = %s;"
        cursor.execute(query,(Rid,Rregion))
        result = []
        for row in cursor:
            result.append(row)
        return result

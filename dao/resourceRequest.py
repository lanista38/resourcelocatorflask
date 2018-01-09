from config.dbconfig import pg_config
import psycopg2

class ResourceRequestDAO:
    def __init__(self):

# Operation 7
    def getAllRequests(self):
        cursor = self.conn.cursor()
        query = "select * from ResourceRequest"
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestByRid(self, Rid):
        cursor = self.conn.cursor()
        query = "select * from ResourceRequest where Rid = %s;"
        cursor.execute(query, (Rid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestByResource(self, Rname):
        cursor = self.conn.cursor()
        query = "select * from ResourceRequest where Rname = %s;"
        cursor.execute(query, (Rname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

from config.dbconfig import pg_config
import psycopg2

class ResourceRequestDAO:
    def __init__(self):
        connection_url = "host=%s dbname=%s user=%s password=%s" % (pg_config['hostname'], pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
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
        query = "select * from Request where Rid = %s;"
        cursor.execute(query, (Rid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestByResource(self, rname):
        cursor = self.conn.cursor()
        query = "select * from request natural inner join resource where rname = %s;"
        cursor.execute(query, (rname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

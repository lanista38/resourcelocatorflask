from config.dbconfig import pg_config
import psycopg2

class ResourceRequestDAO:
    def __init__(self):
        connection_url = "host=%s dbname=%s user=%s password=%s" % (pg_config['hostname'], pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)


    def insertRequest(self, cid, rid, rrqty, tid):
        cursor = self.conn.cursor()
        query = "insert into request(cid, rid, rrqty, tid) values (%s, %s, %s, %s) returning rid;"
        cursor.execute(query, (cid, rid, rrqty, tid,))
        rid = cursor.fetchone()[0]
        self.conn.commit()
        return rid

    def deleteRequest(self, cid, rid):
        cursor = self.conn.cursor()
        query = "delete from request where rid = %s and cid =%s;"
        cursor.execute(query, (rid, cid,))
        self.conn.commit()
        return rid

    def updateRequest(self, rrqty, tid):
        cursor = self.conn.cursor()
        query = "update Resource set rrqty = %s, tid = %s where rid = %s and cid = %s;"
        cursor.execute(query, (rname, rstock, cid, rprice, rid,))
        self.conn.commit()
        return rid
# Operation 7
    def getAllRequests(self):
        cursor = self.conn.cursor()
        query = "select * from Request"
        cursor.execute(query)
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
        query = "select * from request r inner join resource rr on r.rid=rr.rid where rname = %s;"
        cursor.execute(query, (rname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

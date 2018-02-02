from config.dbconfig import pg_config

import psycopg2

class ResourceDAO:
    def __init__(self):
        connection_url = "host=%s dbname=%s user=%s password=%s" % (pg_config['hostname'], pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def insertResource(self, rname, cid):
        cursor = self.conn.cursor()
        query = "insert into Resource(rname, cid) values (%s, %s) returning rid;"
        cursor.execute(query, (rname, cid,))
        rid = cursor.fetchone()[0]
        self.conn.commit()
        return rid

    def deleteResource(self, rid):
        cursor = self.conn.cursor()
        query = "delete from Resource where rid = %s;"
        cursor.execute(query, (rid,))
        self.conn.commit()
        return rid

    def updateResource(self, rid, rname, cid):
        cursor = self.conn.cursor()
        query = "update Resource set rname = %s, cid = %s where rid = %s;"
        cursor.execute(query, (rname, cid, rid,))
        self.conn.commit()
        return rid

    def getAllResources(self):
        cursor = self.conn.cursor()
        query = "select * from resource;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result
        #operation 8 --> resources Available, will not work now
    def getAllResourcesInStock(self):
        cursor = self.conn.cursor()
        query = "select * from resource where rstock > 0;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result
            #resources Available, will not work now
    def getResourceInStockByName(self, rname):
        cursor = self.conn.cursor()
        query = "select * from resource where rstock > 0 and rname ilike %(like)s;"
        cursor.execute(query, dict(like= '%'+rname+'%'))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceByRid(self, Rid):
        cursor = self.conn.cursor()
        query = "select * from resource where rid = %s;"
        cursor.execute(query,[Rid])
        result = cursor.fetchone()
        return result

    def getResourceByRname(self, Rname):
        cursor = self.conn.cursor()
        query = "select * from resource where rname ilike %(like)s;"
        cursor.execute(query,dict(like= '%'+Rname+'%'))
        result = []
        for row in cursor:
            result.append(row)
        return result

    #Operation 14
    def getResourceBySupplier(self,Rid,Sid):
        cursor = self.conn.cursor()
        query = "select r.rid,r.rname,rt.stock,t.tname from town t natural join res_tow_sup rt natural join resource r natural join supplier s where (r.rid=%s or r.rname=%s) and s.sid=%s;"
        cursor.execute(query,(Rid,Rid,Sid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceByCid(self, cid):
        cursor = self.conn.cursor()
        query = "select * from resource where cid = %s;"
        cursor.execute(query,[cid])
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceByPrice(self, rprice):
        cursor = self.conn.cursor()
        query = "select * from resource where rprice = %s;"
        cursor.execute(query,[rprice])
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceByPriceCid(self, rprice,cid):
        cursor = self.conn.cursor()
        query = "select * from resource where rprice = %s and cid = %s;"
        cursor.execute(query,[rprice,cid])
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceByCategoryName(self, Cname):
        cursor = self.conn.cursor()
        query = "select r.* from resource r natural join category c where c.cname ilike %(like)s;"
        cursor.execute(query,dict(like='%'+Cname+'%'))
        result = []
        for row in cursor:
            result.append(row)
        return result


    #Operation 16
    def getResourceByIdRegion(self,Rid,Tid):
        cursor = self.conn.cursor()
        query = "select * from resource r natural join res_tow_sup rts where r.rid=%s and rts.tid=%s;"
        cursor.execute(query,[Rid,Tid])
        result = []
        for row in cursor:
            result.append(row)
        return result

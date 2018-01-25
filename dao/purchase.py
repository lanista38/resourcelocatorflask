from config.dbconfig import pg_config
import psycopg2

class PurchaseDAO:
    def __init__(self):
        connection_url = "host=%s dbname=%s user=%s password=%s" % (pg_config['hostname'], pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllPurchases(self):
        cursor = self.conn.cursor()
        query = "select * from purchase;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getPurchaseByPid(self,Pid):
        cursor = self.conn.cursor()
        query = "select * from purchase where pid = %s;"
        cursor.execute(query,[Pid])
        result = cursor.fetchone()
        return result

    def getPurchaseByResource(self,Rid):
        cursor = self.conn.cursor()
        query = "select * from purchase p natural join resource r where r.rid = %s ;"
        cursor.execute(query,[Rid])
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getPurchaseByCustomer(self,Cid):
        cursor = self.conn.cursor()
        query = "select * from purchase p natural join customer c where c.cid = %s ;"
        cursor.execute(query,[Cid])
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSearch(self,args):
        cursor = self.conn.cursor()
        customer = args.get("customer")
        supplier = args.get("supplier")
        resource = args.get("resource")
        query = "select p.* from purchase p join customer c using(cid) join resource r using(rid) join supplier s using(sid);"
        parts_list = []
        if customer:
            customer = "c.cid="+customer;
        if supplier:
            supplier = "s.cid="+supplier;
        if resource:
            resource = "r.cid="+resource;
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insertPurchase(self, pqty, pprice, cid, rid, sid):
        cursor = self.conn.cursor()
        query = "insert into purchase(pqty, pprice, cid, rid, sid) values(%s,%s,%s,%s,%s) returning pid;"
        cursor.execute(query,(pqty, pprice, cid, rid, sid))
        pid = cursor.fetchone()[0]
        self.conn.commit()
        return pid

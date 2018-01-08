from config.dbconfig import pg_config
import psycopg2

class SupplierDAO:
    def __init__(self):

    def getAllSuppliers(self):
        cursor = self.conn.cursor()
        query = "select * from Supplier"
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierById(self, sid):
            cursor = self.conn.cursor()
            query = "select * from Supplier where Pid = %s;"
            cursor.execute(query, (pid,))
            result = []
            for row in cursor:
                result.append(row)
            return result


    def getSuppliersByRegion(self, region):
        cursor = self.conn.cursor()
        query = "select * from Supplier where region = %s;"
        cursor.execute(query, (region,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersByResourceId(self, Rid):
        cursor = self.conn.cursor()
        query = "select Pid, name, lastname, address, region from Resource natural inner join Supplier natural inner join Announcement where Rid = %s;"
        cursor.execute(query, (Rid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    #Operation 15
    def getSupplierByResource(self,Rid):
        cursor = self.conn.cursor()
        query =" select * from Person natural inner join Announcement where Rid = %s;"
        cursor.execute(query,(Rid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

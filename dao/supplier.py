from config.dbconfig import pg_config
import psycopg2

class SupplierDAO:
    def __init__(self):
        connection_url = "host=%s dbname=%s user=%s password=%s" % (pg_config['hostname'], pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllSuppliers(self):
        cursor = self.conn.cursor()
        query = "select* from supplier;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierById(self, Sid):
            cursor = self.conn.cursor()
            query = "select * from Supplier where Sid = %s;"
            cursor.execute(query, (Sid,))
            result = []
            for row in cursor:
                result.append(row)
            return result

    #to-do
    def getSuppliersByTown(self, tname):
        cursor = self.conn.cursor()
        query = "select * from Supplier natural inner join Town where tname = %s;"
        cursor.execute(query, (tname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersByCompany(self, company):
        cursor = self.conn.cursor()
        query = "select * from Supplier where company= %s;"
        cursor.execute(query, (company,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersByTownAndCompany(self, tname, company):
        cursor = self.conn.cursor()
        query = "select * from Supplier natural inner join Town where tname = %s and where company = %s;"
        cursor.execute(query, (tname, company))
        result = []
        for row in cursor:
            result.append(row)
        return result

    #Operation 15  change selects
    def getSuppliersByResourceId(self, Rid):
        cursor = self.conn.cursor()
        query = "select Sid, name, lastname, address, tid from Resource natural inner join Supplier natural inner join Announcement where Rid = %s;"
        cursor.execute(query, (Rid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

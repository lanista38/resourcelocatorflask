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
            query = "select * from supplier where sid = %s;"
            cursor.execute(query, (Sid,))
            result = []
            for row in cursor:
                result.append(row)
            return result

    #to-do
    def getSuppliersByTown(self, tname):
        cursor = self.conn.cursor()
        query = "select * from supplier natural inner join Town where tname = %s;"
        cursor.execute(query, (tname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # def getSuppliersByCompany(self, company):
    #     cursor = self.conn.cursor()
    #     query = "select * from upplier where company= %s;"
    #     cursor.execute(query, (company,))
    #     result = []
    #     for row in cursor:
    #         result.append(row)
    #     return result

    def getSuppliersByTown(self, tname):
        cursor = self.conn.cursor()
        query = "select * from supplier natural inner join town where tname = %s;"
        cursor.execute(query, (tname, company))
        result = []
        for row in cursor:
            result.append(row)
        return result

    #Operation 15  change selects
    def getSuppliersByResourceID(self, Rid):
        cursor = self.conn.cursor()
        query = "select * from supplier natural inner join announcement where rid = %s;"
        cursor.execute(query, (Rid,))
        result = []
        for row in cursor:
            result.append(row)
        return result
    def getSuppliersByResourceName(self, rname):
        cursor = self.conn.cursor()
        query = "select * from supplier natural inner join announcement natural inner join Resource where rname = %s;"
        cursor.execute(query, (rname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def registerSupplier(self, name, lastname, company, gpsy, gpsx, address, tid):
        cursor = self.conn.cursor()
        query ="INSERT INTO supplier(name, lastname, company, gpsy, gpsx, address, tid) VALUES (%s, %s, %s, %s, %s, %s, %s) returning sid;"
        cursor.execute(query, (name, lastname, company, gpsy, gpsx, address, tid))
        puid = cursor.fetchone()[0]
        self.conn.commit()
        return puid
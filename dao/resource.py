from config.dbconfig import pg_config

import psycopg2

class ResourceDAO:
    def __init__(self):
        connection_url = "host=%s dbname=%s user=%s password=%s" % (pg_config['hostname'], pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllResources(self):
        cursor = self.conn.cursor()
        query = 'select * from flask_schema.resource;'
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceByRid(self, Rid):
        cursor = self.conn.cursor()
        query = 'select * from flask_schema.resource where Rid = %s;'
        cursor.execute(query, (Rid,))
        result = cursor.fetchone()
        return result

    def getResourceByCid(self, cid):
        cursor = self.conn.cursor()
        query = 'select* from flask_schema.resource where Cid = %s;'
        cursor.execute(query, (cid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceByCategoryName(self, Cname):
        cursor = self.conn.cursor()
        query = 'select* from flask_schema.resource where Cname = %s;'
        cursor.execute(query, (Cname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceByName(self, Rname):
        cursor = self.conn.cursor()
        query = 'select* from flask_schema.resource where Rname = %s;'
        cursor.execute(query, (Rname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

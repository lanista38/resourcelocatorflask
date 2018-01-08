from config.dbconfig import pg_config

import psycopg2

class CategoryDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllCategories(self):
        cursor = self.conn.cursor()
        query = "select * from Category;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    #Operations 7 & 8 from email
    def getAllCategoryByRequest(self):
        cursor = self.conn.cursor()
        query = "select * from Category natural inner join ResourceRequest;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllCategoryByAvailability(self):
        cursor = self.conn.cursor()
        query = "select * from Category natural inner join Announcement;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    #Operations 9 & 10 from email
    def getCategoryByKeywordRequest(self,Cname):
        cursor = self.conn.cursor()
        query = "select * from Category where Cname = %s from Category natural inner join ResourceRequest;"
        cursor.execute(query,(Cname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCategoryByKeyWordAvailability(self,Cname):
        cursor = self.conn.cursor()
        query = "select * from Category where Cname = %s from Category natural inner join Announcement;"
        cursor.execute(query,(Cname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

from config.dbconfig import pg_config

import psycopg2

class CategoryDAO:
    def __init__(self):
        connection_url = "host=%s dbname=%s user=%s password=%s" % (pg_config['hostname'], pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2.connect(connection_url)

    def getAllCategories(self):
        cursor = self.conn.cursor()
        query = "select * from Category;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result
    def getCategoryByCid(self, Cid):
        cursor = self.conn.cursor()
        query = "select * from Category where Cid=%s;"
        cursor.execute(query, (Cid,))
        result = cursor.fetchone()
        return result

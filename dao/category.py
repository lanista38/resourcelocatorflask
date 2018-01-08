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
        result = []
        for row in cursor:
            result.append(row)
        return result

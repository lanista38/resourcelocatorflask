from config.dbconfig import pg_config
import psycopg2

class UserDAO:
    def __init__(self):
        connection_url = "host=%s dbname=%s user=%s password=%s" % (pg_config['hostname'], pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2.connect(connection_url)

    def registerUser(self, username, password, cid, sid):
        cursor = self.conn.cursor()
        query ="insert into puser(username, password, cid, sid) values(%s, %s, %s, %s) returning puid;"
        if sid is None:
            cursor.execute(query, (username, password, cid, None))
        elif cid is None:
            cursor.execute(query, (username, password, None, sid))
        else:
            cursor.execute(query, (username, password, cid, sid))
        puid = cursor.fetchone()[0]
        self.conn.commit()
        return puid


    def getAllUsers(self):
        cursor = self.conn.cursor()
        query = "select * from puser;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

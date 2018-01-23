from config.dbconfig import pg_config
import psycopg2

class ReserveDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])

    self.conn = psycopg2._connect(connection_url)
    def registerNewPerson(self, username, password):
        cursor = self.conn.cursor()
        query ="insert into puser(username, password) value(%s,%s) returning puid;"
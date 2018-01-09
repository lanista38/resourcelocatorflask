from config.dbconfig import pg_config
import psycopg2

class AnnouncementDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])

#Operation 18
        self.conn = psycopg2._connect(connection_url)

        def getAllAnnouncements(self):
            cursor = self.conn.cursor()
            query = "select * from Announcement;"
            result = []
            cursor.execute(query)
            for row in cursor:
                result.append(row)
            return result

        def getAnnouncementByPid(self,Pid):
            cursor = self.conn.cursor()
            query = "select * from Announcement where Pid = %s;"
            cursor.execute(query,(Pid,))
            for row in cursor:
                result.append(row)
            return result

from config.dbconfig import pg_config
import psycopg2

class ReserveDAO:
    def __init__(self):
        connection_url = "host=%s dbname=%s user=%s password=%s" % (pg_config['hostname'], pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllReservations(self):
        cursor = self.conn.cursor()
        query = "select * from Reserve;"
        result = []
        cursor.execute(query)
        for row in cursor:
            result.append(row)
        return result

    def getAnnouncementByPid(self,Pid):
        cursor = self.conn.cursor()
        query = "select * from Reserve where Pid = %s;"
        cursor.execute(query,(Pid,))
        for row in cursor:
            result.append(row)
        return result

    def  reserveResource(self, rsqty, cid, rid, sid, tid):
        cursor = self.conn.cursor()
        query = "insert into Reserve(rsqty, cid, rid, sid, tid) values (%s, %s, %s, %s, %s) returning rsid;"
        cursor.execute(query, (rsqty, cid, rid, sid, tid))
        rsid = cursor.fetchone()[0]
        self.conn.commit()
        return rsid

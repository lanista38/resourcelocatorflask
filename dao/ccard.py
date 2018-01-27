from config.dbconfig import pg_config

import psycopg2

class CcardDAO:
    def __init__(self):
        connection_url = "host=%s dbname=%s user=%s password=%s" % (pg_config['hostname'], pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def insertCcard(self, number, cvv, name, expiration,cid):
        cursor = self.conn.cursor()
        query = "insert into Ccard(number, cvv, name, expiration,cid) values (%s, %s, %s, %s, %s) returning ccid;"
        cursor.execute(query, (number, cvv, name, expiration,cid))
        ccid = cursor.fetchone()[0]
        self.conn.commit()
        return ccid

    def deleteCcard(self, ccid):
        cursor = self.conn.cursor()
        query = "delete from Ccard where ccid = %s;"
        cursor.execute(query, (ccid,))
        self.conn.commit()
        return ccid

    def updateCcard(self, ccid, number, cvv, name, expiration,cid):
        cursor = self.conn.cursor()
        query = "update Ccard set number = %s, cvv = %s, name = %s, expiration = %s, cid= %s where ccid = %s;"
        cursor.execute(query, (number, cvv, name, expiration,cid,ccid))
        self.conn.commit()
        return ccid

    def getAllCcards(self):
        cursor = self.conn.cursor()
        query = "select * from ccard;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCcardByccid(self, ccid):
        cursor = self.conn.cursor()
        query = "select * from ccard where ccid = %s;"
        cursor.execute(query,[ccid])
        result = cursor.fetchone()
        return result


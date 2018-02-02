from config.dbconfig import pg_config
import psycopg2

class CustomerDAO:
    def __init__(self):
        connection_url = "host=%s dbname=%s user=%s password=%s" % (pg_config['hostname'], pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2.connect(connection_url)

    def registerCustomer(self, name, lastname, gpsy, gpsx, address, tid):
        cursor = self.conn.cursor()
        query ="INSERT INTO customer(name, lastname, gpsy, gpsx, address, tid) VALUES (%s, %s, %s, %s, %s, %s) returning cid;"
        cursor.execute(query, (name, lastname, gpsy, gpsx, address, tid))
        puid = cursor.fetchone()[0]
        self.conn.commit()
        return puid


    def getAllCustomers(self):
        cursor = self.conn.cursor()
        query = "select * from customer;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

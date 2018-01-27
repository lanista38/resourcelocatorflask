from config.dbconfig import pg_config
import psycopg2

class PaymentDAO:
    def __init__(self):
        connection_url = "host=%s dbname=%s user=%s password=%s" % (pg_config['hostname'], pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2.connect(connection_url)

    def registerPayment(self, tipo, ccid, pid):
        cursor = self.conn.cursor()
        query ="INSERT INTO public.payment(tipo, ccid, pid) VALUES (%s, %s, %s) returning payid;"
        cursor.execute(query, (tipo, ccid, pid))
        puid = cursor.fetchone()[0]
        self.conn.commit()
        return puid


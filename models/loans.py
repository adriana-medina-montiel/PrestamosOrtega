from .db import get_connection

mydb = get_connection()

class Loan:

    def __init__(self, id_cliente, monto, periodo, modalidad_pago, fecha_in , id_prestamo = None):
        self.id_prestamo = id_prestamo
        self.id_cliente = id_cliente
        self.monto = monto
        self.periodo = periodo
        self.modalidad_pago = modalidad_pago
        self.fecha_in = fecha_in

    def save(self):
        if self.id_prestamo is None:
            with mydb.cursor() as cursor:
                sql = "INSERT INTO prestamos (id_cliente, monto, periodo, modalidad_pago, fecha_in) VALUES (%s, %s, %s, %s, %s)"
                val = (self.id_cliente, self.monto, self.periodo, self.modalidad_pago, self.fecha_in)
                cursor.execute(sql, val)
                mydb.commit()
                self.id_prestamo = cursor.lastrowid
                return self.id_prestamo
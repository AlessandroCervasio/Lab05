# Add whatever it is needed to interface with the DB Table studente

from database.DB_connect import get_connection
from model.studente import Studente


class studente_DAO:
    @staticmethod
    def getStudentiDiUnCorso(codins):
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT s.matricola, s.cognome, s.nome, s.cds
                            FROM studente s
                            JOIN iscrizione i
                            ON s.matricola=i.matricola
                            WHERE i.codins=%s

                """
        cursor.execute(query,(codins,))
        res = []
        for row in cursor:
            res.append(Studente(matricola=row["matricola"],
                             cognome=row["cognome"],
                             nome=row["nome"],
                             cds=row["cds"]))
        cursor.close()
        cnx.close()
        return res




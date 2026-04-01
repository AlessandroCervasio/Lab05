# Add whatever it is needed to interface with the DB Table corso

from database.DB_connect import get_connection
from model.corso import Corso


class corso_DAO:
    @staticmethod
    def getAllCorsi():
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """select *
                            from corso

                """
        cursor.execute(query)
        res = []
        for row in cursor:
            res.append(Corso(codIns=row["codins"],
                             crediti=row["crediti"],
                             nome=row["nome"],
                             pd=row["pd"]))
        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getCorsiwMatricola(matricola):
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """select c.*
                    from corso c, iscrizione i
                    where c.codins =i.codins 
                    and i.matricola=%s
                    """
        cursor.execute(query,(matricola,))

        res = []
        for row in cursor:
            res.append(Corso(codIns=row["codins"],
                             crediti=row["crediti"],
                             nome=row["nome"],
                             pd=row["pd"]))


        cursor.close()
        cnx.close()
        return res


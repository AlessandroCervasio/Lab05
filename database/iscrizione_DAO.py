from database.DB_connect import get_connection
from model.iscrizione import Iscrizione
class iscrizione_DAO:
    @staticmethod
    def aggiungiIscrizione(matricola, codins):
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """insert into iscrizione
                    (matricola, codins)
                    values(%s, %s )

                        """
        cursor.execute(query, (matricola,codins))

        cnx.commit()
        cursor.close()
        cnx.close()
        return

    @staticmethod
    def iscrizioneEsiste(matricola, codins):
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """select *
                    from iscrizione
                    where matricola=%s and codins=%s

                            """
        cursor.execute(query, (matricola, codins))
        row = cursor.fetchone()

        if row is None:
            res= False
        else:
            res= True

        cnx.commit()
        cursor.close()
        cnx.close()
        return res
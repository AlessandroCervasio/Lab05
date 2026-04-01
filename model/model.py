from database.corso_DAO import corso_DAO as cd
from database.studente_DAO import studente_DAO as sd
from database.iscrizione_DAO import iscrizione_DAO as id

class Model:
    def __init__(self):
        pass

    def getAllCorsi(self):
        res=cd.getAllCorsi()
        return res

    def getStudentiDiUnCorso(self, codins):
        res=sd.getStudentiDiUnCorso(codins)
        return res

    def getStudenteConMatricola(self, matricola):
        res=sd.getStudenteConMatricola(matricola)
        return res

    def getCorsiwMatricola(self, matricola):
        lista=cd.getCorsiwMatricola(matricola)
        return lista

    def aggiungiIscrizione(self, matricola, codins):
        esiste=id.iscrizioneEsiste(matricola,codins)
        if esiste:
            return False
        else:
            id.aggiungiIscrizione(matricola,codins)
            return True
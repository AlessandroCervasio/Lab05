from database.corso_DAO import corso_DAO as cd
from database.studente_DAO import studente_DAO as sd

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
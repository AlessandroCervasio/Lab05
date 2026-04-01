from dataclasses import dataclass


@dataclass
class Corso:
    codIns:str
    crediti:int
    nome:str
    pd:int

    def __eq__(self, other):
        self.codIns==other.codIns

    def __hash__(self):
        return hash(self.codIns)
    def __str__(self):
        return f"{self.nome} ({self.codIns})"



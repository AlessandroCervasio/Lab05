from dataclasses import dataclass


@dataclass
class Iscrizione:
    matricola:int
    codins:str

    def __eq__(self, other):
        (self.codins, self.matricola)==(other.codins, other.mtricola)

    def __hash__(self):
        return hash((self.codins, self.matricola))
    def __str__(self):
        return f"{self.matricola} ({self.codins})"
from abc import ABC, abstractmethod
from datetime import datetime

class Auto(ABC):
    def __init__(self, rendszam, tipus, berleti_dij):
        self.rendszam = rendszam
        self.tipus = tipus
        self.berleti_dij = berleti_dij

    @abstractmethod
    def __str__(self):
        pass
class Szemelyauto(Auto):
    def __init__(self, rendszam, tipus, berleti_dij, ulesek_szama):
        super().__init__(rendszam, tipus, berleti_dij)
        self.ulesek_szama = ulesek_szama

    def __str__(self):
        return f"Személyautó: {self.rendszam}, {self.tipus}, {self.berleti_dij} Ft/nap, {self.ulesek_szama} ülés"

class Teherauto(Auto):
    def __init__(self, rendszam, tipus, berleti_dij, teherbiras):
        super().__init__(rendszam, tipus, berleti_dij)
        self.teherbiras = teherbiras

    def __str__(self):
        return f"Teherautó: {self.rendszam}, {self.tipus}, {self.berleti_dij} Ft/nap, {self.teherbiras} kg"
    
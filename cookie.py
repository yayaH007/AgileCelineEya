# from dataclasses import dataclass
from marque import Marque


# @dataclass
class Cookie:
    marque: Marque
    gout: str
    nb_pepites_choco: int
    infos_cookie: str = 'La marque du cookie est '

    def __init__(self,gout,nb_pepites_choco=100):
        self.gout = gout
        self.nb_pepites_choco = nb_pepites_choco

    def get_gout(self):
        return self.gout

    def get_nb_pepites_choco(self):
        return self.nb_pepites_choco

    def set_gout(self, gout):
        self.gout = gout

    def set_nb_pepites_choco(self, nb_pepites_choco):
        self.nb_pepites_choco = nb_pepites_choco

    def get_informations_cookie(self):
        return self.infos_cookie + self.marque.get_nom()

    def get_gout_pepite(self):
        if (self.gout == "choco"):
            return 100
        if (self.gout == "sans choco"):
            return 0



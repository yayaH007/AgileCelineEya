# from dataclasses import dataclass

# @dataclass
class Marque:
    nom: str

    def __init__(self):
        self.nom = "Granola"

    def get_nom(self):
        return self.nom

    def set_nom(self, nom):
        self.nom = nom

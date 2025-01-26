# livre.py

class Livre:
    def __init__(self, titre, auteur, annee_publication):
        if not titre or not auteur:
            raise ValueError("Le titre et l'auteur ne peuvent pas être vides.")
        self.titre = titre
        self.auteur = auteur
        self.annee_publication = annee_publication

    def __str__(self):
        return f"{self.titre} de {self.auteur} ({self.annee_publication})"

# bibliotheque.py

from livre import Livre

class Bibliotheque:
    def __init__(self):
        self.livres = []

    # def ajouter_livre(self, livre):
    #     """Ajoute un livre à la bibliothèque."""
    #     self.livres.append(livre)


    def ajouter_livre(self, livre):
            """Ajoute un livre à la bibliothèque s'il n'est pas déjà présent."""
            for l in self.livres:
                if l.titre.lower() == livre.titre.lower():  # Vérification par titre
                    return False  # Retourne False si le livre existe déjà
            self.livres.append(livre)
            return True  # Retourne True si le livre est ajouté avec succès

    def supprimer_livre(self, titre):
        """Supprime un livre de la bibliothèque par son titre."""
        self.livres = [livre for livre in self.livres if livre.titre != titre]

    def charger_livres(self, fichier):
        """Charge les livres depuis le fichier texte."""
        try:
            with open(fichier, "r" ,errors="replace") as f:
                for line in f:
                    titre, auteur, annee_publication = line.strip().split(';')
                    self.ajouter_livre(Livre(titre, auteur, int(annee_publication)))
        except FileNotFoundError:
            print(f"Le fichier {fichier} n'existe pas.")

    def sauvegarder_livres(self, fichier):
        """Sauvegarde les livres dans le fichier texte en UTF-8."""
        try:
            with open(fichier, 'w') as f:
                for livre in self.livres:
                    f.write(f"{livre.titre};{livre.auteur};{livre.annee_publication}\n")
            print(f"Les livres ont été sauvegardés dans {fichier}.")
        except Exception as e:
            print(f"Erreur lors de la sauvegarde : {e}")


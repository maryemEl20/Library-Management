from flask import Flask, render_template, request, redirect, url_for, flash
import pdfkit
from bibliotheque import Bibliotheque
from livre import Livre  # Importer la classe Livre 
from datetime import datetime


app = Flask(__name__)

app.secret_key = '12345'  # Nécessaire pour utiliser flash

# Crée une instance de la bibliothèque
bibliotheque = Bibliotheque()
 
# Charger les livres au démarrage de l'application
fichier = 'biblio.txt'
bibliotheque.charger_livres(fichier) 

@app.route('/')
def index():
    # Afficher tous les livres dans la bibliothèque
    return render_template('index.html', livres=bibliotheque.livres)

# app.py

@app.route('/ajouter', methods=['GET', 'POST'])
def ajouter_livre():
    if request.method == 'POST':
        # Récupérer les informations soumises par le formulaire
        titre = request.form['titre']
        auteur = request.form['auteur']
        annee_publication = int(request.form['annee_publication'])

        # Créer un nouvel objet Livre avec les données du formulaire
        livre = Livre(titre, auteur, annee_publication)

        # Ajouter ce livre à la bibliothèque
        bibliotheque.ajouter_livre(livre)

        # Sauvegarder la bibliothèque dans le fichier après l'ajout
        bibliotheque.sauvegarder_livres(fichier)
        # Flash success message
        flash(f"The book '{titre}' has been added successfully.", "success")
        
        
        # Rediriger l'utilisateur vers la page d'accueil (ou index)
        return render_template('ajout.html')  # Rester sur la même page après l'ajout

    return render_template('ajout.html')

@app.route('/supprimer/<titre>')
def supprimer_livre(titre):
    bibliotheque.supprimer_livre(titre)  # Supprimer le livre de la bibliothèque
    # Sauvegarder après la suppression
    bibliotheque.sauvegarder_livres(fichier)
    
    flash(f"The book '{titre}' has been deleted successfully!", "success")
    return redirect(url_for('lister_livres'))


@app.route('/lister')
def lister_livres():
    # Afficher tous les livres
    return render_template('liste.html', livres=bibliotheque.livres)

@app.route('/print')
def print_books():
    # Retourner la page d'impression avec la liste des livres
    return render_template('print.html', livres=bibliotheque.livres)

# @app.route('/print_content')
# def print_content():
#     # Retourner la page dédiée à l'impression
#     from datetime import datetime
#     current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     return render_template('print_content.html', livres=bibliotheque.livres, current_date=current_date)
@app.route('/print_content')
def print_content():
    # Obtenir la date actuelle
    current_date = datetime.today().strftime('%Y-%m-%d')
    
    # Retourner uniquement le contenu à imprimer (les livres)
    return render_template('print_content.html', livres=bibliotheque.livres, current_date=current_date)



@app.route('/generate_pdf')
def generate_pdf():
    # Générer le PDF à partir du modèle HTML
    rendered = render_template('print.html', livres=bibliotheque.livres)

    # Convertir le HTML en PDF
    pdf = pdfkit.from_string(rendered, False)

    # Sauvegarder le fichier PDF temporairement
    pdf_file_path = os.path.join('static', 'livres_list.pdf')
    with open(pdf_file_path, 'wb') as f:
        f.write(pdf)

    # Retourner le PDF pour le téléchargement
    return send_file(pdf_file_path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)

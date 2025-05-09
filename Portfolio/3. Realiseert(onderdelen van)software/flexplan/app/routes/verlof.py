from flask import Blueprint, render_template, request
from app.models.werknemer import Werknemer
from app.models.verlofaanvraag import Verlofaanvraag

verlof_bp = Blueprint('verlof', __name__)

@verlof_bp.route('/', methods=['GET', 'POST'])
def verlof_aanvraag():
    if request.method == 'POST':
        naam = request.form['naam']
        startdatum = request.form['startdatum']
        einddatum = request.form['einddatum']
        werknemer = Werknemer(1, naam, "mail@test.nl", "wachtwoord", 40)
        aanvraag = Verlofaanvraag(1, werknemer, startdatum, einddatum)
        return f"Aanvraag ingediend door {werknemer.naam} van {startdatum} t/m {einddatum}"
    return render_template('aanvraag_form.html')

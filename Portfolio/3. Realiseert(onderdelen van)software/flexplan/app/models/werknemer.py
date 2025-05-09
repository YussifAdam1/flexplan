from .gebruiker import Gebruiker

class Werknemer(Gebruiker):
    def __init__(self, id, naam, email, wachtwoord, contracturen):
        super().__init__(id, naam, email, wachtwoord)
        self.contracturen = contracturen

    def verlof_aanvragen(self, aanvraag):
        print("Verlof aangevraagd:", aanvraag)

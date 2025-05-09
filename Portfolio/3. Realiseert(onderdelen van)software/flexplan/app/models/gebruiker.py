class Gebruiker:
    def __init__(self, id, naam, email, wachtwoord):
        self.id = id
        self.naam = naam
        self.email = email
        self.wachtwoord = wachtwoord

    def login(self):
        print(f"{self.naam} is ingelogd.")

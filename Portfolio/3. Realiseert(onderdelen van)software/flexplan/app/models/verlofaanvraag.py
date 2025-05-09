class Verlofaanvraag:
    def __init__(self, id, werknemer, startdatum, einddatum):
        self.id = id
        self.werknemer = werknemer
        self.startdatum = startdatum
        self.einddatum = einddatum
        self.status = "Ingediend"

    def aanvraag_beoordelen(self, goedgekeurd):
        self.status = "Goedgekeurd" if goedgekeurd else "Afgewezen"

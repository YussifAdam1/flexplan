class Rooster:
    def __init__(self, id, datum, werknemers=[]):
        self.id = id
        self.datum = datum
        self.werknemers = werknemers

    def maak_rooster(self):
        print("Rooster aangemaakt voor", self.datum)

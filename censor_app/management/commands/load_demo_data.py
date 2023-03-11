from django.core.management.base import BaseCommand
from django.utils import timezone
from censor_app.models import Skole, Eksamen, Lærer, Censor, EksamensCensor, Skoleklasse
import random


def create_skole(navn, addresse):
    skole = Skole(navn=navn, addresse=addresse)
    skole.save()
    return skole


def create_lærer(navn, email, skole=None):
    lærer = Lærer(navn=navn, email=email, skole=skole)
    lærer.save()
    return lærer


def create_censor(navn, skole):
    censor = Censor(navn=navn, skole=skole)
    censor.save()
    return censor


def create_skoleklasse(navn, skole):
    klasse = Skoleklasse(navn=navn, skole=skole)
    klasse.save()
    return klasse


def create_eksamen(navn, skoleklasse, lærer=None, censor=None):
    eksamen = Eksamen(
        navn=navn,
        dato=timezone.now(),
        skoleklasse=skoleklasse,
        lærer=lærer,
        censor=censor,
    )
    eksamen.save()
    return eksamen


def create_eksamens_censor(eksamen, censor):
    eksamens_censor = EksamensCensor(eksamen=eksamen, censor=censor)
    eksamens_censor.save()
    return eksamens_censor


def create_random_skoler(num):
    for i in range(num):
        navn = f"Skole {i+1}"
        addresse = f"Addresse {i+1}"
        create_skole(navn, addresse)


def create_random_lærere(num, skoler):
    for i in range(num):
        navn = f"Lærer {i+1}"
        email = f"laerer{i+1}@skole.dk"
        skole = random.choice(skoler)
        create_lærer(navn, email, skole)


def create_random_censorer(num, skoler):
    for i in range(num):
        navn = f"Censor {i+1}"
        skole = random.choice(skoler)
        create_censor(navn, skole)


def create_random_skoleklasser(num, skoler):
    for i in range(num):
        navn = f"Klasse {i+1}"
        skole = random.choice(skoler)


def create_random_eksamen(skoleklasse, lærere, censorer):
    navn = f"Eksamen {timezone.now().strftime('%Y%m%d%H%M%S')}"
    lærer = random.choice(lærere)
    censor = random.choice(censorer)
    return create_eksamen(navn, skoleklasse, lærer, censor)


def create_random_eksamens_censor(eksamen, censorer):
    censor = random.choice(censorer)
    return create_eksamens_censor(eksamen, censor)


class Command(BaseCommand):
    help = "Load demo data into the database"

    def handle(self, *args, **kwargs):
        self.stdout.write("Loading demo data...")

        skoler = create_random_skoler(5)
        lærere = create_random_lærere(10, skoler)
        censorer = create_random_censorer(5, skoler)
        skoleklasser = create_random_skoleklasser(5, skoler)

        for skoleklasse in skoleklasser:
            for i in range(3):
                eksamen = create_random_eksamen(skoleklasse, lærere, censorer)
                eksamens_censor = create_random_eksamens_censor(eksamen, censorer)

        self.stdout.write(self.style.SUCCESS("Demo data loaded successfully!"))

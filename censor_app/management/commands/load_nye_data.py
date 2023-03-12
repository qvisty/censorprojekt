from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command


class Command(BaseCommand):
    help = "Loads initial data for the application"

    def handle(self, *args, **options):
        call_command("makemigrations")
        call_command("migrate")
        call_command("loaddata", "skole.json")
        call_command("loaddata", "lærer.json")
        call_command("loaddata", "skoleklasse.json")
        call_command("loaddata", "censor.json")
        call_command("loaddata", "eksamen.json")
        call_command("runserver")

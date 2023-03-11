import os
import sys

# Importer Django-indstillinger
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "censorprojekt.settings")
django.setup()

# Importer modeller
from censor_app.models import *
from django.db import models
from django.apps import apps

# Funktion til at udskrive modeller og felter
def print_models(output_file):
    # Åbn tekstfil til skrivning
    with open(output_file, "w") as f:
        # Gennemgå alle modeller og deres felter
        for name, obj in globals().items():
            if isinstance(obj, type) and issubclass(obj, models.Model):
                normal_fields = []
                foreign_key_fields = []
                for field in obj._meta.fields:
                    field_name = field.name
                    if isinstance(field, models.ForeignKey):
                        field_name = f"* {field_name}"
                        foreign_key_fields.append(field_name)
                    else:
                        normal_fields.append(field_name)
                all_fields = normal_fields + foreign_key_fields
                # Udskriv modelnavn og felter til konsol og tekstfil
                print(f"{name}:")
                f.write(f"{name}:\n")
                for field_name in all_fields:
                    if field_name == "id":
                        continue
                    print(f"- {field_name}")
                    f.write(f"- {field_name}\n")
                # Tilføj tom linje til adskillelse mellem modeller
                print("")
                f.write("\n")

print_models("models.txt")

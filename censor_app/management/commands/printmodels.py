from django.core.management.base import BaseCommand
from django.db import models
import matplotlib.pyplot as plt
from django.apps import apps


class Command(BaseCommand):
    help = "Prints a table of all models and their fields"

    def handle(self, *args, **options):

        # Opret en liste af modeller og deres felter
        data = []
        max_fields = 0
        for model in apps.get_models():
            fields = [f.name for f in model._meta.fields if f.name != "id"]
            if not fields:
                fields = [""]
            data.append([model.__name__] + fields)
            if len(fields) > max_fields:
                max_fields = len(fields)

        # Tilføj tomme strenge til rækker med færre felter end den model med flest felter
        for i, row in enumerate(data):
            while len(row) < max_fields + 1:
                row.append("")

        # Opret en figur og en akse til tabellen
        fig, ax = plt.subplots(1, 1)
        ax.axis("off")

        # Opret tabellen som et billede og tilføj den til akset
        table = ax.table(
    cellText=data,
    colLabels=None,
    colWidths=[0.3] * (max_fields + 1),
    cellLoc="left",
    loc="center",
)

        # Juster placeringen af felt kolonnerne for hver model
        for i, model in enumerate(apps.get_models()):
            fields = [f.name for f in model._meta.fields if f.name != "id"]
            if not fields:
                fields = [""]
            for j, field in enumerate(fields):
                try:
                    cell = table[i + 1, j + 1]
                    cell.set_text_props(weight="bold")
                    cell.set_text_props(color="red")
                    cell._loc = "right"
                except KeyError:
                    pass


        # Gem figurer til fil
        fig.savefig("models.png", bbox_inches="tight", pad_inches=0)

        # Udskriv filnavnet på det gemte billede
        print("Table saved as models.png")
